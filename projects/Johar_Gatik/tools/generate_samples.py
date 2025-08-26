# tools/generate_samples.py
"""
Interactive GUI-based program for AR marker generation and webcam feature matching.
"""
import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

def webcam_mode(marker):
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

def upload_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return None

    marker = cv2.imread(file_path)
    if marker is None:
        messagebox.showerror("Error", "Failed to read the image.")
        return None

    messagebox.showinfo("Info", "Image uploaded successfully. Starting webcam mode.")
    webcam_mode(marker)

def main_gui():
    root = tk.Tk()
    root.title("AR Marker Program")
    root.geometry("400x200")

    label = tk.Label(root, text="Choose an Operation", font=("Arial", 16))
    label.pack(pady=20)

    upload_button = tk.Button(root, text="Upload Marker Image", font=("Arial", 14), command=upload_image)
    upload_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
