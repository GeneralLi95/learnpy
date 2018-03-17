#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: web_demo.py 
@time: 2018/03/16 
"""

def application(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    a = 'hello world'
    return [b'<h1>a</h1>']
