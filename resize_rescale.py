import cv2 as cv
def rescale_frame(frame,scale=0.5):   #works with images,vids and webcam
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

def res_Change(width,height):       # only works with webcam
    capture.set(3,width)
    capture.set(4,height)

# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('cat',img)
# img_resized= rescale_frame(img)
# cv.imshow('cat_resized',img_resized)
# cv.waitKey(0)                  # Press any key on keyboard to close the image window
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0,cv.CAP_V4L)     # using 0 as argument take live video from web camera and subsequent integers represent external cameras connected
# cv.CAP_V4L it's a different backend for VideoCapture API , the default one was giving errors
res_Change(400,300)

while True:
    isTrue,frame = capture.read()
    # frame_resized = rescale_frame(frame,0.75)
    cv.imshow('Video_original',frame)
    if(cv.waitKey(100) & 0xFF==ord('d')):                # press d to close the video window Also, cv.waitKey(20)==ord('d') can be written ... 0 in the waitkey value denotes infinity
        break                                           # basically waitkey(10) introduces a delay of 10 milliseconds between the frames and returns the ASCII value of the keyboard key pressed

capture.release()
cv.destroyAllWindows()
