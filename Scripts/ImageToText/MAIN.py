import pytesseract as pytes
import cv2 as cv
import os

pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
dirImg =  "Images"


imgs = os.listdir(dirImg)#get all images
index = 211
for i in imgs:
    img = cv.imread(dirImg+"/"+i)#open image
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    _, img = cv.threshold(img, 210, 255, cv.THRESH_BINARY)
    #cv.imshow("lul", img)
    imageText = pytes.image_to_string(img)#convert image to text
    index+=1

    print(imageText)
    print()