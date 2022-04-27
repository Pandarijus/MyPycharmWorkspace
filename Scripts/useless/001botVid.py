import pyautogui as pg
from Scripts.Success import bigBrain as bs
import cv2 as cv

myVid = cv.VideoCapture(0)
while True:
    isTrue, frame = myVid.read()
    image = bs.res(frame, 2)
    bs.showLive(image)
    px = pg.position()[0]
    py = pg.position()[1]
    height =950
    width =950
    if width<px:
        px = width

    if height < py:
        px =height


    colorPixel = image[px, py]
    print(colorPixel)
    if bs.pressedKey('d'):  # inter >= 20:
        break



