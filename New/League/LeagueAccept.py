import pyautogui as gui
from time import sleep

state = 0
champ = 'il'
banChamp = 'yasuo'



champs = {'sy':'sylas','il':'illaoi','ra':'rakan','py':'pyke','ya':'yasuo'}
def clickOnImage(imgToFind):
    global state
    pos = gui.locateOnScreen(imgToFind, confidence=0.7)
    if pos is not None:
        gui.click(pos)
        print("Clicked")
        state += 1
    else:
        print( "[",state, "]")


def clickOnQueueAndCheckIfQueueIsAccepted():
    global state
    pos = gui.locateOnScreen('Accept.png', confidence=0.7)
    if pos is not None:
        gui.click(pos)
        print("Queue Accepted")
        sleep(10)
        if gui.locateOnScreen('Queue.png', confidence=0.7) is None:
            state += 1
            print("Queue was successful")
        else:
            print("Queue was canceled")
    else:  print("waiting in Queue")




def clickOnImage1(imgToFind):
    sleep(0.5)
    pos = gui.locateOnScreen(imgToFind, confidence=0.9)
    if pos is not None:
        gui.click(pos)
        print("Clicked")
    else:
        print("Not found: " + imgToFind)
        clickOnImage1(imgToFind)


def startPlaying():
    clickOnImage1('Play.png')
    clickOnImage1('RankedFlex.png')
    clickOnImage1('Confirm.png')
    clickOnImage1('SelectLane.png')
    clickOnImage1('TopLane.png')
    clickOnImage1('SelectLane.png')
    clickOnImage1('SupportLane.png')
    clickOnImage1('FindMatch.png')





while True:
    if state == -1:
        startPlaying()
    elif state == 0:
        clickOnImage('FindMatch.png')
    elif state == 1:
        clickOnQueueAndCheckIfQueueIsAccepted()
    elif state == 2:
        clickOnImage('Search.png')
    elif state == 3:
        gui.typewrite(champs[champ], interval=0.1)
        state += 1
    elif state == 4:
        clickOnImage(champs[champ]+'.png')
    elif state == 5:
        sleep(15)
        clickOnImage('Search.png')
    elif state == 6:
        gui.typewrite(banChamp, interval=0.1)
        state += 1
    elif state == 7:
        clickOnImage(banChamp+'.png')
        exit()

    sleep(2)


#class Champion:






