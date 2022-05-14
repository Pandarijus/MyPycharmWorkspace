import socket
from time import sleep

print("Server is running...")
socketConnection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAdressPort = ("127.0.0.1",6969)

while True:
    sleep(1)
    print("Send...")
    data = str.encode("Hello WORLD 420!")
    socketConnection.sendto(data,serverAdressPort)