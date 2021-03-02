import cv2
import numpy as np

img = cv2.imread('assets/zentisu.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # convert the image to gray scale

corners = cv2.goodFeaturesToTrack(img_gray, 100, .01, 10,)     # runs the shi tomasi corner detector algo
corners = np.int0(corners)  # turn the floating point numbers into integers

for corner in corners:
    x, y = corner.ravel()   # flats the array (removing the internal arrays) [[1,2], [1,2]] - > [1,2,1,2]
    cv2.circle(img, (x, y), 5, (255,0,0), -1)

# drawing a line between all the corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()