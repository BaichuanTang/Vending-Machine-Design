# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'why_choice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(488, 389)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 301, 81))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delivery_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delivery_btn.setGeometry(QtCore.QRect(120, 220, 91, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        self.delivery_btn.setFont(font)
        self.delivery_btn.setObjectName("delivery_btn")
        self.delivery_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delivery_btn_2.setGeometry(QtCore.QRect(260, 220, 91, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(13)
        self.delivery_btn_2.setFont(font)
        self.delivery_btn_2.setObjectName("delivery_btn_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 401, 111))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        #mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        #mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "功能选择"))
        self.label.setText(_translate("mainWindow", "     功能选择"))
        self.delivery_btn.setText(_translate("mainWindow", "采购员"))
        self.delivery_btn_2.setText(_translate("mainWindow", "配送员"))
        self.label_2.setText(_translate("mainWindow", "吴昊雨同学同时担任物流员与配送员的角色"))
class why_choice_window(QtWidgets.QWidget, Ui_mainWindow):  # 创建子UI类

    def __init__(self):
        super(why_choice_window, self).__init__()
        self.setupUi(self)