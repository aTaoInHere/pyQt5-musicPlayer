from PyQt5.Qt import *
import os
import pygame
import constant as c
from MyList import MyList

class MyButton(QPushButton):
    def __init__(self, window, text: str, x: int, y: int, connectFunc: str="self.normalButton"):
        '''
        继承QpushButton
        :param text: 按键内容
        :param x: x位置
        :param y: y位置
        :param connectFunc: 连接函数名称
        '''
        super(MyButton, self).__init__(window)
        self.setText(text)
        self.musics = []
        self.move(QPoint(x, y))
        self.clicked.connect(eval(connectFunc))

    def setText(self, text: str) -> None:
        super(MyButton, self).setText(text)

    def move(self, a0: QPoint) -> None:
        super(MyButton, self).move(a0)

    def updateFunc(self, connectFunc: str) -> None:
        pass

    def normalButton(self):
        '''
        无函数 站位槽
        :return:
        '''
        pass

    def openFileAndAddFiles(self):
        '''
        添加歌曲连接函数槽
        :return:
        '''
        try:
            # 其中self指向自身，"读取文件夹"为标题名，"./"为打开时候的当前路径
            self.directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
            self.musics = [self.directory + '/' + music for music in os.listdir(self.directory)]
            c.music.loadMusicPath(self.musics)
            self.mylist = MyList(50 ,200, self.musics, "self.doubleClickedPlay")
        except Exception:
            return

    def playMusic(self):
        '''
        播放暂停连接函数槽
        :return:
        '''
        if (self.text() == '播放'):
            try:
                c.music.play()
                self.setText('暂停')
            except Exception:
                return
        else:
            try:
                c.music.pause()
                self.setText('播放')
            except Exception:
                return

    def nextMusic(self):
        try:
            c.w.bt_play_pause.setText('暂停')
            c.music.nextMusic()
        except Exception:
            return

    def prevMusic(self):
        try:
            c.w.bt_play_pause.setText('暂停')
            c.music.prevMusic()
        except Exception:
            return