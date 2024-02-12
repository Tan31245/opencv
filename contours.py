import cv2 as cv
import numpy as np
# contours are the boundaries of objects  (like edges not exactly same but similar)
img=cv.imread("./Resources/Photos/lady.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3),0) 
edge = cv.Canny(img,125,175)         
ret,thresh=cv.threshold(edge,125,255,cv.THRESH_BINARY)
# it binarises the image i.e. if a pixel density<125 it's set to black else set to 255 (white)
# thresholding_type
contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# contours is a python list of all coordinates of the found contours
# RETR_EXTERNAL for only the outside contours
# RETR_TREE for hierarchical contours
# RETR_LIST for all contours
# contour approximation method CHAIN_APPROX_SIMPLE compresses all found contours into simple ones
blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank,contours,-1,(0,255,0),thickness=2)
# countourIndex = -1 specifies all contours we can set particular indices here
# color set to green
cv.imshow("Lady",gray)
cv.imshow("contours",blank)
cv.imshow("Binary",thresh)
cv.imshow("Canny",edge)
cv.waitKey(0)