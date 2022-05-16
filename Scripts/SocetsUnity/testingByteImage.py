import cv2 as cv
import numpy as np

with open("text.txt","br") as file:
    data = file.read()
    print(data)
    data = np.frombuffer(data,np.uint8)
    print(data)
    #img = cv.imdecode(data, cv.IMREAD_COLOR)
    img = data

    while True:
        cv.imshow("image", img)
        cv.waitKey(1)