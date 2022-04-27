import cv2 as cv
import numpy as np
from Scripts.Success import bigBrain as bs

vid = cv.VideoCapture(0)

camWidth = 1920*2
camHeight = 1080*2
vid.set(3,camWidth)
vid.set(4,camHeight)

detector = bs.getFingerDetector()

while True:
    isTrue,liveImage = vid.read()
    liveImage = cv.flip(liveImage,1)
    #liveImage = detector.drawHands(liveImage)

    success, fingersUp = detector.getFingerBoolUpList(liveImage)
    if success:
        print(fingersUp)
        for i in range(0,len(fingersUp),1):
            sideSlide = i * 60
            liveImage = cv.rectangle(liveImage,(0+sideSlide,0),(50+sideSlide,100),(255*fingersUp[i],0,0),-1)

    cv.imshow('lel',liveImage)



    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()