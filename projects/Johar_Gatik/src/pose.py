# src/pose.py
import cv2
import numpy as np

def estimate_homography(pts_ref, pts_scene, ransac_thresh=3.0,
                        max_iters=5000, confidence=0.995):
    """
    Computes homography H such that: scene_pts ~ H * ref_pts
    pts_* are Nx1x2 float32 arrays.
    """
    H, mask = cv2.findHomography(
        pts_ref, pts_scene,
        cv2.RANSAC, ransac_thresh,
        maxIters=max_iters, confidence=confidence
    )
    if H is None:
        raise ValueError("Homography estimation failed (H is None).")
    inliers = int(mask.sum()) if mask is not None else 0
    return H, mask, inliers

def intrinsics_from_image(shape_hw, f_scale=1.2):
    """
    Build a simple camera intrinsics matrix K based on image size.
    This is a heuristic (no calibration required).
    """
    h, w = shape_hw
    f = f_scale * max(h, w)
    K = np.array([[f, 0, w / 2.0],
                  [0, f, h / 2.0],
                  [0, 0, 1.0]], dtype=np.float64)
    return K

def projection_from_homography(H, K):
    """
    Decompose homography (plane at Z=0) to [R|t] and return projection P = K [R|t].
    Method: K^-1 H = [r1 r2 t] up to scale, then orthonormalize R via SVD.
    """
    K_inv = np.linalg.inv(K)
    Hn = K_inv @ H

    r1 = Hn[:, 0]
    r2 = Hn[:, 1]
    t  = Hn[:, 2]

    # Normalize rotation vectors
    norm1 = np.linalg.norm(r1)
    norm2 = np.linalg.norm(r2)
    if norm1 == 0 or norm2 == 0:
        raise ValueError("Degenerate homography for pose.")

    scale = (norm1 + norm2) / 2.0
    r1 /= norm1
    r2 /= norm2
    r3 = np.cross(r1, r2)

    R = np.column_stack((r1, r2, r3))
    U, _, Vt = np.linalg.svd(R)
    R = U @ Vt
    if np.linalg.det(R) < 0:
        R[:, 2] *= -1.0

    t = t / scale
    P = K @ np.column_stack((R, t))
    return P, R, t
