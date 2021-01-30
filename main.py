
import cv2

cap = cv2.VideoCapture("Roads - 1952.mp4")

# Object detection from stable camera
object_detector = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()
    height, width,_ = frame.shape

    # print(height,width)

    # Extract the field of intrest
    roi = frame[150:,295:]
    print(roi)

    # Object dection
    mask = object_detector.apply(frame)
    countor, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in countor:
        # Calculate the area and eleminate small areas
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(frame,[cnt],-1,(0,255,0))
    

    cv2.imshow("Roi",roi)
    cv2.imshow("Frame",frame)
    # cv2.imshow("Mask",mask)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()