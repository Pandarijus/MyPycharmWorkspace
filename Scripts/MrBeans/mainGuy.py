from gtts import gTTS as g
import pytesseract as pytes
import cv2 as cv
import os

pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
dirImg =  "Images"


imgs = os.listdir(dirImg)#get all images
index = 53
for i in imgs:
    img = cv.imread(dirImg+"/"+i)#open image
    imageText = pytes.image_to_string(img)#convert image to text
    g(imageText,lang='de').save(f"page{index}.mp3")
    index+=1

    print(imageText)
    print()

