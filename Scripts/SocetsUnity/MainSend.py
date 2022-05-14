import socket
from time import sleep
import cv2 as cv

# START
print("Server is running...")
socketConnection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAdressPort = ("127.0.0.1",6969)

vid = cv.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 720)



# UPDATE
while True:
    isTrue, liveImage = vid.read()
    cv.imshow("hi", liveImage)
    # data = cv.imencode('.jpg', liveImage)[1].tobytes()
    # print(data)
    # sleep(10)
    # socketConnection.sendto(data, serverAdressPort)

    if cv.waitKey(20) & 0xFF == ord('d'):
        cv.imwrite("test.jpg", liveImage)
        break

vid.release()
cv.destroyAllWindows()
