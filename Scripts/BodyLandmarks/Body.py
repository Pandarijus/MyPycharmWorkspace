import cv2 as cv
import mediapipe as mp
import socket

socketConnection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAdressPort = ("127.0.0.1",6968)



vid = cv.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 720)
mpDraw = mp.solutions.drawing_utils
mpHol = mp.solutions.holistic

with mpHol.Holistic(min_detection_confidence= 0.5,min_tracking_confidence= 0.5)as hol:
    while True:
        isTrue, img = vid.read()
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # img to rgb
        height, width, _ = img.shape

        re = hol.process(img)
        mpDraw.draw_landmarks(img,re.face_landmarks,mpHol.FACE_CONNECTIONS)
        mpDraw.draw_landmarks(img,re.pose_landmarks,mpHol.POSE_CONNECTIONS)
        mpDraw.draw_landmarks(img,re.left_hand_landmarks,mpHol.HAND_CONNECTIONS)
        mpDraw.draw_landmarks(img,re.right_hand_landmarks,mpHol.HAND_CONNECTIONS)

        data = ""
        for l in re.face_landmarks.landmark:
             x = int(l.x * width)
             y = int(l.y * height)
             pos = (x, y)
             data += str(x)+","+str(x)+";"
             # print(pos)
             img = cv.circle(img, pos, 2, (255, 0, 0), -1)

        #print(data)
        data = str.encode(data)
        socketConnection.sendto(data, serverAdressPort)

        #img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        #cv.imshow("hh", img)   ##UNHIDE THIS FOR IMAGE##
        if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
            break

vid.release()
cv.destroyAllWindows()
