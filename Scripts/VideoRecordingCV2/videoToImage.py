import cv2
import os

name = "Recording[6].mp4v"

def calcIndexThatHasNotBeenUsed():
  #print(os.listdir('Images'))
  listdirr = [int(l) for l in os.listdir('Images')]
  #print(listdirr)
  maxNamedDir = max(listdirr)
  return maxNamedDir+1

vidcap = cv2.VideoCapture(f"Videos/{name}")
success,image = vidcap.read()

if success:

  indexedDirName = calcIndexThatHasNotBeenUsed()
  os.mkdir(f"Images/{indexedDirName}")
  count = 0
  while success:
    cv2.imwrite(f"Images/{indexedDirName}/frame{count}.jpg", image)     # save frame as JPEG file
    success,image = vidcap.read()
    #print(f"Writing frame [{count}]")
    count += 1
else:
    print("sry no video under that name was found")