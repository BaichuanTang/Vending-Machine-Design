# -*- coding: utf-8 -*-
import datetime

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from src.admin_login import admin_login_window
from src.face_login_succ import face_login_succ_window
from src.face_login import face_login_window
from src.select_item import select_item_window
from src_face.predictor_face import mk_final_pred_face
from src.predictor import mk_final_pred_item
from src.select_item_results import select_item_results_window
from src.fankui import fankui_window
from src.stock_main_window import stock_main_window
from src.finance_main_window import finance_main_window
from src.delivery_main_window import delivery_main_window
from src.weixiu import weixiu_window
from src.why_choice import why_choice_window
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
'''
注意：
    按钮名字，
    搜索“修改”，改成你对应的
'''
# 修改
password = '123'
db_name = 'energystation'
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.face_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.face_login_btn.setGeometry(QtCore.QRect(180, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.face_login_btn.setFont(font)
        self.face_login_btn.setObjectName("face_login_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 491, 151))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.admin_login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.admin_login_btn.setGeometry(QtCore.QRect(510, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.admin_login_btn.setFont(font)
        self.admin_login_btn.setObjectName("admin_login_btn")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 340, 305, 203))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face_login_btn.setText(_translate("MainWindow", "人脸登录"))
        self.label.setText(_translate("MainWindow", " 欢迎来到能量站"))
        self.admin_login_btn.setText(_translate("MainWindow", "管理员登录"))

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.graphicsView.setStyleSheet(
            "border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//t0.jpg);")

        # setting main window geometry
        desktop_geometry = QtWidgets.QApplication.desktop()  # 获取屏幕大小
        main_window_width = desktop_geometry.width()  # 屏幕的宽
        main_window_height = desktop_geometry.height()  # 屏幕的高
        rect = self.geometry()  # 获取窗口界面大小
        window_width = rect.width()  # 窗口界面的宽
        window_height = rect.height()  # 窗口界面的高
        x = (main_window_width - window_width) // 2  # 计算窗口左上角点横坐标
        y = (main_window_height - window_height) // 2  # 计算窗口左上角点纵坐标
        self.setGeometry(x, y, window_width, window_height)  # 设置窗口界面在屏幕上的位置

        # 无边框以及背景透明一般不会在主窗口中用到，一般使用在子窗口中，例如在子窗口中显示gif提示载入信息等等
        #self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        #self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明

        '''
        手动新加
        '''
        self.admin_login_windows = admin_login_window()     # 实例化子界面
        self.admin_login_btn.clicked.connect(self.admin_login_clicked)# 槽函数连接

        self.face_login_windows = face_login_window()     # 实例化子界面
        self.face_login_btn.clicked.connect(self.face_login_clicked)# 槽函数连接

        self.face_login_succ_window = face_login_succ_window() #登陆成功
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.select_item_window = select_item_window()
        self.select_item_window.pushButton.clicked.connect(self.close_door)#关门
        self.select_item_results_window=select_item_results_window()
        self.timer2 = QtCore.QTimer(self)
        self.timer2.setSingleShot(True)
        self.timer3 = QtCore.QTimer(self)
        self.timer3.setSingleShot(True)
        self.timer4 = QtCore.QTimer(self)
        self.timer4.setSingleShot(True)
        self.timer0 = QtCore.QTimer(self)
        self.timer0.setSingleShot(True)
        self.select_item_results_window.pushButton.clicked.connect(self.fankui)
        self.fankui_window=fankui_window()
        self.fankui_window.shoujihao.setPlaceholderText('18810609200')
        self.fankui_window.pushButton_3.clicked.connect(self.fankui1)
        self.fankui_window.dingdanid.setPlaceholderText('订单号')
        self.fankui_window.pushButton_4.clicked.connect(self.fankui2)
        self.fankui_window.dingdanid_2.setPlaceholderText('货柜ID')
        self.fankui_window.pushButton.clicked.connect(self.fankui3)
        self.fankui_window.dingdanid_4.setPlaceholderText('详细描述')
        '''
        财务
        '''
        self.finance_main_window = finance_main_window()
        self.stock_main_window=stock_main_window()
        self.delivery_main_window=delivery_main_window()
        self.weixiu_window=weixiu_window()
        self.why_choice_window=why_choice_window()
        #self.why_choice_window.delivery_btn.clicked.connect(lambda x: self.why_choice_window.close())
        self.why_choice_window.delivery_btn.clicked.connect(lambda x: self.stock_main_window.show())
        #self.why_choice_window.delivery_btn_2.clicked.connect(lambda x: self.why_choice_window.close())
        self.why_choice_window.delivery_btn_2.clicked.connect(lambda x: self.delivery_main_window.show())
        self.op_time=None
        self.sql1=None
        self.cd_time=None
        self.dict_cyf=None
        self.userID=None
        self.ContainerID=None

    def admin_login_clicked(self):
        self.admin_login_windows.show()
    def face_login_clicked(self):
        self.face_login_windows.show()
        who = mk_final_pred_face()
        #who='why'
        if who=='tbc':
            self.face_login_windows.close()
            self.face_login_succ_window.change_text('唐百川','顾客')
            self.face_login_succ_window.show()
            self.timer.start(3000)
            self.timer.timeout.connect(self.tbc_select_items)
        if who=='cjy':
            self.face_login_windows.close()
            self.face_login_succ_window.change_text('陈洁仪','财务员')
            self.face_login_succ_window.show()
            self.timer2.start(3000)
            self.timer2.timeout.connect(self.cjy_todo)
        if who=='why':
            self.face_login_windows.close()
            self.face_login_succ_window.change_text('吴昊雨','采购员、配送员')
            self.face_login_succ_window.show()
            self.timer3.start(3000)
            self.timer3.timeout.connect(self.why_todo)
        if who == 'cyf':
            self.face_login_windows.close()
            self.face_login_succ_window.change_text('崔一帆','维修员')
            self.face_login_succ_window.show()
            self.timer4.start(3000)
            self.timer4.timeout.connect(self.cyf_todo)
    def why_todo(self):
        self.face_login_succ_window.close()
        self.why_choice_window.show()
    def cjy_todo(self):
        self.face_login_succ_window.close()
        self.finance_main_window.show()
    def cyf_todo(self):
        self.face_login_succ_window.close()
        self.weixiu_window.show()
    def tbc_select_items(self):
        self.face_login_succ_window.close()

        self.select_item_window.show()
        print('selected started')
        '''
        留给崔凡 开柜时间
        '''
        self.op_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.item_results_map=mk_final_pred_item()
        self.item_results_map.pop('blank')
        self.item_results_map["百事可乐-青柠"] = self.item_results_map.pop("kele")
        self.item_results_map["北冰洋"] = self.item_results_map.pop("beibingyang")
        self.item_results_map["加多宝"] = self.item_results_map.pop("jiaduobao")
        self.item_results_map["纯享"] = self.item_results_map.pop("suannai")
        self.item_results_map["可口可乐-爽椰派"] = self.item_results_map.pop("xuebi")
    def close_door(self):
        #self.face_predictor.end_tag=1
        #self.face_predictor=None
        cv2.destroyAllWindows()
        self.select_item_window.close()
        print('选购完成')
        st = ''
        sump=0
        prices = [3,5,4.5,8,6]
        for (i, j) ,p in zip(self.item_results_map.items(),prices):
            st += i
            st += '\t'
            st += str(j)
            sump+=j*p
            st += '\n'
        st=st+'总价为'+str(sump)+'元'
        '''
        导入DB
        '''
        self.sql1 = "call purchase('{}','{}',{},{},{});"
        self.cd_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dict_cyf={
            '北冰洋':1,
            '加多宝':2,
            '百事可乐-青柠':3,
            '可口可乐-爽椰派':4,
            '纯享':5
        }
        self.UserID=1
        self.ContainerID=4
        #self.Insert(self.sql1, self.cd_time, self.dict_cyf, self.UserID, self.ContainerID)
        self.select_item_results_window.textBrowser.setText(st)
        self.select_item_results_window.show()


    def Insert(self,sql1,cd_time,dict_cyf,UserID,ContainerID):
        print('ab')
        for name in self.item_results_map:
            print(name)
            if self.item_results_map[name]!=0:
                print(self.item_results_map[name])
                print(cd_time,dict_cyf,UserID,ContainerID)
                self.IDU(
                    sql1.format(
                        self.op_time,
                        self.cd_time,
                        self.UserID,
                        self.ContainerID,
                        dict_cyf[name],
                        self.item_results_map[name]
                    )
                )

    def IDU(self, sql):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=password, db=db_name, charset='utf8')
        cursor = conn.cursor()
        # print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            QMessageBox.information(self, "Message", "操作成功~", QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Message", "Something Wrong!", QMessageBox.Yes)
            conn.rollback()
        cursor.close()
        conn.close()

    def fankui(self):
        self.select_item_results_window.close()
        self.fankui_window.show()
    def fankui1(self):
        paras = self.fankui_window.shoujihao.text()
        print('留给崔凡 btn1',paras)
        #数据库里面查询
        #tableWidget怎么样
    def fankui2(self):
        paras = self.fankui_window.dingdanid.text()
        print('留给崔凡 btn2',paras)
        #数据库里面查询
        #tableWidget_2怎么样
    def fankui3(self):
        paras1 = self.fankui_window.dingdanid_2.text()
        paras2 = self.fankui_window.dingdanid_4.text()
        print('留给崔凡 btn3',paras1)
        print('留给崔凡 btn3', paras2)
        #数据库里面查询怎么样





import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())