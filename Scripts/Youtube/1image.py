import cv2 as cv

#img = cv.imread('Photos/MarsDialog.png')

#cv.imshow('YEET NAME', img)

def myReescelator(frame, scale=0.75):
    width = int (frame.shape[1]*scale)
    height = int (frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


myVid = cv.VideoCapture(0)#'Videos/GameOfLife.mp4')#0 is webcam

while True:
    isTrue, frame = myVid.read()
    frameSmall = myReescelator(frame,1.5)
    cv.imshow('YeetVideo', frameSmall)

    if cv.waitKey(20) & 0xFF == ord('d'):
       break

myVid.release()
cv.destroyAllWindows()
