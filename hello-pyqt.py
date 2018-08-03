#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: hello-pyqt.py 
@time: 2018/08/02 
"""
import untitled

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
if __name__=='__main__':
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = untitled.Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

