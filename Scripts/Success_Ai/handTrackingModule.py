import cv2 as cv
import mediapipe as mp

class myHandDetector():
    def __init__(self,mode = False,maxHands =1,detectionConfidence = 0.5,trackingConfidence=0.5):
        self.mode = mode
        self.maxHands =maxHands
        self.detectionConfidence =detectionConfidence
        self.trackingConfidence = trackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionConfidence,self.trackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils



    def setUpHandPoints(self,image):
        imageRGB = cv.cvtColor(image, cv.COLOR_BGRA2RGB)
        self.results = self.hands.process(imageRGB)

    def checkLeftRight(self):
        print('')
        #TODO find if hand is left or right


    def drawHands(self, image, draw = True):
        self.setUpHandPoints(image)
        if self.results.multi_hand_landmarks:
            for handLandmark in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLandmark, self.mpHands.HAND_CONNECTIONS)
        return image

    def getFingerPosList(self, image, handIndex = 0):
        self.setUpHandPoints(image)
        lmList = []
        success = False
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handIndex]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([cx, cy])
                success = True
        return success,lmList

    def getFinger(self,image,fingerIndex):
        pos = (0,0)
        success,list =self.getFingerPosList(image)
        if success:
            pos = list[fingerIndex]
        return success, pos

    def getFingerTips(self,image):
        success, list = self.getFingerPosList(image)
        fingerTips = []
        if success:
            for x in range(4,21,4):
                fingerTips.append(list[x])

        return success,fingerTips

    def getFingerBoolUpList(self,image):
        success, fingers = self.getFingerPosList(image)
        dirBools = []
        if success:
            if fingers[4][0] > fingers[3][0]:
                dirBools.append(0)
            else:
                dirBools.append(1)
            for x in range(8, 21, 4):

                if fingers[x][1] > fingers[x - 2][1]:
                    dirBools.append(0)
                else:
                    dirBools.append(1)

            # print(dirBools)
        return success,dirBools
