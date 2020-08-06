# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Face_login(object):
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
        self.logining = QtWidgets.QLabel(self.centralwidget)
        self.logining.setGeometry(QtCore.QRect(240, 180, 331, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.logining.setFont(font)
        self.logining.setObjectName("logining")
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
        self.logining.setText(_translate("MainWindow", "扫脸登陆中……"))

class face_login_window(QtWidgets.QWidget, Face_login):  # 创建子UI类

    def __init__(self):
        super(face_login_window, self).__init__()
        self.setupUi(self)
