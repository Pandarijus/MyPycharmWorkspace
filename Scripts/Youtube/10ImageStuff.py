import os
from Scripts.Success import bigBrain as bs
import cv2 as cv


path = r"C:\Users\krott\Pictures\PicsForPython"

folderList = os.listdir(path)
imageList = []
print(folderList)
if len(folderList) != 0:
    for xImageName in folderList:
        image = cv.imread(f'{path}/{xImageName}')
        imageList.append(image)


if imageList != 0:
    img = imageList[1]
    header = imageList[0]
    img[0:240,0:1920] = header[0:240,0:1920]#header
    bs.show(img)

cv.waitKey(0)