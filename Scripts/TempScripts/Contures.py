import cv2 as cv
import numpy as np


vid = cv.VideoCapture(0)

while True:
    _,img = vid.read()
    img = cv.flip(img,1)
    imgg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    _,imggg = cv.threshold(imgg,140,255,cv.THRESH_BINARY)

    conts,_h = cv.findContours(imggg,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    # if len(conts)!=0:
    #      for cont in conts:
    #          if cv.contourArea(cont)>500:
    #              x,y,w,h = cv.boundingRect(cont)
    #              cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    #mask = cv.drawContours(np.zeros(img.shape,np.uint8),conts,-1,(255,255,255),40)
    img = cv.drawContours(img,conts,-1,(1,10,60),4)

    cv.imshow("Name2", img)
    #img2 = cv.bitwise_xor(img,mask)
    #img3 = cv.bitwise_or(img,mask)

    #cv.imshow("Name",img)

    #cv.imshow("Name2", img2)

    #cv.imshow("Name3", img3)
    #cv.imshow("Mask", mask)



    if cv.waitKey(20) & 0xFF == ord('d'):
        break
