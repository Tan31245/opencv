import cv2 as cv
import numpy as np
img = cv.imread('./Resources/Photos/cat.jpg')

# 1) Converting an image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('original',img)
# cv.imshow('grayscale',gray)


# 2) Blurring an image
blur = cv.GaussianBlur(img, (7,7),0)    # mid argument is kernel size which should be an odd number , third
                                        #is the standard deviation if it's zero then it auto calculates from the kernel size
# cv.imshow('blur',blur)

# 3) Edge cascade    We'll use Canny edge detector
edge=cv.Canny(blur,125,175)              #they are threshold values   Also,there are less edges in the blurred image
# cv.imshow("Edge",edge)

# 4)Dilating the image using the above Canny edges
dilate =cv.dilate(edge,(7,7), iterations=3)   # Applied on grayscale or Canny images to thicken the boundaries of objects
# cv.imshow('dilated',dilate)


# 5) Eroding (means turning back the dilated image to Canny edge)
erode=cv.erode(dilate,(7,7),iterations=3)
# cv.imshow('Erode',erode)

# 6) Resizing an image
# resized1 = cv.resize(edge,(1200,1200),interpolation= cv.INTER_AREA)          # AREA is suitable for downsizing an image but for enlarging it LINEAR or CUBIC is used
# resized2 = cv.resize(edge,(1200,1200),interpolation= cv.INTER_LINEAR)       
# resized3 = cv.resize(edge,(1200,1200),interpolation= cv.INTER_CUBIC)        # CUBIC is better than LINEAR for upsizing an image
# cv.imshow('Resized1',resized1)
# cv.imshow('Resized2',resized2)
# cv.imshow('Resized3',resized3)

# 7) Cropping an image
crop = img[300:500,300:500]       # img is just a numpy array so we can crop using array slicing
cv.imshow('Cropped',crop)
cv.waitKey(0)