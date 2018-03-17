#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: hello.py
@time: 2018/03/16 
"""

def application(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    #http状态码  200 -服务器成功返回网页，OK 一切正常
    #404 -请求的网页不存在
    #503 -服务不可用  还有一些其他的状态码
    body = '<h1>hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
    #return [b'<h1>Hello, web!</h1>']
