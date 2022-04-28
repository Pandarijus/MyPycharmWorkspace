import pyautogui as gui
import numpy as np
import cv2 as cv
import time


loopTime = 0
while(True):
    img = gui.screenshot()
    img = np.array(img)
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #img = cv.Canny(img, 100, 200)
    timeDiff = time.time() - loopTime
    loopTime = time.time()

    print(1/timeDiff)
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break