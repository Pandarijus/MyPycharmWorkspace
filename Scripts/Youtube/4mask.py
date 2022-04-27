from Scripts.Success import bigBrain as bs
import cv2 as cv

img = bs.getMarsImage()
img = bs.res(img,.18)
temp = bs.getEmptyImage(img.shape[:2])
mask = cv.circle(temp, (230, 60), 50, 255, -1)
masked = bs.cutWithMask(img,mask)

bs.show(masked)





























cv.waitKey(0)