#  -*- coding:utf8 -*-

import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',8080))
s.listen(8)

# newSocket,addr = s.accept()
def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print data
        re_data = raw_input()
        sock.send(re_data)

while True:
    # 接收客户端连接
     newSocket,addr = s.accept()

     client_thread = threading.Thread(target=handle_sock,args=(newSocket,addr))
   
     client_thread.start()
   # data = newSocket.recv(1024)
   #  print data
   #  re_data = raw_input()
   #  newSocket.send(data)
    
