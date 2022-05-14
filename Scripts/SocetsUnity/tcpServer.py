import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.25", 6969))
server.listen()
clientSocket, clientAddr = server.accept()
file = open('gotImage.jpg', 'wb')
package = clientSocket.recv(2048)
while package:
    file.write(package)
    package = clientSocket.recv(2048)

file.close()
clientSocket.close()