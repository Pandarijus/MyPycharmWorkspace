import cv2 as cv
import mediapipe as mp

vid = cv.VideoCapture(0)
#vid.set(3, 1280)
#vid.set(4, 720)

while True:
    isTrue, img = vid.read()
    fm = mp.solutions.face_mesh.FaceMesh()
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)#img to rgb
    height,width,_ = img.shape
    re = fm.process(img)

    if re.multi_face_landmarks:
        for landmarks in re.multi_face_landmarks:
            for l in landmarks.landmark:
                #p1 = landmarks.landmark[0]
                x = int(l.x * width)
                y = int(l.y * height)
                pos = (x, y)
                #print(pos)
                img = cv.circle(img, pos, 2, (255, 0, 0), -1)





    cv.imshow("hh", img)

    if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
        break

vid.release()
cv.destroyAllWindows()