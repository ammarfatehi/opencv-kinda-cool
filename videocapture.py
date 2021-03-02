import cv2, random
import numpy as np

cap = cv2.VideoCapture(
    0)  # u put in the number of the webcam you want to use; if you want to use a pre recorded video just add the file to this folder and put the route to the video in the ()

while True:
    ret, frame = cap.read()  # gets the image of the current frame; ret tells you if the capture was successful
    width = int(cap.get(
        3))  # the integer represents the property we want from cap; by default these come as floating point values but we need ints for slice
    height = int(cap.get(4))

    # adding 4 videos at once with all different orientations
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=.5, fy=.5)

    image[:height // 2, :width // 2] = smaller_frame  # pasting the smaller frame into the top left corner
    image[height // 2:, :width // 2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)   # pasting the smaller frame into the bottom left corner
    image[:height // 2, width // 2:] = smaller_frame   # pasting the smaller frame into the top right corner
    image[height // 2:, width // 2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)  # pasting the smaller frame into the bottom left corner

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break  # waits 1ms and if q has been pressed: break

cap.release()  # releases the camera so other programs can use the device
cv2.destroyAllWindows()
