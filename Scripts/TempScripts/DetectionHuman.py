import cv2 as cv
from Scripts.Success import bigBrain as bscv

vid = cv.VideoCapture(0)
vid.set(3,1280)
vid.set(4,720)




while True:
    isTrue,img = vid.read()
    img = bscv.flip(img)
    #img = cv.findContours(img,cv.RETR_CCOMP,cv.CONTOURS_MATCH_I2)#cvStartFindContours_Impl CV_RETR_FLOODFILL
    cv.imshow("cam", img)

    if bscv.pressedKey('d'):#Quit    get key up
        break









#vid.release()
cv.destroyAllWindows()