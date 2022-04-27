from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2 as cv
from Scripts.Success import bigBrain as bscv
import Bigbrain as bs

vid = cv.VideoCapture(0)
vid.set(3,1280)
vid.set(4,720)

fourcc = cv.VideoWriter_fourcc(*'mp4v')
i = bs.calcIndexOfDir("Videos","Recording")
videoPath = f"Videos/Recording[{i}].mp4v"
myVideo = cv.VideoWriter(videoPath, fourcc, 10, (1280, 720))

seg = SelfiSegmentation(0)
rec = False
while True:
    isTrue,liveImage = vid.read()
    liveImage = bscv.flip(liveImage)

    s = seg.removeBG(liveImage,(4,244,4))
    #s = bscv.sobeEdgeDetection(s)

    if bscv.pressedKey('r'):
        rec = not rec
    if rec:
        myVideo.write(s)
        #myVideo.write(s.astype('uint8') * 255)
        newS = cv.putText(s, 'Recording', (20, 80), cv.FONT_HERSHEY_SIMPLEX, 3, (0,0 , 0), 10, cv.LINE_AA)

        cv.imshow("cam", newS)
    else:
        cv.imshow("cam", s)

    #cv.imwrite("ts.png",s)

    if bscv.pressedKey('d'):#Quit    get key up
        break









#vid.release()
cv.destroyAllWindows()