import cv2

# Initialize the camera (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

print("Press 'q' to close the window.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Is your camera being used by another app?")
        break

    # Show the video feed
    cv2.imshow('Camera Test', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()