# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stock(object):
    def setupUi(self, stock):
        stock.setObjectName("stock")
        stock.resize(512, 373)
        #stock.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(stock)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(135, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(135, 120, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(135, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(135, 180, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(135, 210, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(135, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 150, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 210, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.stock_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stock_btn.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.stock_btn.setObjectName("stock_btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 120, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 180, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 240, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 105, 82))
        self.graphicsView.setObjectName("graphicsView")
        #stock.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(stock)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName("menubar")
        #stock.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(stock)
        self.statusbar.setObjectName("statusbar")
        #stock.setStatusBar(self.statusbar)

        self.retranslateUi(stock)
        QtCore.QMetaObject.connectSlotsByName(stock)

    def retranslateUi(self, stock):
        _translate = QtCore.QCoreApplication.translate
        stock.setWindowTitle(_translate("stock", "采购"))
        self.label.setText(_translate("stock", "采购"))
        self.label_1.setText(_translate("stock", "预计到货时间"))
        self.label_2.setText(_translate("stock", "供应商名称"))
        self.label_3.setText(_translate("stock", "运货费"))
        self.label_4.setText(_translate("stock", "商品名称"))
        self.label_5.setText(_translate("stock", "采购数量"))
        self.label_6.setText(_translate("stock", "仓库名称"))
        self.lineEdit.setText(_translate("stock", "\'2019-12-30\'"))
        self.lineEdit_2.setText(_translate("stock", "160.5"))
        self.lineEdit_4.setText(_translate("stock", "120"))
        self.stock_btn.setText(_translate("stock", "采购"))
        self.comboBox.setItemText(0, _translate("stock", "(请选择供应商)"))
        self.comboBox_2.setItemText(0, _translate("stock", "(请选择商品)"))
        self.comboBox_3.setItemText(0, _translate("stock", "(请选择仓库)"))
class stock_window(QtWidgets.QWidget, Ui_stock):  # 创建子UI类

    def __init__(self):
        super(stock_window, self).__init__()
        self.setupUi(self)
        self.graphicsView.setStyleSheet(
            "border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//caigou.png);")

