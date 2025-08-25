# src/features.py
import cv2
import numpy as np

class FeatureResult:
    def __init__(self, kp1, kp2, matches, pts1, pts2):
        self.kp1 = kp1
        self.kp2 = kp2
        self.matches = matches
        self.pts1 = pts1  # Nx1x2 float32 (ref)
        self.pts2 = pts2  # Nx1x2 float32 (scene)

def detect_and_match_orb(ref_img_gray, scene_img_gray,
                         nfeatures=2000, cross_check=True,
                         max_matches=500, keep_ratio=1.0):
    """
    Detect ORB keypoints, brute-force match with Hamming distance,
    return top matches. keep_ratio in (0,1] picks a fraction of best matches.
    """
    if keep_ratio <= 0 or keep_ratio > 1:
        raise ValueError("keep_ratio must be in (0,1].")

    orb = cv2.ORB_create(
        nfeatures=nfeatures,
        scaleFactor=1.2,
        nlevels=8,
        edgeThreshold=31,
        patchSize=31,
        fastThreshold=20,
    )
    kp1, des1 = orb.detectAndCompute(ref_img_gray, None)
    kp2, des2 = orb.detectAndCompute(scene_img_gray, None)

    if des1 is None or des2 is None or len(kp1) < 10 or len(kp2) < 10:
        raise ValueError("Not enough keypoints/descriptors found. "
                         "Try different images or more features.")

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=cross_check)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda m: m.distance)

    if keep_ratio < 1.0:
        k = max(10, int(len(matches) * keep_ratio))
        matches = matches[:k]

    matches = matches[:max_matches]

    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    return FeatureResult(kp1, kp2, matches, pts1, pts2)
