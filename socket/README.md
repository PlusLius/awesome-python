## socket的使用

> socket.socket(网络层ip协议蔟,传输层协议类型,默认协议)

```py
# server.py
# 导入模块
import socket

# 实例化服务器,使用ipv4协议,tcp协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口号 0.0.0.0监听所有ip地址
s.bind(('0.0.0.0',12345)) 

# 监听端口,设置连接数 
s.listen(5)

# 阻塞挂起，等待客户端连接
connSocket,addr = s.accept()

# 连接成功后，接收客户端发来的数据,设置一次接收的数据大小,1kb
data = connSocket.recv(1024)

# 返回数据
connSocket.send(data)

# 断开连接
connSocket.close()

# client.py
# 导入模块
import socket

# 实例化客户端
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务器
client.connect(('127.0.0.1',8080))

# 接收服务器数据
client.recv(1024)

# 断开连接
client.close()
```

## socket的通信过程

![](../imgs/tcp.png)

## socket的应用

```py
# 模拟http客户端发送请求

# 导入socket模块和url解析模块
import socket
from urlparse import urlparse

# 定义发送请求get_url函数
def get_url(url):
   # 解析url
   url = urlparse(url)
   # 提取主机名
   host = url.netloc
   # 提取路径
   path = url.path
   # 如果路径没有,访问根路径
   if path == "":
      path = "/" 
   # 客户端实例化 
   client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   # 建立socket连接
   client.connect((host,80))
   # 构造http协议 
   protol = "GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n".format(path,host)
   # 发送请求数据
   client.send(protol)
   # 定义data接收服务器的返回结果 
   data = ""
   # 确保接收完数据
   while True:
     d = client.recv(1024)
     # 如果有值继续拼接
     if d:
       data += d
     else:
       break
    # 将返回协议提取出来
    html_data = data.split('\r\n\r\n')[1]
    # 打印提取结果
    print html_data 
    # 断开tcp连接

```
