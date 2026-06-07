import cv2
import os


def get_model_path():
    """Find the face detection model file inside the models folder."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(project_root, "models", "haarcascade_frontalface_default.xml")


def main():
    model_path = get_model_path()

    if not os.path.exists(model_path):
        print(f"ERROR: Model file not found at: {model_path}")
        return

    face_cascade = cv2.CascadeClassifier(model_path)

    if face_cascade.empty():
        print("ERROR: Could not load the face detection model.")
        return

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("ERROR: Could not open webcam. Check if camera is connected.")
        return

    print("Face Detection started! Press 'q' to quit.")

    while True:
        success, frame = cap.read()

        if not success:
            print("ERROR: Failed to read frame from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        face_count = len(faces)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"Faces: {face_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Real-Time Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Program closed successfully.")


if __name__ == "__main__":
    main()