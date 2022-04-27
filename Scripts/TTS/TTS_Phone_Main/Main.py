import cv2 as cv

from FigureOutImage import FigureOutImage
from TTS import TTS
import BigbrainTTS as b



f = FigureOutImage()
tts = TTS()
dirImg =  "C:\\Users\\krott\\Pictures\\ForTTS"
checkThresh = False

imgs = b.getImagesOutOfDirectory(dirImg,"ToConert")
#index = 1
for imageName in imgs:
    image = cv.imread(dirImg+"\\ToConert" + "\\" + imageName)  # open image
    print(imageName)
    image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    if checkThresh:
        maxi,mini = f.figureOut(image)
        image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, maxi, mini)
    else:
        image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 133, 15)

    cv.imwrite(dirImg +"\\Debug"+"\\" + imageName, image)


    imageText = b.convertImageToText(image)


    #imageText = ''.join(filter(str.isalnum, imageText))
    #imageText = imageText.strip()

    imageText = [t for t in imageText if ((48 <= ord(t)  < 250)or ord(t) == 10 or ord(t) == 32or ord(t) == 44 or ord(t) == 46or ord(t) == 40 or ord(t) == 41 or ord(t) == 37 )and ord(t) != 126and ord(t) != 124 and ord(t) != 95]
    imageText = b.removeEmptyLines(imageText)

    imageText = ''.join(imageText)

    for t in imageText:
        print(t+" = "+str(ord(t)))

    print(imageText)
    TTS.convert(imageText,dirImg+"\\OutputSpeech\\"+imageName[:-5]+".mp3")
    l = open(dirImg+"\\OutputText\\"+imageName[:-5]+".txt","w")#,encode='UTF-8'
    l.write(imageText)
    l.close()