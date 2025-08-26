"""
AR Face Filter Program
"""
import cv2
import os

class ARFaceFilter:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.marker_path = "glasses.png"

    def overlay_marker(self, frame, face_coords):
        """Overlay the marker on detected faces."""
        marker = cv2.imread(self.marker_path, cv2.IMREAD_UNCHANGED)
        for (x, y, w, h) in face_coords:
            marker_resized = cv2.resize(marker, (w, h // 2))
            marker_h, marker_w, _ = marker_resized.shape
            y_offset = y
            x_offset = x
            for i in range(marker_h):
                for j in range(marker_w):
                    if marker_resized[i, j][3] != 0:  # Check alpha channel
                        frame[y_offset + i, x_offset + j] = marker_resized[i, j][:3]

    def start(self):
        """Start the AR Face Filter program."""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Cannot access the webcam.")
            return

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture frame from webcam.")
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                self.overlay_marker(frame, faces)

                cv2.putText(frame, "Press 'q' to quit", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                cv2.imshow("AR Face Filter", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    ARFaceFilter().start()
