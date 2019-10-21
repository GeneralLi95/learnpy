#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yaoli 
@file: raw_input_test.py 
@time: 2018/11/27 
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        a = sys.argv[1]
        b = sys.argv[2]
    elif len(sys.argv) == 2:
        a = sys.argv[1]
        b = input("请输入参数b ")
    elif len(sys.argv) == 1:
        a = input("请输入参数a ")
        b = input("请输入参数b ")

    print(a + b)
    print(sys.argv)
