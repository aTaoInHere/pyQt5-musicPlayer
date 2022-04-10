from PyQt5.Qt import *
import os
import pygame
import constant as c
# from PyQt5.QtCore import QTimer

class MyLabel(QLabel):
    def __init__(self, window: QWidget, text: str, x: int, y: int):
        '''
        继承QLabel
        :param window: 窗口对象，父控件
        :param text: 按键内容
        :param x: x位置
        :param y: y位置
        '''
        super(MyLabel, self).__init__(window)
        self.setText(text)
        self.move(QPoint(x, y))

    def setText(self, text: str) -> None:
        super(MyLabel, self).setText(text)

    def move(self, a0: QPoint) -> None:
        super(MyLabel, self).move(a0)

    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        try:
            if not c.music.justPause: #非暂停
                current_sec = int(self.text()[0]) * 60 + int(self.text()[2]) * 10 + int(self.text()[3])
                if current_sec != 0:
                    #歌曲进度条前进
                    c.music.progress_bar.setValue(c.music.music_time - current_sec)
                    current_sec -= 1
                    if current_sec % 60 < 10:
                        self.setText('{}:0{}'.format(current_sec // 60, current_sec % 60))
                    else:
                        self.setText('{}:{}'.format(current_sec // 60, current_sec % 60))
                    self.current_sec = current_sec
        except Exception:
            print("我有问题！")

