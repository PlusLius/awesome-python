# -*- coding:utf-8 -*-
# 引入socket模块
import socket

# 实例化socket
s = socket.socket()

# 获取本地主机名
host = socket.gethostname() 

# 获取端口
port = 12345

# 绑定端口
s.bind((host,port))

# 监听端口
s.listen(5) 

while True:
    # 获取客户端socket
    c,addr = s.accept()
    print '连接地址',addr
   
    # 想客户端发送消息
    c.send('欢迎连接本服务器')

    # 关闭连接 
    c.close() 
    

