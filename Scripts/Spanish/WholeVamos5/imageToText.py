import cv2 as cv
import pytesseract as pytes
import os


pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

for img in os.listdir("images"):
    imagePath = "images\\"+img
    image = cv.imread(imagePath)
    image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    imageText = pytes.image_to_string(image)
    imageText  = "\n".join([ll.rstrip() for ll in imageText.splitlines() if ll.strip()])#filter whitespaces

    file = open("images\\"+img[:-5]+".txt", "w+")
    file.write(imageText)
    print("Wrote "+img+" to path "+imagePath)