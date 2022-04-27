import cv2 as cv

img = cv.imread('../../Photos/MarsDialog.png')




def myReescelator(frame, scale=0.75):
    width = int (frame.shape[1]*scale)
    height = int (frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

ogImage = myReescelator(img,.2)

cv.imshow('Original', ogImage)

img = cv.cvtColor(ogImage,cv.COLOR_BGR2GRAY)


#img = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('After Yeet', img)

#EDGE DETECTION!!!!!!!!!!!!!!
img = cv.Canny(img,125,175)

img = ogImage[50:300, 200:400]

cv.imshow('cropped', img)
cv.waitKey(0)








