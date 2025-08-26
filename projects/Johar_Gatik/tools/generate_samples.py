# tools/generate_samples.py
"""
Advanced AR Program: Real-Time Face Detection with Virtual Object Overlay
Automatically generates a placeholder glasses image if not found.
"""
import cv2
import numpy as np
import os
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox

def create_placeholder_glasses():
    """Create a placeholder glasses image."""
    width, height = 200, 100
    glasses = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    draw = ImageDraw.Draw(glasses)
    draw.rectangle([20, 30, 80, 70], fill=(0, 0, 0, 255))  # Left lens
    draw.rectangle([120, 30, 180, 70], fill=(0, 0, 0, 255))  # Right lens
    draw.rectangle([80, 45, 120, 55], fill=(0, 0, 0, 255))  # Bridge

    glasses.save("objects/glasses.png")

def load_virtual_object(object_name):
    """Load the virtual object image based on the selected object name."""
    object_path = f"objects/{object_name}.png"
    if not os.path.exists(object_path):
        create_placeholder_glasses()
    return cv2.imread(object_path, cv2.IMREAD_UNCHANGED)

def overlay_virtual_object(frame, face_coords, virtual_object):
    """Overlay the virtual object on the detected face."""
    for (x, y, w, h) in face_coords:
        object_resized = cv2.resize(virtual_object, (w, h))
        obj_h, obj_w, _ = object_resized.shape

        y_offset = y
        x_offset = x

        for i in range(obj_h):
            for j in range(obj_w):
                if object_resized[i, j][3] != 0:  # Check alpha channel
                    frame[y_offset + i, x_offset + j] = object_resized[i, j][:3]

def start_advanced_ar():
    """Start the advanced AR program."""
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the default virtual object (e.g., glasses)
    virtual_object = load_virtual_object("glasses")
    if virtual_object is None:
        messagebox.showerror("Error", "Failed to load virtual object.")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot access the webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to capture frame from webcam.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            overlay_virtual_object(frame, faces, virtual_object)

            cv2.putText(frame, "Press 'q' to quit", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("Advanced AR Program", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ensure the objects directory exists
    if not os.path.exists("objects"):
        os.makedirs("objects")

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    start_advanced_ar()
