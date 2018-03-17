#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: server.py 
@time: 2018/03/16 
"""

from wsgiref.simple_server import  make_server
from hello import application

httped = make_server('',8000, application)
print('serving HTTP on port 8000...')

httped.serve_forever()


