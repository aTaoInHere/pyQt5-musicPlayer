from PyQt5.Qt import *
import os
import pygame
import constant as c

class MyList(QListView):
    def __init__(self, x: int, y: int, qList: list, connectFunc: str="self.normalList"):
        '''
        继承QListView
        :param x: x位置
        :param y: y位置
        :param qList: 列表内容
        :param connectFunc: 连接函数名称
        '''
        super(MyList, self).__init__(c.w)
        self.move(QPoint(x, y))
        # self.clicked.connect(eval(connectFunc))
        self.slm = QStringListModel()  # 创建mode
        self.qList = [s.split('/')[-1][0:-4] for s in qList]  # 添加的数组数据
        self.slm.setStringList(self.qList)  # 将数据设置到model
        self.setModel(self.slm)  ##绑定 listView 和 model
        self.show()
        # QListWidget
        # self.closePersistentEditor(self.slm)
        self.doubleClicked.connect(eval(connectFunc))  # listview 的点击事件
        # self.setEditTriggers(QAbstractItemView=NoEditTriggers)
        # layout.addWidget(listView)  # 将list view添加到layout
        # self.setLayout(layout)

    def normalList(self):
        pass

    def doubleClickedPlay(self, item):
        c.music.loadCurrMusic(byName=True, name=item.data())

    def setQueryContent(self, qList: list):
        '''
        显示查询结果
        :param qList: 查询内容
        :return:
        '''
        self.slm.setStringList(qList)
        self.setModel(self.slm)
        self.show()