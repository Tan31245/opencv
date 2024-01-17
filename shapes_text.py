import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8') #blank image

# 1. Paint the colour blue
cv.imshow('Blank',blank)
blank[:] = 255,0,0                   #GRB
cv.imshow('Blue',blank)
cv.waitKey(0)

# 2. Paint some portions of the image blue
blank[300:400,200:300] = 0,0,255                   #BGR
# 300 to 400 row numbers and 200 to 300 column numbers
# by 300,400 we can access individual pixels
cv.imshow('Blue',blank)
cv.waitKey(0)

# 3.  Draw a rectangle over an image
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness= -1)   # arguments are point1 , point2 , colour , line thickness in pixels 
#if thickness given negative value or cv.FILLED rectangle will be filled
cv.imshow('Rectangle',blank)
cv.waitKey(0)

# 4. Draw a circle
cv.circle(blank,(250,250),50,(0,0,255),thickness= -1)   # arguments are center , radius in pixels , colour , line thickness in pixels 
cv.imshow('Circle',blank)
cv.waitKey(0)

# 5, Draw a line
cv.line(blank,(5,5),(250,250),(255,0,0),2)    # the two points as arguments through which the line has to pass through
cv.imshow('Line',blank)
cv.waitKey(0)

# 6. Write some text
cv.putText(blank,"hello",org =(225,225),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale =1,color = (0,255,255))
cv.imshow('text',blank)
cv.waitKey(0)

