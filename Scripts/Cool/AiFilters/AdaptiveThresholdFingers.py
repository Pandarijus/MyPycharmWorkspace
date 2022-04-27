from Scripts.Success_Ai import bigBrain as bs
import cv2 as cv
import mediapipe as mp

vid = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1)

mpDraw = mp.solutions.drawing_utils

maxMagnitude = 30

mini = 13
maxi = 31

while True:
    isTrue,liveImage = vid.read()
    startImg = liveImage
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
                    liveImage = cv.circle(liveImage,(cx,cy),13,(0,0,0),-1)#dark green = (50,100,50)
                    thumb =(cx,cy)
                if id == 8:
                    liveImage = cv.circle(liveImage, (cx, cy), 13, (0, 0, 0), -1)
                    indexFinger =(cx,cy)
            #print("thumb:"+str(thumb))
            #print("indexFinger:"+str(indexFinger))
            dir = (abs(thumb[0])-abs(indexFinger[0]),abs(thumb[1])-abs(indexFinger[1]))

            #print("dir"+str(dir))

            magnitudeFake = abs(dir[0])+abs(dir[1])
            magnitudeFake = abs(magnitudeFake)

            # mini = int(13*(magnitudeFake*0.001))
            # liveImage = cv.adaptiveThreshold(liveImage,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,59)
            mini = 13
            maxi = int(magnitudeFake/2)+1
            maxi = max(maxi,3)
            if maxi % 2 == 0:
                maxi = maxi + 1

            #liveImage = cv.putText(liveImage, str(magnitudeFake), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
            liveImage = cv.line(liveImage, thumb, indexFinger, (55, 50, 255), 2)
            #mpDraw.draw_landmarks(liveImage, handLandmark,mpHands.HAND_CONNECTIONS)
    liveImage = cv.cvtColor(liveImage, cv.COLOR_RGB2GRAY)
    liveImage = cv.adaptiveThreshold(liveImage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, maxi, mini)

    bs.showLive(liveImage)
    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()