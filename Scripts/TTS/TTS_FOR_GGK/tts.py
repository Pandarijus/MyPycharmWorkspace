from gtts import gTTS as g
import pytesseract as pytes
import cv2 as cv
import os

pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
dirImg =  "images"
files = os.listdir(dirImg)#get all images

for file in files:
    img = cv.imread(dirImg+"/"+file)#open image
    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #cv.imshow("lol1", img)
    _,img = cv.threshold(img,210,255,cv.THRESH_BINARY)
    #cv.imshow("lol2",img)
    #cv.waitKey(0)
    imageText = pytes.image_to_string(img)#convert image to text
    g(imageText,lang='de').save(file[:-5]+"mp3")

    print(imageText)
    print()

