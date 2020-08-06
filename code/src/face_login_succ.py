# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_login_succ.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 491, 151))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logined = QtWidgets.QLabel(self.centralwidget)
        self.logined.setGeometry(QtCore.QRect(300, 190, 491, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(32)
        self.logined.setFont(font)
        self.logined.setObjectName("logined")
        self.logined_2 = QtWidgets.QLabel(self.centralwidget)
        self.logined_2.setGeometry(QtCore.QRect(310, 280, 491, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.logined_2.setFont(font)
        self.logined_2.setObjectName("logined_2")
        self.login_s_p = QtWidgets.QGraphicsView(self.centralwidget)
        self.login_s_p.setGeometry(QtCore.QRect(40, 180, 254, 254))
        self.login_s_p.setObjectName("login_s_p")
        self.logined_3 = QtWidgets.QLabel(self.centralwidget)
        self.logined_3.setGeometry(QtCore.QRect(310, 360, 491, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(22)
        self.logined_3.setFont(font)
        self.logined_3.setObjectName("logined_3")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " 欢迎来到能量站"))
        self.logined.setText(_translate("MainWindow", "√登陆成功，欢迎"))
        self.logined_2.setText(_translate("MainWindow", "您的角色是："))
        self.logined_3.setText(_translate("MainWindow", "三秒后自动进入界面……"))
class face_login_succ_window(QtWidgets.QWidget, Ui_MainWindow):  # 创建子UI类

    def __init__(self):
        super(face_login_succ_window, self).__init__()
        self.setupUi(self)
        self.draw()
    def change_text(self, name1: str,name2: str):
        _translate = QtCore.QCoreApplication.translate
        self.logined.setText(_translate("MainWindow", "登陆成功，欢迎"+name1))
        self.logined_2.setText(_translate("MainWindow", "您的角色是："+name2))
    def draw(self):
        # 添加图片时只能用\\或者/，不能直接用filepath
        self.login_s_p.setStyleSheet("border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//succ_login.png);")