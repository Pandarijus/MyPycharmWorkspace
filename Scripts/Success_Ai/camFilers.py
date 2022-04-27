import cv2 as cv
from Scripts.Success import bigBrain as bs
import os
vid = cv.VideoCapture(0)
vid.set(3,1920);
vid.set(4, 1080);

framesForVideo =[]
handManager = bs.getFingerDetector()

shouldRecord = False
shouldRecordFromStart = False


def showContureColor(image,color):
    contures,hy = cv.findContours(image,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    colorImage = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
    cv.drawContours(colorImage,contures,-1,color,1)
    return colorImage

def canny(image):
    color = (0,0,255)
    img = bs.grayScale(image)
    img = bs.gausianBlur(img, 3)
    img = cv.Canny(img, 15, 50)#(80,90) is stable but low detail     (15,50)  hier ist die edge min max difference
    return showContureColor(img, color)

def lapi(image):
   return bs.laplacianEdgeDetection(image)

def sobre(image):
    return bs.sobeEdgeDetection(image)

def selectFilter(name):
    print(name)
    if name == 'canny':
        image =  canny(liveImage)
    elif name == 'lapi':
        image = lapi(liveImage)
    elif name == 'sobre':
        image = sobre(liveImage)
    elif name == 'hand':
        image = handManager.drawHands(liveImage)
        succsess,fingerPos = handManager.getFinger(liveImage,8)
        if succsess:
            image = bs.drawCircle(image,fingerPos)
    else:
        image = liveImage
        name = 'NO FILTER SELECTED'

    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.imshow(name, image)
    return image

def getVideoPath():
    counter = 0
    path = r'C:\Users\krott\Pictures\pythonFilterTests\FilterVideos'
    while 1:
        name = f'new{counter}.avi'
        checkList = os.listdir(path)
        if checkList.__contains__(name):
            counter = counter+1
        else:
            realPath = os.path.join(path, name)
            #print(realPath)
            return realPath



photoCounter = 0
stop = False
isBreak = False

inp = input("[c]anny [l]api [s]obre [h]and")
names  = ["canny", "lapi", "sobre","hand"]
for n in names:
    if n[0] == inp[0]:
        filterName = n

if not filterName:
    filterName = names[-1]

while True:
    isTrue,liveImage = vid.read()

    liveImage = bs.flip(liveImage)


    photo = selectFilter(filterName)# canny lapi sobre hand



    if bs.pressedKey('p'):#photo
        cv.imwrite(f"MyFilterRun({2})andCounter({photoCounter}).jpg", photo)
        cv.destroyAllWindows()
        photoCounter += 1

    if not shouldRecordFromStart:
        if bs.pressedKey('v'):#video
            if not shouldRecord:
                shouldRecord = True
                stop = False
            else:
                shouldRecord = False

    if shouldRecord or shouldRecordFromStart:
        photo = bs.getScreenshot()
        if not stop:
            height, width, layers = photo.shape
            fourcc = cv.VideoWriter_fourcc(*'mp4v')
            videoPath = getVideoPath()
            myVideo = cv.VideoWriter(videoPath, fourcc, 20, (width, height))
            stop = True
        myVideo.write(photo)

    if bs.pressedKey('d'):#Quit    get key up
        break



vid.release()
cv.destroyAllWindows()