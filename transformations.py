import cv2 as cv
import numpy as np
img=cv.imread("./Resources/Photos/park.jpg")
cv.imshow("Boston",img)

#1) Translation
def translate(img,x,y):                                 # +x ->right  -x->left   +y->down    -y->up
    transMat=np.float32([[1,0,x],[0,1,y]])              # Here 1's are the scaling factor in x and y directions, 0's are the shearing factor
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)       # cv.warpAffine takes a Affine Transformation Matrix (2x3) which defines how to change the image
# P' = MP       where M is matrix and P is column vector of a point i.e its x and y coordinates
# img_translated=translate(img,100,0)
# cv.imshow("Boston2",img_translated)

#2) Rotation
def rotate(img,angle,rot_point=None):
    height = img.shape[0]
    width  = img.shape[1]
    if rot_point is None:
        rot_point=(height//2,width//2)
    dim=(width,height)    
    rotMat=cv.getRotationMatrix2D(rot_point,angle,1.0)          # angle in degrees and anticlockwise... -ve value for clockwise
    return cv.warpAffine(img,rotMat,dim)
img_rotated=rotate(img,90)              
# We can also rotate a rotated image but the parts which have been cut due to rotation will still be persistent through the second rotation
# cv.imshow("Rotated",img_rotated)

# interpolation in resizing refers to the technique used to estimate the pixel values of the new image when resizing an image from one resolution to another. Interpolation is necessary because when you resize an image, you are essentially changing the spatial arrangement of pixels, and you need to estimate the intensity values of the pixels in the new positions.

#3) Resizing
def resize(img,width,height):
    return cv.resize(img,(width,height),interpolation=cv.INTER_AREA)        # for enlarging cubic>linear>area>default 
    #for shrinking area>default
# resized=resize(img,100,600)                                   # Always when dimensions are passed in a cv function they are passed as (width,height)
# cv.imshow("Resized",resized)

#4) Flipping
flipped= cv.flip(img,0)             # 1 for horizontal flip, 0 for vertical , -1 for both
cv.imshow("Flipped",flipped)
cv.waitKey(0) 