import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6969))
server.listen()
clientSocekt, clientAddr = server.accept()
file = open('gotImage.jpg', 'wb')
package = clientSocekt.recv(2048)
while package:
    file.write(package)
    package = clientSocekt.recv(2048)

file.close()
clientSocekt.close()