import cv2, random
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert your BGR image to HSV

    # extracting a single color
    lower_red = np.array([10, 167, 37])  # HSV
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)  # a portion of an image

    result = cv2.bitwise_and(frame, frame, mask=mask)   # this pretty much gets rid of all the pixels that arent in our mask (not in our pixel range)

    cv2.imshow('frame', result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
