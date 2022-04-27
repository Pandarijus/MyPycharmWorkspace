import numpy as np
import cv2 as cv
import random as rdm
#import pyautogui as py
from Scripts.Success_Ai import handTrackingModule

#def printMousePos():
 #   print(py.position())

def getEmptyImage(vector2Size):
    return np.zeros(vector2Size,dtype='uint8')
def getEmptywithImage(image):
    return np.zeros(image[:2],dtype='uint8')
def gausianBlur(image, kernalSize):
    return cv.GaussianBlur(image, (kernalSize, kernalSize), cv.BORDER_DEFAULT)
def res(image, scale=0.75):
    width = int (image.shape[1] * scale)
    height = int (image.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(image, dimensions, interpolation = cv.INTER_AREA)

#def resTo(image1,image2):
#    width = int(image2.shape[1] )
 #   height = int(image2.shape[0])
  #  dimensions = (width, height)
   # return cv.resize(image1,dimensions)


def showLive(image):
    name = 'Live'
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.imshow(name, image)
def show(image):
    cv.imshow(str(rdm.randint(0,100)), image)

def flip(image):
    return cv.flip(image,1)

def rnd(mi,ma):
   return rdm.randint(mi, ma)

#def getScreenshot():
 #   screenshot = py.screenshot()
   # screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
  #  return screenshot

#def takeScreenshot(fileName):
 #   screenshot = getScreenshot()
  #  cv.imwrite(fileName+'.png', screenshot)
def pressedKey(keyCode):
       return cv.waitKey(20) & 0xFF == ord(keyCode)

def getMarsImage():
    return cv.imread('../../Photos/old/MarsDialog.png')

def getsmallMarsImage():
    return res(getMarsImage(),.18)

def grayScale(image):
   return cv.cvtColor(image,cv.COLOR_BGR2GRAY)

def getPrepedImage():
   return grayScale(getsmallMarsImage())

def cutWithMask(image,mask):
   return cv.bitwise_and(image, image, mask=mask)

def laplacianEdgeDetection(image):
    return  np.uint8(np.absolute(cv.Laplacian(image, cv.CV_64F)))
def sobeEdgeDetection(image):
    return combine(cv.Sobel(image, cv.CV_64F,1,0),cv.Sobel(image, cv.CV_64F,0,1))

def combine(img1,img2):
    return cv.bitwise_or(img1,img2)

#def getMouseInfo():
   # return py.mouseInfo()

def getFingerDetector():
    return handTrackingModule.myHandDetector(maxHands=1,detectionConfidence=0.6)
def drawCircle(image,pos,color=(255, 0, 0),size = 20,thiccc = 2):
    img = cv.circle(image, pos, size,color, thiccc)
    return img


