import cv2 as cv
import pytesseract as pytes

def nothing(x):
    pass
pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

windowName = "Trackbars"
windowImageName = "Threshold Image"
cv.namedWindow(windowImageName)
cv.namedWindow(windowName)

cv.createTrackbar("mini",windowName,0,255,nothing)
cv.setTrackbarPos("mini",windowName,170)
#cv.createTrackbar("maxi",windowName,0,255,nothing)
startingImg = cv.imread("gg.png")
#imgSize = startingImg.shape


while True:
    #cv.resizeWindow(windowImageName, int(imgSize[1]/2),int(imgSize[0]/2))
    cv.resizeWindow(windowName, 400,3)
    image = startingImg
    #cv.imshow("input Image",image)
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    #cv.imshow("black and white Image", image)
    mini = cv.getTrackbarPos("mini",windowName)
    maxi = 255#cv.getTrackbarPos("maxi",windowName)
    _, image = cv.threshold(image,mini,maxi, cv.THRESH_BINARY)#170,255
    #image = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,81,4)
    cv.imshow(windowImageName, image)
    if cv.waitKey(20) & 0xFF == ord('d'):
        cv.destroyAllWindows()
        break
#    imageText = pytes.image_to_string(image)  # convert image to text
#    print(imageText)