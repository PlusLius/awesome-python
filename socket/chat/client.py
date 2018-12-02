# -*- coding:utf8 -*-

import socket

c  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('127.0.0.1',8080))

while True:
    re_data = raw_input()
    c.send(re_data)
    data = c.recv(1024)
    print data
