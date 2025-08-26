"""
AR Face Filter Program with Realistic Glasses Overlay
"""
import argparse
import sys
import time
import cv2
import numpy as np

from src.io_utils import imread_color, imread_gray, save_image
from src.features import detect_and_match_orb
from src.overlay import draw_polygon
from src.pose import estimate_homography

# Main AR functionality
def process_frame(ref_bgr, ref_gray, frame_bgr):
    scene_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    feats = detect_and_match_orb(ref_gray, scene_gray)
    H, mask, inliers = estimate_homography(feats.pts1, feats.pts2)
    out = frame_bgr.copy()
    draw_polygon(out, H, color=(0, 255, 0), thickness=2)
    return out

def main():
    ref_path = "path_to_reference_image"
    ref_bgr = imread_color(ref_path)
    ref_gray = imread_gray(ref_path)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame_bgr = cap.read()
        if not ret:
            break
        out = process_frame(ref_bgr, ref_gray, frame_bgr)
        cv2.imshow("AR", out)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
