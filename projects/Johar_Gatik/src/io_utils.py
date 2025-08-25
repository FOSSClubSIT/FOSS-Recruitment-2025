# src/io_utils.py
import os
import cv2

def ensure_exists(path: str, kind: str = "file"):
    if kind == "file":
        if not os.path.isfile(path):
            raise FileNotFoundError(f"{path!r} not found.")
    else:
        if not os.path.isdir(path):
            raise FileNotFoundError(f"{path!r} directory not found.")

def imread_color(path: str):
    ensure_exists(path, "file")
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Failed to read image: {path}")
    return img

def imread_gray(path: str):
    ensure_exists(path, "file")
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Failed to read image: {path}")
    return img

def save_image(path: str, img):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not cv2.imwrite(path, img):
        raise IOError(f"Failed to write image to {path}")
