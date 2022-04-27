import cv2 as cv

vid = cv.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 720)
flip = True

while True:
    isTrue, liveImage = vid.read()
    if flip:
        flipped = cv.flip(liveImage,1)
    else:
        flipped = liveImage

    cv.imshow("hh", flipped)

    if cv.waitKey(20) & 0xFF == ord('f'):
        flip = not flip

    if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
        cv.imwrite("Screenshot.png",liveImage)#I don't use the fipped image
        break

vid.release()
cv.destroyAllWindows()