import cv2 as cv

class FigureOutImage:

    def __int__(self):
        pass
        #self.figureOut()

    def nothing(x):
        pass

    def figureOut(self,startingImg):

        windowName = "Trackbars"
        windowImageName = "Threshold Image"
        cv.namedWindow(windowImageName)
        cv.namedWindow(windowName)

        cv.createTrackbar("mini", windowName, 30, 255, self.nothing)
        # cv.setTrackbarPos("mini",windowName,4)
        cv.createTrackbar("maxi", windowName, 59, 255, self.nothing)
        cv.setTrackbarMin("maxi", windowName, 2)
        while True:
            #image = cv.cvtColor(startingImg, cv.COLOR_RGB2GRAY)
            mini = cv.getTrackbarPos("mini", windowName)
            maxi = cv.getTrackbarPos("maxi", windowName)
            if maxi % 2 == 0:
                maxi = maxi + 1
            image = cv.adaptiveThreshold(startingImg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, maxi, mini)
            cv.imshow(windowImageName, image)
            if cv.waitKey(20) & 0xFF == ord('d'):
                cv.destroyAllWindows()
                return maxi,mini


#f = FigureOutThreshold()
#f.figureOut()