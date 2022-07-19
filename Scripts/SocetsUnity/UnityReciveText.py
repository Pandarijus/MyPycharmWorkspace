import socket
from time import sleep
import cv2 as cv
print("Clinet is running...")

UDP_IP = "127.0.0.1"
#UDP_IP = "192.168.0.79"
UDP_PORT = 6969
bufferSize = 8192#1024*8

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    print("Getting data...")
    sleep(1)
    data, addr = sock.recvfrom(bufferSize)  # buffer size is 1024 bytes
    print("received message: %s" % data)
