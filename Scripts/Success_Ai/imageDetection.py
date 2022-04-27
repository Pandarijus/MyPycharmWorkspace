import cv2 as cv
from Scripts.Success import bigBrain as bs
import os


def getDesArray(imageArray):
    desList = []
    orb = cv.ORB_create(nfeatures=1000)
    for image in imageArray:
        kp, des = orb.detectAndCompute(image, None)
        desList.append(des)
    return desList


def getId(img, desArray,threshhold,features):
    orb = cv.ORB_create(nfeatures=features)
    bf = cv.BFMatcher()
    matchList = []
    finalValue = -1

    kp2, des2 = orb.detectAndCompute(img, None)

    try:
        for des in desArray:
            good = []
            matches = bf.knnMatch(des, des2, k=2)
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass

    if len(matchList) != 0:
        if max(matchList)> threshhold:
            finalValue = matchList.index(max(matchList))
            #print(matchList)
    return finalValue





path = r'/Photos/Pics'


images = []
imageNames = []
myList = os.listdir(path)

for realImageName in myList:
    currentImage = cv.imread(f'../../Photos/Pics/{realImageName}')#,0 makes it grayscale
    currentImage = bs.grayScale(currentImage)
    images.append(currentImage)
    imageNames.append(os.path.splitext(realImageName)[0])
#print(imageNames)

desArray = getDesArray(images)


vid = cv.VideoCapture(0)
lastIndex =-1
indexCount = 0
maxIndex = 10
show = False

mode = 1
while 1:
    success, liveImage = vid.read()
    gray = bs.grayScale(liveImage)

    index = getId(gray,desArray,20,2000)





    if index != -1:  # check if found something

        if mode == 1:
            liveImage = cv.putText(liveImage, imageNames[index], (0, 80), cv.FONT_HERSHEY_SIMPLEX, 3,
                                   (255, 255, 255), thickness=2)
        else:
            if lastIndex != index:# if other/new object found
                lastIndex = index#than take on new object
                print('reset' + "index" + str(index) + "count:" + str(indexCount))
                indexCount = 0#and reset counter


            else:
                indexCount+=1#increase couter if still save object

                if indexCount >= maxIndex:#if max reached turn on show
                        show = True
                        #print("index" + str(index) + "count:" + str(indexCount))

                if show:
                     liveImage = cv.putText(liveImage, imageNames[index], (0, 80), cv.FONT_HERSHEY_SIMPLEX, 3,
                                       (255, 255, 255), thickness=2)
    #else: show = False
    #print("index" + str(index)+"count:"+str(indexCount))






    bs.showLive(liveImage)
    cv.waitKey(1)
    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()

