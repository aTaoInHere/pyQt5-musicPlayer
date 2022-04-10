import threading
import pygame
import time
import os
from PyQt5.Qt import *
from MyButton import *
from Music import *
import constant as c
from MyWindow import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)  # 创建应用程序对象 （sys.argv命令行python代码的名称）
    # print(app.arguments()) #获取命令行参数  # print(qApp.arguments()) 全局变量

    window = MyWindow()  # 窗口对象#创建一个控件，其没有父控件，则默认为父控件，当作顶层控件，
    # 系统会自动给窗口添加一些装饰（标题栏），以及窗口控件的特性，设置图标名称
    # 控件也可以作为一个容器，承载其他控件
    window.show()  # 标签控件被装入父控件，父控件展示，子空间默认show()
    c.w = window
    sys.exit(app.exec_())  # app.exec_()执行对象，并进入消息循环 exit()->输出退出码