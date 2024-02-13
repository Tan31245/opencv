import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("./Resources/Photos/group 2.jpg")

cv.imshow("Image",img)

# A color image basically consists of color channels, basically Red,Green and Blue ... All of them merged
# 1) Splitting the image into its channels
b,g,r=cv.split(img)                 # Will be shown as grayscale images to reprent different intensity distribution... Whiter indicates more intensity
# cv.imshow("Blue",b)
# cv.imshow("Green",g)
# cv.imshow("Red",r)

print(img.shape)                    # see the 3rd dimension in the tuple that represents color channels
print(b.shape)                      # Here only the dimensions are shown
print(g.shape)
print(r.shape)
# 2) Merging color channels
merged=cv.merge([b,g,r])
# cv.imshow("Merged",merged)

# 3) Showing color of images as individual channels
blank=np.zeros(b.shape,dtype='uint8')
# This always takes 3 arguments If we want to just merge 2 channels pass in a blank image... Just "blacken" the intensity distribution of other channels
merged_blue=cv.merge([b,blank,blank])                
merged_red=cv.merge([blank,blank,r])
merged_green=cv.merge([blank,g,blank])
cv.imshow("Blue",merged_blue)
cv.imshow("Green",merged_green)
cv.imshow("Red",merged_red)
cv.waitKey(0)
cv.destroyAllWindows()