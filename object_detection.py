import cv2
import numpy as np

img_base = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/shoe.png', 0)
img_base = cv2.resize(img_base, (0, 0), fx=.8, fy=.8)
template = cv2.resize(template, (0, 0), fx=.8, fy=.8)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF,
           cv2.TM_SQDIFF_NORMED]  # these r all the different methods/algos u can apply to your image

for method in methods:
    img = img_base.copy()

    result = cv2.matchTemplate(img, template, method)  # (W-w+1, H-h+1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(
        result)  # returns the min and max value in the array and the location of them

    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        location = min_loc
    else:
        location = max_loc
    print(location)

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img, location, bottom_right, 255, 5)
    cv2.imshow('Match', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
