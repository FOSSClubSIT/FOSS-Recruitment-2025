# tools/generate_samples.py
"""
AR Measurement Tool: Measure distances in real-time using a webcam.
"""
import cv2
import numpy as np

class ARMeasurementTool:
    def __init__(self):
        self.points = []
        self.window_name = "AR Measurement Tool"

    def click_event(self, event, x, y, flags, param):
        """Handle mouse click events to select points."""
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))

            # Draw the point on the frame
            cv2.circle(self.frame, (x, y), 5, (0, 0, 255), -1)

            # If two points are selected, calculate and display the distance
            if len(self.points) == 2:
                self.calculate_distance()

    def calculate_distance(self):
        """Calculate the distance between two points."""
        point1, point2 = self.points
        distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

        # Display the distance on the frame
        cv2.line(self.frame, point1, point2, (255, 0, 0), 2)
        cv2.putText(self.frame, f"Distance: {distance:.2f} pixels", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

        # Reset points after displaying the distance
        self.points = []

    def start(self):
        """Start the AR Measurement Tool."""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Cannot access the webcam.")
            return

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.click_event)

        try:
            while True:
                ret, self.frame = cap.read()
                if not ret:
                    print("Error: Failed to capture frame from webcam.")
                    break

                # Display the frame
                cv2.imshow(self.window_name, self.frame)

                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    tool = ARMeasurementTool()
    tool.start()
