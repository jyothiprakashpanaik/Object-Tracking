
import cv2

cap = cv2.VideoCapture("Roads - 1952.mp4")

# Object detection from stable camera


while True:
    ret, frame = cap.read()

    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()