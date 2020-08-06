# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_good.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_good(object):
    def setupUi(self, add_good):
        add_good.setObjectName("add_good")
        add_good.resize(489, 373)
        self.centralwidget = QtWidgets.QWidget(add_good)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 35, 121, 51))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(150, 130, 71, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 130, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 180, 54, 12))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(260, 180, 113, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 230, 54, 12))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 230, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.addGood = QtWidgets.QPushButton(self.centralwidget)
        self.addGood.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.addGood.setObjectName("addGood")
        # add_good.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_good)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 23))
        self.menubar.setObjectName("menubar")
        # add_good.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_good)
        self.statusbar.setObjectName("statusbar")
        # add_good.setStatusBar(self.statusbar)

        self.retranslateUi(add_good)
        QtCore.QMetaObject.connectSlotsByName(add_good)

    def retranslateUi(self, add_good):
        _translate = QtCore.QCoreApplication.translate
        add_good.setWindowTitle(_translate("add_good", "添加商品"))
        self.label.setText(_translate("add_good", "添加商品"))
        self.label_1.setText(_translate("add_good", "商品名称"))
        self.lineEdit.setText(_translate("add_good", "大西洋"))
        self.label_2.setText(_translate("add_good", "单价"))
        self.lineEdit_1.setText(_translate("add_good", "5.5"))
        self.label_3.setText(_translate("add_good", "单位"))
        self.lineEdit_2.setText(_translate("add_good", "罐"))
        self.addGood.setText(_translate("add_good", "添加"))

class add_good_window(QtWidgets.QWidget, Ui_add_good):  # 创建子UI类

    def __init__(self):
        super(add_good_window, self).__init__()
        self.setupUi(self)