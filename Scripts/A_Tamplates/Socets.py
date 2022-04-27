import socket

#socet stuff video:  https://youtu.be/rPVy-OzWatM

socketConnection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAdressPort = ("127.0.0.1",6969)

while True:
    data = str.encode("Hello WORLD 420!")
    socketConnection.sendto(data,serverAdressPort)