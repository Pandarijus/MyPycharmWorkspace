import pyautogui as gui
from time import sleep
import win32gui

state = -2
champ = 'il'
banChamp = 'yasuo'

champs = {'sy':'sylas','il':'illaoi','ra':'rakan','py':'pyke','ya':'yasuo'}

def nextState():
    global state
    state += 1
    print('Switching to State: ' + str(state))
def clickOnImage(imgToFind, onlyOnce = False):
    global state
    pos = gui.locateOnScreen(imgToFind, confidence=0.7)
    if pos is not None:
        gui.click(pos)
        print("[",state, "]Clicked on:" + imgToFind)
        nextState()
    else:
        print("[",state, "]I didn't find: " + imgToFind)
        if not onlyOnce:
            clickOnImage(imgToFind)


def isNotInQueue():
    inQueue = gui.locateOnScreen('Queue.png', confidence=0.5)
    return inQueue is None
def canSee(name):
    return gui.locateOnScreen(name, confidence=0.8)

def clickAndCheckQueue():
    global state
    pos = gui.locateOnScreen('Accept.png', confidence=0.7)
    if pos is not None:
        gui.click(pos)
        print("Queue Accepted")
        sleep(15)
        if isNotInQueue():
            print("Queue was successful")
        else:
            print("Queue was canceled")

    else:  print("waiting in Queue")
    clickAndCheckQueue()


def startPlaying():
    clickOnImage('Play.png')
    clickOnImage('RankedFlex.png')
    clickOnImage('Confirm.png')
    clickOnImage('SelectLane.png')
    clickOnImage('TopLane.png')
    clickOnImage('SelectLane.png')
    clickOnImage('SupportLane.png')


while True:
    if state == -2:
        win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'League of Legends'))
        if canSee('Play.png'):
            startPlaying()
    elif state == -1:
        clickOnImage('FindMatch.png',True)
    elif state == 0:
        if isNotInQueue():
            clickOnImage('Play.png')
    elif state == 1:
        clickAndCheckQueue()
    elif state == 2:
        clickOnImage('Search.png')
    elif state == 3:
        gui.typewrite(champs[champ], interval=0.1)
    elif state == 4:
        clickOnImage(champs[champ]+'.png')
    elif state == 5:
        sleep(15)
        clickOnImage('Search.png')
    elif state == 6:
        gui.typewrite(banChamp, interval=0.1)
    elif state == 7:
        clickOnImage(banChamp+'.png')
        exit()

    sleep(2)
    nextState()