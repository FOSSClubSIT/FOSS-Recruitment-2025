# tools/generate_samples.py
"""
Generate a synthetic marker (reference.png) and a scene (scene.png) by
warping the marker into a random quadrilateral on a plain background.
This makes the project fully offline and reproducible.
"""
import os
import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

def make_marker(size=400):
    img = np.full((size, size, 3), 255, np.uint8)
    # Thick black border
    cv2.rectangle(img, (10, 10), (size-10, size-10), (0, 0, 0), thickness=20)
    # Checkerboard interior (8x8)
    cells = 8
    cell = (size - 60) // cells
    ox = oy = 30
    for y in range(cells):
        for x in range(cells):
            if (x + y) % 2 == 0:
                cv2.rectangle(img,
                              (ox + x*cell, oy + y*cell),
                              (ox + (x+1)*cell, oy + (y+1)*cell),
                              (0, 0, 0), thickness=-1)
    # Add a unique identifier text
    cv2.putText(img, "AR-MARKER", (50, size - 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
    return img

def compose_scene(marker, out_h=720, out_w=960):
    bg = np.full((out_h, out_w, 3), 230, np.uint8)

    h, w = marker.shape[:2]
    src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

    # Random-ish convex quad
    margin = 80
    dst = np.float32([
        [np.random.randint(margin, out_w//2), np.random.randint(margin, out_h//2)],
        [np.random.randint(out_w//2, out_w-margin), np.random.randint(margin, out_h//2)],
        [np.random.randint(out_w//2, out_w-margin), np.random.randint(out_h//2, out_h-margin)],
        [np.random.randint(margin, out_w//2), np.random.randint(out_h//2, out_h-margin)],
    ])

    H = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(marker, H, (out_w, out_h))

    mask = np.zeros((out_h, out_w), np.uint8)
    cv2.fillConvexPoly(mask, dst.astype(np.int32), 255)
    inv = cv2.bitwise_not(mask)

    bg_fg = cv2.bitwise_and(warped, warped, mask=mask)
    bg_bg = cv2.bitwise_and(bg, bg, mask=inv)
    comp = cv2.add(bg_fg, bg_bg)

    # Add light noise/text to avoid being too clean
    cv2.putText(comp, "MINI AR DEMO", (30, out_h - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (50, 50, 50), 3, cv2.LINE_AA)
    return comp, H

def webcam_mode(marker):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot access the webcam.")
        return

    print("[INFO] Press 'q' to quit webcam mode.")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[ERROR] Failed to capture frame from webcam.")
                break

            # Convert frame to grayscale
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            marker_gray = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)

            # Detect and match features
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(marker_gray, None)
            kp2, des2 = orb.detectAndCompute(frame_gray, None)

            if des1 is not None and des2 is not None:
                bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                matches = bf.match(des1, des2)
                matches = sorted(matches, key=lambda x: x.distance)

                # Draw matches
                frame = cv2.drawMatches(marker, kp1, frame, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

            # Add overlay text and instructions
            overlay_text = "Webcam Mode: Press 'q' to quit"
            cv2.putText(frame, overlay_text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

            # Display the webcam feed
            cv2.imshow("Webcam Feed", frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def main():
    try:
        print("[INFO] Choose an option:")
        print("1. Generate synthetic marker and scene")
        print("2. Use webcam mode")
        print("3. Upload your own image")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            marker = make_marker(460)
            scene, homography = compose_scene(marker)
            ref_path = os.path.join(ASSETS, "reference.png")
            scn_path = os.path.join(ASSETS, "scene.png")
            homography_path = os.path.join(ASSETS, "homography.txt")

            cv2.imwrite(ref_path, marker)
            cv2.imwrite(scn_path, scene)
            np.savetxt(homography_path, homography, fmt="%.6f")

            print(f"[OK] Wrote {ref_path}")
            print(f"[OK] Wrote {scn_path}")
            print(f"[OK] Wrote homography matrix to {homography_path}")

            # Display the generated images
            cv2.imshow("Generated Marker", marker)
            cv2.imshow("Generated Scene", scene)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif choice == "2":
            marker = make_marker(460)  # Default marker for webcam mode
            webcam_mode(marker)
        elif choice == "3":
            file_path = input("Enter the path to your image: ")
            if not os.path.isfile(file_path):
                print("[ERROR] File not found.")
                return

            marker = cv2.imread(file_path)
            if marker is None:
                print("[ERROR] Failed to read the image.")
                return

            print("[INFO] Using uploaded image as marker.")
            webcam_mode(marker)
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

if __name__ == "__main__":
    np.random.seed(42)  # determinism for reviewers
    main()
