"""
AR Face Filter Program with OpenCV Haar Cascades
"""
import cv2
import numpy as np

class ARFaceFilter:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.glasses = cv2.imread("glasses.png", cv2.IMREAD_UNCHANGED)

    def overlay_glasses(self, frame, face_coords):
        """Overlay glasses on detected faces."""
        for (x, y, w, h) in face_coords:
            glasses_width = w
            glasses_height = int(glasses_width * self.glasses.shape[0] / self.glasses.shape[1])

            # Resize the glasses image
            resized_glasses = cv2.resize(self.glasses, (glasses_width, glasses_height))

            # Calculate the position to overlay the glasses
            y_offset = y + int(h / 4)
            x_offset = x

            for i in range(glasses_height):
                for j in range(glasses_width):
                    if resized_glasses[i, j][3] != 0:  # Check alpha channel
                        if y_offset + i < frame.shape[0] and x_offset + j < frame.shape[1]:
                            frame[y_offset + i, x_offset + j] = resized_glasses[i, j][:3]

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

                self.overlay_glasses(frame, faces)

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
