import cv2 as cv
from Scripts.Success import bigBrain as bs

vid = cv.VideoCapture(0)


def cascadeMode(name):

    if name == 'face':
        cascadeName = 'faceCascades.xml'
        a = 3
        b = 5

        rectColor = (255,0,0)
    elif name == 'eye':
        cascadeName = 'eyeCascade.xml'
        a = 3
        b = 5
        rectColor = (0, 255, 0)
    else:
        cascadeName = 'smileCascade.xml'
        a = 3.5
        b = 20
        rectColor = (0, 0, 255)


    cascade = cv.CascadeClassifier(cascadeName)
    facesRect = cascade.detectMultiScale(gray, a, b)

    for (x, y, w, h) in facesRect:
        cv.rectangle(liveImage, (x, y), (x + w, y + h), rectColor, thickness=2)
        cv.putText(liveImage, name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

    bs.showLive(liveImage)




while True:
    isTrue,liveImage = vid.read()
    liveImage = bs.flip(liveImage)
    gray = bs.grayScale(liveImage)

    cascadeMode('face')
    cascadeMode('eye')
    cascadeMode('smile')

    if bs.pressedKey('d'):
        break

vid.release()
cv.destroyAllWindows()