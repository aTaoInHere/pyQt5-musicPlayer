import time
from PyQt5.QtCore import QTimer
import eyed3
import pygame
import threading
import constant as c
from MyLabel import MyLabel
from MySlider import MySlider

class Music:
    '''
    pygame.mixer.music.load()  ——  载入一个音乐文件用于播放
    pygame.mixer.music.play()  ——  开始播放音乐流
    pygame.mixer.music.rewind()  ——  重新开始播放音乐
    pygame.mixer.music.stop()  ——  结束音乐播放
    pygame.mixer.music.pause()  ——  暂停音乐播放
    pygame.mixer.music.unpause()  ——  恢复音乐播放
    pygame.mixer.music.fadeout()  ——  淡出的效果结束音乐播放
    pygame.mixer.music.set_volume()  ——  设置音量
    pygame.mixer.music.get_volume()  ——  获取音量
    pygame.mixer.music.get_busy()  ——  检查是否正在播放音乐
    pygame.mixer.music.set_pos()  ——  设置播放的位置
    pygame.mixer.music.get_pos()  ——  获取播放的位置
    pygame.mixer.music.queue()  ——  将一个音乐文件放入队列中，并排在当前播放的音乐之后
    pygame.mixer.music.set_endevent()  ——  当播放结束时发出一个事件
    pygame.mixer.music.get_endevent()  ——  获取播放结束时发送的事件
    Pygame 中播放音乐的模块和 pygame.mixer 模块是密切联系的。使用音乐模块去控制在调音器上的音乐播放。
    '''
    def __init__(self):
        pygame.mixer.init()
        self.music_num = 0
        self.musics = []
        self.justPause = False #判断是否暂停标志
    
    def loadMusicPath(self, musics):
        '''
        加载音乐路径
        预加载第一首歌
        加载音乐时间标签，以及计时器,进度条
        :param musics: 音乐路径
        :return:
        '''
        self.musics = musics
        print(musics)
        self.len_musics = len(self.musics)
        self.loadCurrMusic(isPlay=False) #首次加载歌曲
        self.music_time_label = MyLabel(c.w, "", 90, 130) #音乐时长标签
        self.music_name_label = MyLabel(c.w, "", 70, 168) #音乐名称标签
        self.progress_bar = MySlider(c.w, 200, 140, 0, 250, 7, 1, 0, 0, connectFunc="self.setMusicPos") #进度条对象
        self.timer = QTimer(c.w.bt_play_pause)  # 初始化一个定时器
        self.timer.timeout.connect(c.music.nextMusic)
        # 计时结束调用c.music.nextMusic()方法 ->自动切歌，更换掉有逼格的线程检查
        self.music_time_label.startMyTimer(1000)  # 开启歌曲时长计时器
        self.musics_name = [self.musics[i].split('/')[-1][0:-4] for i in range (self.len_musics)]#歌曲名
        print(self.musics_name)

            
    def play(self, numOfMusic=1):
        '''
        播放歌曲
        :param numOfMusic: 歌曲队列长度
        :return:
        '''
        self.justPause = False
        # threading.Thread(target=self.checkMusicPlaying).start()
        if self.musics is not None and self.first_play:
            self.music_name_label.setText('正在播放 {}'.format(self.musics_name[self.music_num % self.len_musics]))
            print(self.musics[self.music_num % self.len_musics].split('/')[-1][0:-4])
            self.timer.start((self.music_time + 1) * 1000)  # 设置计时间隔并启动，结束自动调用nextMusic()
            #歌曲播放进度条
            self.progress_bar.setRange(0, self.music_time + 1)
            if self.music_time % 60 < 10:
                self.music_time_label.setText('{}:0{}'.format(self.music_time // 60, self.music_time % 60))
            else:
                self.music_time_label.setText('{}:{}'.format(self.music_time // 60, self.music_time % 60))

            self.music_time_label.show()
            self.music_name_label.show()
            self.progress_bar.show()
            # pygame.mixer.music.set_endevent(1)
            # threading.Thread(target=self.checkMusicPlaying).start()
            pygame.mixer.music.play(numOfMusic)
            self.first_play = False
        else:

            pygame.mixer.music.unpause()

    def pause(self):
        '''
        暂停歌曲
        :return:
        '''
        self.justPause = True
        if self.musics is not None:
            pygame.mixer.music.pause()

    def nextMusic(self):
        '''
        下一首
        :return:
        '''
        self.music_num += 1
        # self.music_num %= self.len_musics
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.loadCurrMusic(num=self.music_num)
        # pygame.mixer.music.load(self.musics[self.music_num].encode())
        # self.first_play = True
        # self.play()

    def prevMusic(self):
        '''
        上一首
        :return:
        '''
        self.music_num -= 1
        # self.music_num %= self.len_musics
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.loadCurrMusic(num=self.music_num)
        # pygame.mixer.music.load(self.musics[self.music_num].encode())
        # self.first_play = True
        # self.play()

    def checkMusicPlaying(self):
        '''
        线程-> 检查当前歌曲是否播放完毕，播放完跳到下一首
        :return:
        '''
        while True:
            print(pygame.mixer.music.get_busy())
            if not pygame.mixer.music.get_busy():
                time.sleep(3)
                if not pygame.mixer.music.get_busy() and not self.justPause:
                    c.music.nextMusic()

    def loadCurrMusic(self, num: int=0, isPlay: bool=True, byName: bool=False, name: str=''):
        '''
        加载当前音乐并播放
        :param num: 当前音乐序号
        :param isPlay: 是否播放
        :param byName:
        :param name:
        :return:
        '''
        # self.music_num = num if not byName else i for i in range(self.len_musics) if self.musics[i % self.len_musics] == name
        if not byName:
            self.music_num = num
        else:
            for i in range(self.len_musics):
                if self.musics_name[i % self.len_musics] == name:
                    self.music_num = num = i
        pygame.mixer.music.load(self.musics[num % self.len_musics].encode())
        #获取歌曲时长
        self.music_time = self.getVoiceTimeSecs(self.musics[num % self.len_musics].replace('/', '\\'))
        self.first_play = True
        if isPlay:
            self.play()

    def setVolume(self, volume: float):
        '''
        设置音量
        :param volume:
        :return:
        '''
        pygame.mixer.music.set_volume(volume)

    def getVoiceTimeSecs(self, file_path):
        """
        获取音频文件时长
        :param file_path 文件路径
        """
        # 加载本地文件
        voice_file = eyed3.load(file_path)
        # 获取音频时长
        secs = int(voice_file.info.time_secs)
        return secs

    def setMusicPos(self, sec: float):
        """
        设置播放的位置
        :param sec 播放的位置
        """
        # self.music_time_label.current_sec = sec
        # 绝对定位
        pygame.mixer.music.rewind()
        # 设置播放的位置
        pygame.mixer.music.set_pos(sec)

        