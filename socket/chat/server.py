#  -*- coding:utf8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',8080))
s.listen(8)
newSocket,addr = s.accept()

while True:
    data = newSocket.recv(1024)
    print data
    re_data = raw_input()

    newSocket.send(re_data)

    
