# tools/generate_samples.py
"""
AR Marker Detection and Overlay Program
"""
import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ARProgram:
    def __init__(self, root):
        self.root = root
        self.root.title("AR Marker Program")
        self.root.geometry("500x300")

        self.marker = None

        label = tk.Label(root, text="AR Marker Detection and Overlay", font=("Arial", 18))
        label.pack(pady=20)

        upload_button = tk.Button(root, text="Upload Marker Image", font=("Arial", 14), command=self.upload_image)
        upload_button.pack(pady=10)

        webcam_button = tk.Button(root, text="Start Webcam Mode", font=("Arial", 14), command=self.start_webcam)
        webcam_button.pack(pady=10)

        exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
        exit_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return

        self.marker = cv2.imread(file_path)
        if self.marker is None:
            messagebox.showerror("Error", "Failed to read the image.")
            return

        messagebox.showinfo("Info", "Image uploaded successfully. You can now start the webcam mode.")

    def start_webcam(self):
        if self.marker is None:
            messagebox.showerror("Error", "Please upload a marker image first.")
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

                # Convert frame to grayscale
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                marker_gray = cv2.cvtColor(self.marker, cv2.COLOR_BGR2GRAY)

                # Detect and match features
                orb = cv2.ORB_create()
                kp1, des1 = orb.detectAndCompute(marker_gray, None)
                kp2, des2 = orb.detectAndCompute(frame_gray, None)

                if des1 is not None and des2 is not None:
                    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                    matches = bf.match(des1, des2)
                    matches = sorted(matches, key=lambda x: x.distance)

                    # Draw matches
                    frame = cv2.drawMatches(self.marker, kp1, frame, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = ARProgram(root)
    root.mainloop()
