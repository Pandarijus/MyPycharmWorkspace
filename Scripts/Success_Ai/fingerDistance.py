from Scripts.Success import bigBrain as bs
import cv2 as cv
import mediapipe as mp

vid = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1)

mpDraw = mp.solutions.drawing_utils

maxMagnitude = 30

while True:
    isTrue,liveImage = vid.read()
    liveImage = cv.flip(liveImage,1)
    imageRGB = cv.cvtColor(liveImage,cv.COLOR_BGRA2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            thumb = (0,0)
            indexFinger= (0,0)
            for id,lm in enumerate(handLandmark.landmark):
                h, w, c = liveImage.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4: #id%4 == 0 and id != 0:
                    liveImage = cv.circle(liveImage,(cx,cy),20,(255,0,0),2)#dark green = (50,100,50)
                    thumb =(cx,cy)
                if id == 8:
                    liveImage = cv.circle(liveImage, (cx, cy), 20, (255, 50, 0), 2)
                    indexFinger =(cx,cy)
            #print("thumb:"+str(thumb))
            #print("indexFinger:"+str(indexFinger))
            dir = (abs(thumb[0])-abs(indexFinger[0]),abs(thumb[1])-abs(indexFinger[1]))

            #print("dir"+str(dir))

            magnitudeFake = abs(dir[0])+abs(dir[1])
            magnitudeFake = abs(magnitudeFake)
            print(magnitudeFake)


            if magnitudeFake <= 100:
                liveImage = cv.putText(liveImage, 'close',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,(255, 255, 255), 2)
                liveImage = cv.line(liveImage, thumb, indexFinger, (55, 50, 255), 2)
                liveImage = bs.drawCircle(liveImage,
                                          ((thumb[0] + indexFinger[0]) // 2, (thumb[1] + indexFinger[1]) // 2),(100,100,255), size=10,
                                          thiccc=-1)
            else:
                liveImage = cv.putText(liveImage, 'far', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (230, 255, 255), 2)
                liveImage = cv.line(liveImage, thumb, indexFinger, (205, 200, 255), 2)
                liveImage = bs.drawCircle(liveImage,
                                          ((thumb[0] + indexFinger[0]) // 2, (thumb[1] + indexFinger[1]) // 2), size=10,
                                          thiccc=-1)
            #mpDraw.draw_landmarks(liveImage, handLandmark,mpHands.HAND_CONNECTIONS)


    bs.showLive(liveImage)
    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()