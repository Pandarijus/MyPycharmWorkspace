import socket

fileName = "recived.jpg"

ip = socket.gethostbyname(socket.gethostname())
port = 6969
buffer = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))

print(f"Connected to {(ip,port)}")
#fileName = client.recv(buffer)//is this alwais first??
file = open(fileName,"wb")#"recived.jpg"
while True:
    data = client.recv(buffer)
    if not data:
        break
    file.write(data)

print(f"Saved file")
file.close()
client.close()
