import cv2 as cv
import mediapipe as mp
import csv

def drawPoint(img,l):

    x = int(l.x * screenSize[0])
    y = int(l.y * screenSize[1])
    pos = (x, y)
    return cv.circle(img, pos, 2, (255, 0, 0), -1)

vid = cv.VideoCapture(0)
screenSize = (1280,720)
vid.set(3, 1280)
vid.set(4, 720)
mpDraw = mp.solutions.drawing_utils
mpHol = mp.solutions.holistic

#-----------------------------INPUT HERE----------------------------#
mood = "sad"
#-------------------------------------------------------------------#
with mpHol.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)as hol:
    while True:
        isTrue, img = vid.read()
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # img to rgb

        re = hol.process(img)



        lis = [mood]
        if re.face_landmarks:

            for l in re.face_landmarks.landmark:
                img = drawPoint(img,l)
                x = l.x
                y =l.y
                z =l.z
                lis.append(x)
                lis.append(y)
                lis.append(z)
            with open('mySaves.csv', 'a', newline='') as file:
                wr = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                #header = ['class','x1','y1','z1','...']
                #wr.writerow(header)
                wr.writerow(lis)

        cv.imshow("hh", img)
        if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
            break

vid.release()
cv.destroyAllWindows()
