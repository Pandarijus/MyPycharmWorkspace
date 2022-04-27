import cv2 as cv
import pytesseract as pytes


pytes.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

inp = input("Write The Name Of The Image You Want To Turn Into Texts:\n")#"Spanish.jpg"
imagePath = "Images\\"+inp
image = cv.imread(imagePath)

imageText = pytes.image_to_string(image)


imageText  = "\n".join([ll.rstrip() for ll in imageText.splitlines() if ll.strip()])#filter whitespaces

#print(imageText)
file = open("Texts\\"+inp[:-4]+".txt", "w+")
file.write(imageText)
print("Wrote "+inp+" to path "+imagePath)


