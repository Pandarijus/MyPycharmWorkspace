import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # creates blank canvis

# blank[200:300, 100:200] = 255, 0, 0#bgr  blue green red
# cv.imshow('BlueRect', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 225, 0), thickness=2)  # thickness = -1 is fill
cv.circle(blank, (250, 250), 40, (0, 225, 0), thickness=2)
cv.line(blank, (0, 0), (300, 300), (0, 200, 200), thickness=2)
cv.putText(blank, 'Hello',(0,400),cv.FONT_HERSHEY_TRIPLEX, 0.8, (20,0,20), 2)
cv.imshow('SquYERT', blank)
cv.waitKey(0)
