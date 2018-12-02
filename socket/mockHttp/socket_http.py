# -*-coding:utf-8-*-
import socket
from urlparse import urlparse

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    # 提取主域名
    host = url.netloc
    # 提取路径
    path = url.path
    if path == "":
        path = "/"
        
    # 建立socket连接
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,80))

    # 发送数据
    client.send("GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n".format(path,host))
    data = ""
    while True:
      d = client.recv(1024) 
      if d:
          data += d
      else:
          break
    html_data = data.split('\r\n\r\n')[1]
    print html_data 
    client.close()

get_url('https://www.baidu.com')
