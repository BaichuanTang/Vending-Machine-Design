# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weixiu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(797, 681)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(33)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.seeWareHouseInventory = QtWidgets.QPushButton(self.centralwidget)
        self.seeWareHouseInventory.setGeometry(QtCore.QRect(136, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.seeWareHouseInventory.setFont(font)
        self.seeWareHouseInventory.setObjectName("seeWareHouseInventory")
        self.addGood = QtWidgets.QPushButton(self.centralwidget)
        self.addGood.setGeometry(QtCore.QRect(136, 165, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.addGood.setFont(font)
        self.addGood.setObjectName("addGood")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(430, 88, 331, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(136, 420, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "     (请选择货柜)")
        self.seeContainerInventory = QtWidgets.QPushButton(self.centralwidget)
        self.seeContainerInventory.setGeometry(QtCore.QRect(136, 490, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.seeContainerInventory.setFont(font)
        self.seeContainerInventory.setObjectName("seeContainerInventory")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(430, 440, 331, 131))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.seeContainerHotGood = QtWidgets.QPushButton(self.centralwidget)
        self.seeContainerHotGood.setGeometry(QtCore.QRect(140, 570, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.seeContainerHotGood.setFont(font)
        self.seeContainerHotGood.setObjectName("seeContainerHotGood")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(318, 500, 111, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(220, 450, 20, 41))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(430, 260, 331, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 300, 61, 31))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(220, 520, 20, 51))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 530, 181, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(318, 323, 111, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(320, 170, 111, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(30, 40, 126, 123))
        self.graphicsView_2.setObjectName("graphicsView_2")
        #mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName("menubar")
        #mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        #mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "维修员子界面"))
        self.label.setText(_translate("mainWindow", "欢迎维修员"))
        self.seeWareHouseInventory.setText(_translate("mainWindow", "故障信息汇总"))
        self.addGood.setText(_translate("mainWindow", "查看未完成维修"))
        self.seeContainerInventory.setText(_translate("mainWindow", "查看货柜的状态"))
        self.seeContainerHotGood.setText(_translate("mainWindow", "是"))
        self.label_2.setText(_translate("mainWindow", "可视化"))
        self.label_3.setText(_translate("mainWindow", "更改货柜状态？"))
import pymysql
password = '123'
db_name = 'energystation'
class weixiu_window(QtWidgets.QWidget, Ui_mainWindow):  # 创建子UI类

    def __init__(self):
        super(weixiu_window, self).__init__()
        self.setupUi(self)
        self.draw()

        # 设置货柜combobox的内容
        rows1 = self.select('select 货柜名称 from 货柜', ['货柜名称'])[0]
        for i in range(len(rows1)):
            self.comboBox_2.addItem(rows1[i][0])

        #查看未完成维修
        self.addGood.clicked.connect(lambda x: "留给崔凡")

        #故障信息汇总
        self.seeWareHouseInventory.clicked.connect(lambda x: "留给崔凡")

        #查看货柜状态
        self.text_huogui=self.get_CurrentIndex(self.comboBox_2)
        self.seeContainerInventory.clicked.connect(lambda x: "留给崔凡")

        #更改货柜的状态
        self.seeContainerHotGood.clicked.connect(lambda x: "留给崔凡")
    def draw(self):
        # 添加图片时只能用\\或者/，不能直接用filepath
        self.graphicsView_2.setStyleSheet("border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//weixiu.png);")
    def select(self, sql, sql_getColumns):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=password, db=db_name, charset='utf8')
        # 获取数据
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        # 获取列名
        if type(sql_getColumns) == str:
            cursor = conn.cursor()
            cursor.execute(sql_getColumns)
            columns = cursor.fetchall()
            columns = [columns[i][0] for i in range(len(columns))]
            cursor.close()
        if type(sql_getColumns) == list:
            columns = sql_getColumns
        return rows, columns
    def IDU(self, sql):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=password, db=db_name, charset='utf8')
        cursor = conn.cursor()
        # print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Message", "操作成功~", QtWidgets.QMessageBox.Yes)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "Message", "Something Wrong!", QtWidgets.QMessageBox.Yes)
            conn.rollback()
        cursor.close()
        conn.close()

    def get_CurrentText(self, comboBox):
        return comboBox.currentText()

    def get_CurrentIndex(self, comboBox):
        return comboBox.currentIndex()