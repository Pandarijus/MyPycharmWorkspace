import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("192.168.0.25", 6969))# clientSocket.connect(("localhost", 6969))

file = open("test.jpg", "rb")
imageBytes = file.read(2048)

while imageBytes:
    clientSocket.send(imageBytes)
    imageBytes = file.read(2048)

file.close()
clientSocket.close()