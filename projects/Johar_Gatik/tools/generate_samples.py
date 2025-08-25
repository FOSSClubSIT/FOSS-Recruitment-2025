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

    # add light noise/text to avoid being too clean
    cv2.putText(comp, "MINI AR DEMO", (30, out_h - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (50, 50, 50), 3, cv2.LINE_AA)
    return comp

def main():
    marker = make_marker(460)
    scene  = compose_scene(marker)
    ref_path = os.path.join(ASSETS, "reference.png")
    scn_path = os.path.join(ASSETS, "scene.png")
    cv2.imwrite(ref_path, marker)
    cv2.imwrite(scn_path, scene)
    print(f"[OK] Wrote {ref_path}")
    print(f"[OK] Wrote {scn_path}")

if __name__ == "__main__":
    np.random.seed(42)  # determinism for reviewers
    main()
