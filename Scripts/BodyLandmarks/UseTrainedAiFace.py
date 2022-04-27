import pickle
import pandas as pd
import cv2 as cv
import mediapipe as mp
import numpy as np


#---------------
pickleRick = 'face.pkl'
#---------------


with open(pickleRick,'rb') as file:
    model = pickle.load(file)

vid = cv.VideoCapture(0)
screenSize = (1280,720)
vid.set(3, 1280)
vid.set(4, 720)
mpDraw = mp.solutions.drawing_utils
mpHol = mp.solutions.holistic

def drawPoint(img,l,size):
    x = int(l.x * screenSize[0])
    y = int(l.y * screenSize[1])
    pos = (x, y)
    return cv.circle(img, pos, size, (0, 0, 0), -1)

with mpHol.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)as hol:
    while True:
        isTrue, img = vid.read()
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.flip(img, 1)
        re = hol.process(img)
        #img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        lis = []

        # ---------------
        if re.face_landmarks:#face_landmarks
            for l in re.face_landmarks.landmark:#face_landmarks
                # ---------------
                img = drawPoint(img,l,2)
                lis += [l.x,l.y,l.z]

            data = pd.DataFrame([lis])
            aiGuess = model.predict(data)[0]


            img = cv.putText(img, aiGuess, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if "Hand" in aiGuess:
                img =np.uint8(np.absolute(cv.Laplacian(img, cv.CV_64F)))



        cv.imshow("hh", img)
        if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
            break


vid.release()
cv.destroyAllWindows()
