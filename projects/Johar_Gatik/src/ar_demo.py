# src/ar_demo.py
import argparse
import sys
import time
import cv2
import numpy as np

from io_utils import imread_color, imread_gray, save_image
from features import detect_and_match_orb
from pose import estimate_homography, intrinsics_from_image, projection_from_homography
from overlay import warp_ref_corners_to_scene, draw_polygon, draw_cube

def parse_args():
    p = argparse.ArgumentParser(
        description="Mini AR with OpenCV — offline-first homography + (optional) cube overlay."
    )
    p.add_argument("--reference", "-r", required=True, help="Path to reference image (marker).")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--scene", "-s", help="Path to scene image.")
    src.add_argument("--webcam", action="store_true", help="Use webcam (optional).")

    p.add_argument("--save", help="Path to save output image/frame.", default=None)
    p.add_argument("--draw-cube", action="store_true", help="Overlay a 3D cube.")
    p.add_argument("--keep-ratio", type=float, default=1.0, help="Fraction of best matches to keep (0,1].")
    p.add_argument("--nfeatures", type=int, default=2000, help="ORB nfeatures.")
    p.add_argument("--ransac", type=float, default=3.0, help="RANSAC reprojection threshold (px).")
    p.add_argument("--show", action="store_true", help="cv2.imshow the result window.")
    p.add_argument("--f-scale", type=float, default=1.2, help="Virtual intrinsics focal length scale.")
    return p.parse_args()

def process_single_frame(ref_bgr, ref_gray, frame_bgr, args):
    scene_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

    feats = detect_and_match_orb(
        ref_gray, scene_gray,
        nfeatures=args.nfeatures, keep_ratio=args.keep_ratio
    )

    H, mask, inliers = estimate_homography(
        feats.pts1, feats.pts2,
        ransac_thresh=args.ransac
    )

    # Draw detected quadrilateral
    h_ref, w_ref = ref_gray.shape[:2]
    quad = warp_ref_corners_to_scene(H, w_ref, h_ref)
    out = frame_bgr.copy()
    draw_polygon(out, quad, color=(0, 255, 0), thickness=2)

    if args.draw_cube:
        # Build simple intrinsics from scene size
        h_sc, w_sc = scene_gray.shape[:2]
        K = intrinsics_from_image((h_sc, w_sc), f_scale=args.f_scale)
        P, R, t = projection_from_homography(H, K)
        draw_cube(out, P, w_ref, h_ref, height_factor=0.5, color=(255, 0, 0), thickness=2)

    return out, inliers, len(feats.matches)

def main():
    args = parse_args()

    ref_bgr = imread_color(args.reference)
    ref_gray = imread_gray(args.reference)

    if args.scene:
        frame_bgr = imread_color(args.scene)
        out, inliers, total_matches = process_single_frame(ref_bgr, ref_gray, frame_bgr, args)
        print(f"[INFO] matches={total_matches}, inliers={inliers}")
        if args.show:
            cv2.imshow("AR Result", out)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if args.save:
            save_image(args.save, out)
    else:
        # Webcam mode (optional)
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("[ERROR] Cannot open webcam.", file=sys.stderr)
            sys.exit(1)
        try:
            fps_t0 = time.time(); frames = 0
            while True:
                ok, frame_bgr = cap.read()
                if not ok:
                    break
                try:
                    out, inliers, total_matches = process_single_frame(ref_bgr, ref_gray, frame_bgr, args)
                    cv2.putText(out, f"matches={total_matches} inliers={inliers}",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (20, 220, 20), 2, cv2.LINE_AA)
                except Exception as e:
                    out = frame_bgr
                    cv2.putText(out, f"ERR: {str(e)}",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

                cv2.imshow("AR Webcam", out)
                key = cv2.waitKey(1) & 0xFF
                if key == 27 or key == ord('q'):
                    break

                frames += 1
                if frames % 30 == 0:
                    t = time.time(); dt = t - fps_t0
                    fps = frames / max(dt, 1e-6)
                    print(f"[INFO] streaming fps ~ {fps:.1f}")
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
