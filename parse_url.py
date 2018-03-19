#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: parse_url.py   拼接url地址的一个函数
@time: 2018/03/19
"""

URL = "http://127.0.0.1/version"

dicts = {'platform': 'Mac', 'object': 'agent', 'version': '20180319'}

def parse_url(data={}):
    item=data.items()
    urls='?'
    for i in item:
        (key,value) = i
        temp_str = key + "=" +value
        urls = urls +temp_str + "&"

    #urls = urls[:-1]
    urls = urls[:len(urls)-1]
    #两句话作用一致
    return urls

print (URL + parse_url(dicts))
