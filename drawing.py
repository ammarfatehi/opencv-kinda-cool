import cv2, random
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # drawing lines
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0),
                   10)  # drawing a line on an image cv2.line(frame, start, finish, color, thickness)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0),
                   5)  # drawing a line on an image cv2.line(frame, start, finish, color, thickness)

    # drawing a rectangle
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128),
                        5)  # cv2.rectangle(frame, start, finish, color, thickness (if -1 then it fills the rectangle)

    # drawing a circle
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    # drawing text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "This is text i think", (200, height - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
