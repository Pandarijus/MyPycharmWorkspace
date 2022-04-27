import cv2 as cv

class FigureOutThreshold:

    def __int__(self):
        self.figureOut()

    def nothing(x):
        pass

    def figureOut(self):

        dirImg = "C:\\Users\\krott\\Pictures\\ForTTS\\ToConert"

        windowName = "Trackbars"
        windowImageName = "Threshold Image"
        cv.namedWindow(windowImageName)
        cv.namedWindow(windowName)

        cv.createTrackbar("mini", windowName, 13, 255, self.nothing)
        # cv.setTrackbarPos("mini",windowName,4)
        cv.createTrackbar("maxi", windowName, 41, 255, self.nothing)
        cv.setTrackbarMin("maxi", windowName, 2)
        startingImg = cv.imread("gg.png")
        vid = cv.VideoCapture(0)
        while True:
            _, image = vid.read()  # startingImg
            image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
            mini = cv.getTrackbarPos("mini", windowName)
            maxi = cv.getTrackbarPos("maxi", windowName)
            if maxi % 2 == 0:
                maxi = maxi + 1
            image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, maxi, mini)
            cv.imshow(windowImageName, image)
            if cv.waitKey(20) & 0xFF == ord('d'):
                cv.destroyAllWindows()
                break


f = FigureOutThreshold()
f.figureOut()