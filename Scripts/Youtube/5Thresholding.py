from Scripts.Success import bigBrain as bs
import cv2 as cv

img = bs.getPrepedImage()

#Version One
useless, thresh = cv.threshold(img, 60, 255, cv.THRESH_BINARY)

bs.show(thresh)
#Version Two
adapt = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 0)


bs.show(adapt)


cv.waitKey(0)
