"""
AR Face Filter Program with Hyper-Realistic Glasses Overlay
"""
import cv2
import mediapipe as mp
import numpy as np

class ARFaceFilter:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
        self.drawing_utils = mp.solutions.drawing_utils
        self.drawing_styles = mp.solutions.drawing_styles
        self.glasses = cv2.imread("glasses.png", cv2.IMREAD_UNCHANGED)

    def overlay_glasses(self, frame, landmarks):
        """Overlay glasses on the face using facial landmarks."""
        # Extract key points for the eyes
        left_eye = landmarks[33]  # Example landmark for left eye
        right_eye = landmarks[263]  # Example landmark for right eye
        nose_bridge = landmarks[168]  # Example landmark for nose bridge

        # Calculate the width and height of the glasses
        glasses_width = int(np.linalg.norm(np.array(left_eye) - np.array(right_eye)))
        glasses_height = int(glasses_width * self.glasses.shape[0] / self.glasses.shape[1])

        # Resize the glasses image
        resized_glasses = cv2.resize(self.glasses, (glasses_width, glasses_height))

        # Calculate the position to overlay the glasses
        x = int(nose_bridge[0] - glasses_width / 2)
        y = int(nose_bridge[1] - glasses_height / 2)

        # Overlay the glasses on the frame
        for i in range(glasses_height):
            for j in range(glasses_width):
                if resized_glasses[i, j][3] != 0:  # Check alpha channel
                    frame[y + i, x + j] = resized_glasses[i, j][:3]

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

                # Convert the frame to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Process the frame with Mediapipe Face Mesh
                results = self.face_mesh.process(rgb_frame)

                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        # Extract landmark coordinates
                        landmarks = [(int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]))
                                     for landmark in face_landmarks.landmark]

                        # Overlay glasses
                        self.overlay_glasses(frame, landmarks)

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
