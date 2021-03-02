import cv2,random

img = cv2.imread('assets/zentisu.jpg',
                 1)  # BGR 0==grayscale -1==normal/default 1== if your image has transparency stuff happens?

# roating/resizing the image
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)
img = cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# how to save an updated image
# cv2.imwrite('new_zentisu.jpg', img)

# cv2.imshow('Image', img)  # show the image
# cv2.waitKey(0)  # wait an infinite amount of time for u to press a key to destroy the windows; 0 == infinitely, 5 = 5 secs
# cv2.destroyAllWindows()

print(img.shape)  # (height (row) ,width (column) ,channels) channels is the color of the image (BGR)

# changing values in the image
for i in range(100):
    for j in range(img.shape[1]):
        # rows,cols,channels
        img[i][j] = [random.randrange(255),random.randrange(255),random.randrange(255)]


# copying one part of the image and putting it somewhere else

tag = img[200:400,600:900]  # copies a sqaure of your array rows 500-700 and columns 600-900
img[100:300, 400:700] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
