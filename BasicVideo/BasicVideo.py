import cv2 as cv

vid = cv.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 720)

while True:
    isTrue, liveImage = vid.read()
    cv.imshow("hh", liveImage)

    if cv.waitKey(20) & 0xFF == ord('d'):  # Quit
        break

vid.release()
cv.destroyAllWindows()