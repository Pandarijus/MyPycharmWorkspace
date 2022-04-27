import pytesseract as pytes
import cv2 as cv
import os

pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def imageToText(image):
    cv.imwrite("gg.png", image)
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    image = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,133,15)
    cv.imwrite("gg1.png",image)
    imageText = pytes.image_to_string(image)  # convert image to text

    print(imageText)



oneImage = True#False if input("One image [0]  Images out of folder [1]")=='1' else True

if oneImage:
    img = None
    vid = cv.VideoCapture(0)
    vid.set(3, 1280)
    vid.set(4, 720)
    flip = False

    while True:
        isTrue, liveImage = vid.read()
        if flip:
            flipped = cv.flip(liveImage, 1)
        else:
            flipped = liveImage

        cv.imshow("hh", flipped)

        if cv.waitKey(20) & 0xFF == ord('f'):
            flip = not flip

        if cv.waitKey(20) & 0xFF == ord('d'):  # Quit


            img = liveImage
            #imageToText(img)
            break

#    print("hi?")
    imageToText(img)
    vid.release()
    cv.destroyAllWindows()

else:
    dirImg =  "Images"
    imgs = os.listdir(dirImg)#get all images
    #index = 1
    for i in imgs:
        #index += 1
        img = cv.imread(dirImg + "/" + i)  # open image
        imageToText(img)