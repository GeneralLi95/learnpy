#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: do_tcp.py 
@time: 2018/03/17 
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

#客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。新浪网站的IP地址可以使用域名www.sina.com.cn自动转换到IP地址

#80端口是Web服务的标准端口，SMTP的服务是25端口  FTP是21端口。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把接收的数据写入文件:
with open('sina.html','wb') as f:
    f.write(html)