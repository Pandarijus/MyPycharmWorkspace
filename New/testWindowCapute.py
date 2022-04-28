import cv2 as cv
from WindowCapture import WindowCapture

winCap = WindowCapture('League of Legends')

while(True):
    img = winCap.get_screenshot()#gui.screenshot()
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break