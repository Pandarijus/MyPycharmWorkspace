import numpy as np
from Scripts.Success import bigBrain as bs
import cv2 as cv

img = bs.getPrepedImage()

lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
#bs.show(lap)

sobleX = cv.Sobel(img, cv.CV_64F,1,0)
bs.show(sobleX)
sobleY = cv.Sobel(img, cv.CV_64F,0,1)
bs.show(sobleY)

combinedSobble = bs.combine(sobleX,sobleY)
bs.show(combinedSobble)
cv.waitKey(0)