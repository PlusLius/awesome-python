# -*-coding:utf-8-*-
# 导入socket模块
import socket

# 实例化客户端
s = socket.socket()

# 保持和服务器的主机名端口一致
host = socket.gethostname()
port = 12345

# 连接服务器
s.connect((host,port))

# 接收的数据为1024个字节
print s.recv(1024)

# 接收完数据后断开连接
s.close()
