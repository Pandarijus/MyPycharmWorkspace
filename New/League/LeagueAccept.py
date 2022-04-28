import pyautogui as gui
from time import sleep
#import New.WindowCapture as wc
# wc.screenshot()
#print(gui.locateOnScreen('Accept.png', confidence=0.7))
#gui.locateOnScreen('FindMatch.png')
state = 0
while True:

    if state == 0:
        imgToFind = 'FindMatch.png'
        sleep(1)
    elif state == 1:
        imgToFind = 'Accept.png'
        sleep(8)
    elif state == 2:
        imgToFind = 'Search.png'
        sleep(1)


    pos = gui.locateOnScreen(imgToFind, confidence=0.7)
    if pos is not None:
        gui.click(pos)
        print("Clicked")
        state+=1
    else:
        print("Not found")





