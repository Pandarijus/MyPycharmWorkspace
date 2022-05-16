import pickle
import pandas as pd
import cv2 as cv
import mediapipe as mp
import numpy as np



#---------------
pickleRick = 'abend.pkl'
#---------------


with open(pickleRick,'rb') as file:
    model = pickle.load(file)

vid = cv.VideoCapture(0)
screenSize = (1280,720)
vid.set(3, 1280)
vid.set(4, 720)
mpDraw = mp.solutions.drawing_utils
mpHol = mp.solutions.holistic
laplace = False;

def drawPoint(img,l,size):
    x = int(l.x * screenSize[0])
    y = int(l.y * screenSize[1])
    pos = (x, y)
    return cv.circle(img, pos, size, (0, 0, 0), -1)

def showContureColor(image,color):
    contures,hy = cv.findContours(image,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    colorImage = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
    cv.drawContours(colorImage,contures,-1,color,1)
    return colorImage

def canny(img):
    color = (0,0,255)
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
    img = cv.Canny(img, 15, 50)#(80,90) is stable but low detail     (15,50)  hier ist die edge min max difference
    return showContureColor(img, color)


with mpHol.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)as hol:
    while True:
        isTrue, img = vid.read()
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        #img = cv.flip(img, 1)
        re = hol.process(img)
        #img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        lis = []


        # ---------------
        if re.right_hand_landmarks:#face_landmarks
            for l in re.right_hand_landmarks.landmark:#face_landmarks
                # ---------------
                img = drawPoint(img,l,10)
                lis += [l.x,l.y,l.z]

            data = pd.DataFrame([lis])
            aiGuess = model.predict(data)[0]


            img = cv.putText(img, aiGuess, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            laplace = "Hand" in aiGuess




        if not laplace:
            if re.face_landmarks:  # face_landmarks
                for l in re.face_landmarks.landmark:  # face_landmarks
                    # ---------------
                    img = drawPoint(img, l, 3)
                    lis += [l.x, l.y, l.z]
            #img = cv.putText("bye", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            #img = np.uint8(np.absolute(cv.Laplacian(img, cv.CV_64F)))
        else:

            #img = cv.putText("hi", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            #img = cv.bitwise_or(cv.Sobel(img, cv.CV_64F,1,0),cv.Sobel(img, cv.CV_64F,0,1))
            pass
            #img = canny(img)


#        img = cv.flip(img, 1)
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imshow("hh", img)
        if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
            break


vid.release()
cv.destroyAllWindows()
