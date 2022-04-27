import cv2 as cv
from Scripts.Success import bigBrain as bscv
import Bigbrain as bs
vid = cv.VideoCapture(0)
vid.set(3,1280)
vid.set(4,720)

fourcc = cv.VideoWriter_fourcc(*'mp4v')
i = bs.calcIndexOfDir("Videos","Recording")
videoPath = f"Videos/Recording[{i}].mp4v"
myVideo = cv.VideoWriter(videoPath, fourcc, 30, (1280, 720))
while True:
    isTrue,liveImage = vid.read()
    liveImage = bscv.flip(liveImage)
    cv.imshow("hh",liveImage)
    myVideo.write(liveImage)

    if bscv.pressedKey('d'):#Quit    get key up
        break



vid.release()
cv.destroyAllWindows()
