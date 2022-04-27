from Scripts.Success import bigBrain as bs
import cv2 as cv

#def main():

vid = cv.VideoCapture(0)
    ###################### finger
    #handDetector = handTrackingModule.myHandDetector(maxHands=1)
fingerManager = bs.getFingerDetector()
    ###################### finger
while True:
    isTrue, liveImage = vid.read()
    liveImage = cv.flip(liveImage, 1)




###################### finger
    liveImage = fingerManager.drawHands(liveImage)
    fingerList = fingerManager.getFingerPosList(liveImage)
    if len(fingerList) != 0:
        indexFinger =fingerList[8]
        liveImage = cv.circle(liveImage, (indexFinger[1], indexFinger[2]), 20, (255, 0, 0), 2)
        print(indexFinger)
###################### finger




        bs.showLive(liveImage)
        if bs.pressedKey('d'):
            vid.release()
            cv.destroyAllWindows()
            break


#if __name__ == "__main__":
main()