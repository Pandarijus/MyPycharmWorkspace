import regex as re
import pytesseract as pytes
import os

pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def removeEmptyLines(imageText):
    imageText = re.sub(r'^$\n', '', imageText, flags=re.MULTILINE)
def convertImageToText(image):
    return pytes.image_to_string(image)  # convert image to text
def getImagesOutOfDirectory(dir,folder):
    return os.listdir(dir + "\\"+ folder)  # get all images