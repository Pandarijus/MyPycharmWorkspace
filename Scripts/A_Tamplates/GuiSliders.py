def nothing():
    pass
windowName = "Trackbars"
cv.namedWindow(windowName)

cv.createTrackbar("mini", windowName, 13, 255, nothing)
cv.createTrackbar("maxi", windowName, 41, 255, nothing)

    mini = cv.getTrackbarPos("mini", windowName)
    maxi = cv.getTrackbarPos("maxi", windowName)