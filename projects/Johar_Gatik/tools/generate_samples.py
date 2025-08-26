# tools/generate_samples.py
"""
AR Object Tracker and Annotator
"""
import cv2
import tkinter as tk
from tkinter import simpledialog

class ARObjectTracker:
    def __init__(self):
        self.window_name = "AR Object Tracker"
        self.tracker = self.create_tracker()
        self.bbox = None
        self.annotating = False

    def create_tracker(self):
        """Create a tracker, falling back to available options if necessary."""
        try:
            return cv2.TrackerCSRT_create()
        except AttributeError:
            print("CSRT tracker not available. Falling back to KCF tracker.")
            return cv2.TrackerKCF_create()

    def start(self):
        """Start the AR Object Tracker."""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Cannot access the webcam.")
            return

        cv2.namedWindow(self.window_name)

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture frame from webcam.")
                    break

                if self.annotating:
                    # Update tracker and draw bounding box
                    success, self.bbox = self.tracker.update(frame)
                    if success:
                        x, y, w, h = [int(v) for v in self.bbox]
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, "Tracking", (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    else:
                        cv2.putText(frame, "Lost Track", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

                cv2.putText(frame, "Press 'a' to annotate, 'q' to quit", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                cv2.imshow(self.window_name, frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('a'):
                    self.annotate(frame)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def annotate(self, frame):
        """Annotate an object by selecting a bounding box."""
        self.bbox = cv2.selectROI(self.window_name, frame, fromCenter=False, showCrosshair=True)
        self.tracker.init(frame, self.bbox)
        self.annotating = True

if __name__ == "__main__":
    tracker = ARObjectTracker()
    tracker.start()
