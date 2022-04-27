import cv2 as cv
import pytesseract as pytes

def nothing(x):
    pass
pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

windowName = "Trackbars"
windowImageName = "Threshold Image"
cv.namedWindow(windowImageName)
cv.namedWindow(windowName)

cv.createTrackbar("mini",windowName,13,255,nothing)
#cv.setTrackbarPos("mini",windowName,4)
cv.createTrackbar("maxi",windowName,41,255,nothing)
cv.setTrackbarMin("maxi",windowName,2)
startingImg = cv.imread("gg.png")
vid = cv.VideoCapture(0)


while True:
    #cv.resizeWindow(windowName, 400,80)
    _,image = vid.read()#startingImg
    #cv.imshow("input Image",image)
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    #cv.imshow("black and white Image", image)
    mini = cv.getTrackbarPos("mini",windowName)
    maxi = cv.getTrackbarPos("maxi",windowName)
    if maxi % 2 == 0:
        maxi = maxi+1
    image = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,maxi,mini)
    cv.imshow(windowImageName, image)
    if cv.waitKey(20) & 0xFF == ord('d'):
        cv.destroyAllWindows()
        break
#    imageText = pytes.image_to_string(image)  # convert image to text
#    print(imageText)