# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delivery.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delivery(object):
    def setupUi(self, delivery):
        delivery.setObjectName("delivery")
        delivery.resize(488, 389)
        self.centralwidget = QtWidgets.QWidget(delivery)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(113, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(113, 130, 61, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 90, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 130, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 61, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(113, 230, 61, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 180, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 230, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.delivery_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delivery_btn.setGeometry(QtCore.QRect(190, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(11)
        self.delivery_btn.setFont(font)
        self.delivery_btn.setObjectName("delivery_btn")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 40, 69, 53))
        self.graphicsView.setObjectName("graphicsView")
        #delivery.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(delivery)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        #delivery.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(delivery)
        self.statusbar.setObjectName("statusbar")
        #delivery.setStatusBar(self.statusbar)

        self.retranslateUi(delivery)
        QtCore.QMetaObject.connectSlotsByName(delivery)

    def retranslateUi(self, delivery):
        _translate = QtCore.QCoreApplication.translate
        delivery.setWindowTitle(_translate("delivery", "配送"))
        self.label.setText(_translate("delivery", "配送"))
        self.label_2.setText(_translate("delivery", "仓库名称"))
        self.label_3.setText(_translate("delivery", "货柜名称"))
        self.label_4.setText(_translate("delivery", "商品名称"))
        self.label_5.setText(_translate("delivery", "配送数量"))
        self.delivery_btn.setText(_translate("delivery", "配送"))
class delivery_window(QtWidgets.QWidget, Ui_delivery):  # 创建子UI类

    def __init__(self):
        super(delivery_window, self).__init__()
        self.setupUi(self)
        self.graphicsView.setStyleSheet(
            "border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//peisong.png);")
