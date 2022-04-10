from PyQt5.Qt import *
import os
import pygame
import constant as c

class MySlider(QSlider):
    def __init__(self, window, x: int, y: int, value: int, x_size: int, y_size: int,
                 single_step: int, x_range: int, y_range: int,
                 direction: Qt.Orientation=Qt.Horizontal, connectFunc: str="self.normalSlider"):
        '''
        继承QSlider，滑块
        :param window: 窗口对象
        :param x: 位置
        :param y: 位置
        :param value: 默认值
        :param x_size: 大小
        :param y_size: 大小
        :param single_step: 每步大小
        :param x_range: 范围
        :param y_range: 范围
        :param direction: 方向
        :param connectFunc: 连接函数
        '''
        super(MySlider, self).__init__(window)
        self.move(QPoint(x, y))
        self.setValue(value)
        self.setOrientation(direction)
        self.resize(x_size, y_size)
        self.setSingleStep(single_step)
        self.setRange(x_range, y_range)
        self.valueChanged.connect(eval(connectFunc))

    def normalSlider(self):
        pass

    def changeVolume(self, volume):
        c.music.setVolume(float(volume / 100.0))

    def setMusicPos(self, musicPos):
        # c.music.setMusicPos(float(musicPos))
        pass