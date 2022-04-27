from Scripts.Success import bigBrain as bs
import cv2 as cv
import mediapipe as mp

vid = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1)

mpDraw = mp.solutions.drawing_utils

while True:
    isTrue,liveImage = vid.read()
    liveImage = cv.flip(liveImage,1)
    imageRGB = cv.cvtColor(liveImage,cv.COLOR_BGRA2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handLandmark.landmark):
                h, w, c = liveImage.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id%4 == 0 and id != 0:
                    liveImage = cv.circle(liveImage,(cx,cy),20,(255,0,0),2)#dark green = (50,100,50)
            #mpDraw.draw_landmarks(liveImage, handLandmark,mpHands.HAND_CONNECTIONS)


    bs.showLive(liveImage)
    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()