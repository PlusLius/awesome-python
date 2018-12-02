import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ('0.0.0.0',12345)

s.bind(ip_port)

while True:
    data = s.recv(1024)

    print data
