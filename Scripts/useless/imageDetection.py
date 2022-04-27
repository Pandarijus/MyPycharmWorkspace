import cv2 as cv
from Scripts.Success import bigBrain as bs

image = bs.getPrepedImage()
image2 = image.copy()

orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(image, None)
kp2, des2 = orb.detectAndCompute(image2, None)
# image = cv.drawKeypoints(image, kp1, None)

bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

mat = cv.drawMatchesKnn(image, kp1, image2, kp2, good,None)
print(len(good))
cv.imshow('l', mat)
cv.waitKey(0)