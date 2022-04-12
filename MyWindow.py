import threading
import pygame
import time
import os
from PyQt5.Qt import *
from MyButton import *
from Music import *
from MySlider import MySlider
import constant as c
from MyLabel import MyLabel

class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("音乐播放器")  # 窗口名称
        self.resize(500, 500)  # 改变大小
        self.move(500, 200)  # 窗口位置
        self.setUi()

    def setUi(self):
        # 添加歌曲按钮
        self.bt_add_files = MyButton(self, "添加歌曲", 50, 20, "self.openFileAndAddFiles")

        # 播放/暂停
        self.bt_play_pause = MyButton(self, "播放", 200, 80, "self.playMusic")

        # 上一曲
        self.bt_prev_music = MyButton(self, "上一曲", 50, 80, "self.prevMusic")

        # 下一曲
        self.bt_next_music = MyButton(self, "下一曲", 350, 80, "self.nextMusic")

        # 音量控制标签
        self.la_volume = MyLabel(self, "音量", 270, 30)

        # 音量控制滑块
        self.sl_volume = MySlider(self, 320, 26, 50, 150, 25, 1, 0, 100, Qt.Horizontal, "self.changeVolume")

        self.le_query = QLineEdit(self)
        self.le_query.move(50, 400)
        self.le_query.resize(300, 50)
        # self.le_query.setText("请输入你想要查询的歌曲")
        self.le_query.setPlaceholderText("请输入你想要查询的歌曲")
        def querry():
            query_name = c.w.le_query.text()
            list = []
            for music_name in [s.split('/')[-1][0:-4] for s in c.music.musics]:
                if query_name in music_name:
                    list.append(music_name)
            self.bt_add_files.mylist.setQueryContent(list)
        self.le_query.textChanged.connect(querry)

        #查询按钮
        self.bt_query_music = MyButton(self, "查询", 360, 408, "self.queryMusicByName")

        self.q = QMdiSubWindow(self)
        self.q.close()





