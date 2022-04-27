import cv2 as cv
import numpy as np
import bigBrain as bs

mars = bs.getMarsImage()

#lower = np.array([0,0,0]) #rgb 000=black
#upper = np.array([130,130,130])

lower = np.array([110,110,110]) #rgb =white   picks up lots of white = [180,180,180]
upper = np.array([255,255,255])



def nothing():
    pass

windowName = "Trackbars"
cv.namedWindow(windowName)

cv.createTrackbar("r1", windowName, 0, 255, nothing)
cv.createTrackbar("g1", windowName, 0, 255, nothing)
cv.createTrackbar("b1", windowName, 0, 255, nothing)
cv.createTrackbar("r2", windowName, 0, 255, nothing)
cv.createTrackbar("g2", windowName, 0, 255, nothing)
cv.createTrackbar("b2", windowName, 0, 255, nothing)

cv.resizeWindow(windowName,500,500)



vid = cv.VideoCapture(0)

photoCounter = 0
while True:
    succsess, liveImage = vid.read()
    liveImage = bs.flip(liveImage)
    image = cv.cvtColor(liveImage, cv.COLOR_BGR2RGB)

    r1 = cv.getTrackbarPos("r1", windowName)
    g1 = cv.getTrackbarPos("g1", windowName)
    b1 = cv.getTrackbarPos("b1", windowName)
    lower = np.array([r1 , g1, b1])
    r2 = cv.getTrackbarPos("r2", windowName)
    g2 = cv.getTrackbarPos("g2", windowName)
    b2 = cv.getTrackbarPos("b2", windowName)
    upper = np.array([r2 , g2, b2])

    mask = cv.inRange(image,lower,upper)



    
    invertedMask = cv.bitwise_not(mask)
    contures, hyr = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(contures)!=0:
        for cont in contures:
            if cv.contourArea(cont)>500:
                x,y,w,h = cv.boundingRect(cont)
                cv.rectangle(liveImage, (x, y), (x + w, y + h), (0, 0, 255), 3)

    bs.showLive(liveImage)
    cv.imshow('mask',mask)
    cv.imshow('mask2', invertedMask)

    #croppedMars = mars[0:image.shape[1], 0:image.shape[0]]

    #empty = np.zeros(liveImage[:2],dtype='uint8')
    #empty = bs.getEmptyImage(liveImage[:2])
    #empty = cv.circle(empty,(50,50),50,255,-1)
    #greenScreen = bs.cutWithMask(empty, liveImage)
    #add = cv.bitwise_or(greenScreen, liveImage)
    #cv.imshow('temp', greenScreen)

    #print(image[:2])

    #bs.getMouseInfo()


    if bs.pressedKey('p'):
        cv.imwrite(f"MyFilterRun({1})andCounter({photoCounter}).jpg", invertedMask)
        photoCounter+=1

    if bs.pressedKey('d'):
        break