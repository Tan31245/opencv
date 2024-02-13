import cv2 as cv
import numpy as np
img=cv.imread("./Resources/Photos/lady.jpg")
cv.imshow("Image",img)
# What happens in blurring is that we define a kernel size. That kernel is a window(matrix) and the middle pixel is blurred as a result of its surrounding pixels and it is done for the whole image. With this mental picture in mind,let's proceed with different types of blurring techniques

#1) Averaging   (middle one gets the average intensity of its surrounding 8 pixels)
average=cv.blur(img,(3,3))          # the higher kernel size, the more blurry the image gets
# cv.imshow("Average",average)

#2) Gaussian Blur (middle one gets the weighted average intensity of its surrounding 8 pixels)... this is why it is les blurry than average but it is more natural
gaussian = cv.GaussianBlur(img,(5,5),0)         # 3rd arg is standard deviation in the x direction
# if sigmay is set zero then it becomes equal to sigmax
# if sigmax is set zero then it is auto-calculated as sigma=0.3×((ksize x−1)×0.5−1)+0.8
# cv.imshow("Gaussian",gaussian)

#3) Median blurring         # Same as averaging but it calculates median instead of average of the surrounding 8 pixels
# It is more effective than reducing noise in an image as compared to averaging and GaussianBlur
median=cv.medianBlur(img,3) # Here this 3 indicates kernel size of (3,3)
# cv.imshow("median",median)

#4) Bilateral Blurring      # It is the most effective in computer vision projects as compared to other blurring techniques because it retains the edges in the image
# Here 5 is the diamter of pixel neighbourhood, 3rd arg is sigmacolor ... whose higher value indicates that more colours will be considered in the neighbourhood
# 4th argument is sigmaspace... whose larger value means that the pixels further out from the centre will influence the blurring calculation
bil=cv.bilateralFilter(img,10,35,25)  
cv.imshow("Bil",bil)
cv.waitKey(0)