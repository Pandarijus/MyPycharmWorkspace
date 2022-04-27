import cv2 as cv
from Scripts.Success import bigBrain as bs

def showContureColor(image,color):
    contures,hy = cv.findContours(image,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    colorImage = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
    cv.drawContours(colorImage,contures,-1,color,1)
    return colorImage

def cannye(image):
    color = (0,0,255)
    img = bs.grayScale(image)
    img = bs.gausianBlur(img, 3)
    img = cv.Canny(img, 15, 50)#(80,90) is stable but low detail     (15,50)  hier ist die edge min max difference
    return showContureColor(img, color)

SCREEN_SIZE = (480, 640)
COLOR = (255,255,255)
isCanny = False
isDraw = False
vid = cv.VideoCapture(0)
#vid.set(4,720);
#vid.set(3, 1280);
mask = bs.getEmptyImage(SCREEN_SIZE)

detector = bs.getFingerDetector()
while True:
    isTrue,liveImage = vid.read()

    liveImage = cv.flip(liveImage,1)
    canny = cannye(liveImage)

    liveImage = detector.drawHands(liveImage)

    success, position = detector.getFinger(liveImage, 8)
    if success:
        liveImage =  bs.drawCircle(liveImage, position, (0,0,255), 20, -1)
        mask = bs.drawCircle(mask, position, COLOR, 50, -1)#50 works well



    #liveImage = cv.bitwise_and(liveImage, liveImage, None, mask)
    #liveImage = cv.bitwise_and(canny, canny, None, mask)




    if bs.pressedKey('w'):
        isDraw = not isDraw
        if isDraw:
            COLOR = (0,0,0)
        else:
            COLOR = (255,255,255)


    if bs.pressedKey('e'):
        isCanny = not isCanny

    if isCanny:
        liveImage = cv.bitwise_and(canny, canny, None, mask)
    else:
        liveImage = cv.bitwise_and(liveImage, liveImage, None, mask)

    bs.showLive(liveImage)

    if bs.pressedKey('r'):
        mask = bs.getEmptyImage(SCREEN_SIZE)
    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()


#TODO how to radier ein Image istead black