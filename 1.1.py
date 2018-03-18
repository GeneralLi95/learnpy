#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: 1.1.py   基本数据结构
@time: 2018/03/18 
"""

#Python3 中共有六个标准的数据类型：
# Number (数字） String(字符串) List（列表）Tuple(元组）Sets（集合）Dictionary（字典）


counter = 100   # int
miles = 1000.0  # float
name = "liyao"  # string

print (counter)
print (miles)
print (name)


#############

a, b, c, d = 20, 5.5, True, 4 + 3j
print (type(a), type(b), type(c), type(d))

#############


e = 111
print(isinstance(e, int))

#python2 中没有布尔型， 它用0 表示False，用1表示True。在Python3中，把True和False定义成了关键字，但是它们的值还是1和0，可以和数字相加

#############
