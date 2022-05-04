import pyautogui as gui
from time import sleep
import win32gui

state = -2
champ = 'no'
banChamp = 'yasuo'

champs = {'sy':'sylas','il':'illaoi','ra':'rakan','py':'pyke','ya':'yasuo','no':'nocturne'}

def wait():
    sleep(0.5)
def getImagePos(imgName):
    return gui.locateOnScreen(imgName, confidence=0.8)

def clickOnImage(imgToFind, onlyOnce = False):

    pos = getImagePos(imgToFind)
    if pos is not None:
        gui.click(pos)
        print("Clicked on:" + imgToFind)
    else:
        print("I didn't find: " + imgToFind)
        if onlyOnce is False:
      #      print("waiting")
            sleep(1)
      #      print("loop")
            clickOnImage(imgToFind)


def isNotInQueue():
    inQueue = getImagePos('Queue.png')#0.5
    return inQueue is None

def canSee(name):
    return getImagePos(name)#0.8

def clickAndCheckQueue():
    global state
    pos =getImagePos('Accept.png')
    if pos is not None:
        gui.click(pos)
        print("Queue Accepted")
        sleep(15)
        if isNotInQueue():
            print("Queue was successful")
        else:
            print("Queue was canceled")
            wait()
            clickAndCheckQueue()

    else:
        print("waiting in Queue")
        wait()
        clickAndCheckQueue()


def startPlaying():
    clickOnImage('Play.png')
    clickOnImage('RankedFlex.png')
    clickOnImage('Confirm.png')
    clickOnImage('SelectLane.png')
    clickOnImage('TopLane.png')
    clickOnImage('SelectLane.png')
    clickOnImage('SupportLane.png')

def keyboardWrite(text):
    gui.typewrite(text, interval=0.1)

def yeeting():
    win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'League of Legends'))
    wait()
    if canSee('Play.png'):
        startPlaying()
    else:
        print("Can't see Play")
    clickOnImage('FindMatch.png',True)
    if isNotInQueue():
        clickOnImage('FindMach.png')
    clickAndCheckQueue()
    clickOnImage('Search.png')
    keyboardWrite(champs[champ])
    clickOnImage(champs[champ]+'.png')
    sleep(15)
    clickOnImage('Search.png')
    keyboardWrite(banChamp)
    clickOnImage(banChamp+'.png')
    exit()



if __name__ == '__main__':
    yeeting()
