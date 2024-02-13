import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("./Resources/Photos/group 2.jpg")

cv.imshow("Image",img)

# 1) BGR to Gray Scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# 2) BGR to HSV(Hue Saturation Value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

# 3) BGR to Lab                       # Lab : L for lightness a,b for color opponent dimensions... The way how we perceive color differences
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("Lab",lab)

# 4) BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("rgb",rgb)                # We see inversion of colours but it is correct outside of opencv such as matplotlib
# plt.imshow(rgb)
# plt.show()

# 5) HSV to BGR                 
# bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow("bgr",bgr)

# 6) Lab to BGR
# bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
# cv.imshow("bgr",bgr)

# 7) Gray to BGR                    # We can't convert gray to HSV directly We have to convert gray to BGR and then BGR to HSV
bgr=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)         # No colours will be restored because the color channel is only one in grayscale images and the color info is lost
cv.imshow("bgr",bgr)
cv.waitKey(0)
cv.destroyAllWindows()
