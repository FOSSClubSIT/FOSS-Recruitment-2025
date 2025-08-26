# tools/generate_samples.py
"""
Face Detection with Marker Overlay
"""
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image

def overlay_marker(frame, face_coords, marker):
    for (x, y, w, h) in face_coords:
        marker_resized = cv2.resize(marker, (w, h // 2))
        marker_h, marker_w, _ = marker_resized.shape

        y_offset = y - marker_h if y - marker_h > 0 else y
        x_offset = x

        for i in range(marker_h):
            for j in range(marker_w):
                if marker_resized[i, j][3] != 0:  # Check alpha channel
                    frame[y_offset + i, x_offset + j] = marker_resized[i, j][:3]

def start_webcam():
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load marker image (e.g., glasses or hat with transparency)
    marker = cv2.imread('marker.png', cv2.IMREAD_UNCHANGED)
    if marker is None:
        messagebox.showerror("Error", "Marker image not found. Please ensure 'marker.png' is in the same directory.")
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

            overlay_marker(frame, faces, marker)

            cv2.putText(frame, "Press 'q' to quit", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("Webcam Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    start_webcam()
