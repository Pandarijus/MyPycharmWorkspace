import socket

fileName = "g.jpg"

ip = socket.gethostbyname(socket.gethostname())
port = 6969
buffer = 1024
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port))
print(f"Sender Connected at IP [{ip}] to the port {port}")
server.listen()#WHAT DOES THIS DO?

client,add = server.accept()
print(f"Accepted client at {add}")

with open(fileName,"rb") as file:

    while True:
        data = file.read(buffer)
        if not data:
            break
        client.send(data)
    client.close()
