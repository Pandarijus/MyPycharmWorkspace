import cv2 as cv
from WindowCapture import WindowCapture
from time import sleep
WindowCapture.list_window_names()
#win = WindowCapture('League of Legends')#League of Legends (TM) Client
sleep(10)
win = WindowCapture()#League of Legends (TM) Client     'League of Legends'

while(True):
    img = win.get_screenshot()#gui.screenshot()
    #img = cv.contur(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break