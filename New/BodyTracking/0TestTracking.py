import cv2 as cv
import mediapipe as mp



#-----------------------------INPUT HERE----------------------------#
inputs = [1,1,1,1]
faceTracking = inputs[0]
bodyTracking = inputs[1]
leftHandTracking = inputs[2]
rightHandTracking = inputs[3]

#-------------------------------------------------------------------#



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

        if faceTracking:
            mpDraw.draw_landmarks(img,re.face_landmarks,mpHol.FACE_CONNECTIONS)
        if bodyTracking:
            mpDraw.draw_landmarks(img, re.pose_landmarks, mpHol.POSE_CONNECTIONS)
        if leftHandTracking:
            mpDraw.draw_landmarks(img, re.left_hand_landmarks, mpHol.HAND_CONNECTIONS)
        if rightHandTracking:
            mpDraw.draw_landmarks(img, re.right_hand_landmarks, mpHol.HAND_CONNECTIONS)

        # for l in re.face_landmarks.landmark:
        #     x = int(l.x * width)
        #     y = int(l.y * height)
        #     pos = (x, y)
        #     # print(pos)
        #     img = cv.circle(img, pos, 2, (255, 0, 0), -1)

        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imshow("You", img)
        if cv.waitKey(20) != -1:  # Quit  0xFF == ord('d')
            break

vid.release()
cv.destroyAllWindows()
