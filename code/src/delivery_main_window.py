import datetime
import os
import sys
import pymysql
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTableView, QHeaderView, \
    QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from src.delivery_ui_window import Ui_delivery_ui_window
from src.delivery import delivery_window

'''
注意：
    按钮名字，
    搜索“修改”，改成你对应的
'''
# 修改
password = '123'
db_name = 'energystation'

class delivery_main_window(QtWidgets.QMainWindow,Ui_delivery_ui_window,delivery_window):

    def __init__(self):
        super(delivery_main_window, self).__init__()
        self.setupUi(self)

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

        '''
        手动新加
        '''
        # 添加图片 -修改
        self.graphicsView.setStyleSheet("border-image: url(C:/Users/Ben/Desktop/xf/facial_emotion_recognition__EMOJIFIER-master/snowman.png);")

        # 采购子界面
        self.delivery_window = delivery_window()  # 实例化子界面
        self.delivery.clicked.connect(self.delivery_clicked)  # 槽函数连接

        # 设置仓库combobox的内容
        rows0=self.select('select 仓库名称 from 仓库',['仓库名称'])[0]
        for i in range(len(rows0)):
            self.comboBox.addItem(rows0[i][0])

        # 设置货柜combobox的内容
        rows1=self.select('select 货柜名称 from 货柜',['货柜名称'])[0]
        for i in range(len(rows1)):
            self.comboBox_2.addItem(rows1[i][0])

        # 设置配送子界面的comboBox:仓库名称
        rows2=self.select('select 仓库名称 from 仓库 ',['仓库名称'])[0]
        for i in range(len(rows2)):
            self.delivery_window.comboBox.addItem(rows2[i][0])

        # 设置配送子界面的comboBox_2:货柜名称
        rows3=self.select('select 货柜名称 from 货柜',['货柜名称'])[0]
        for i in range(len(rows3)):
            self.delivery_window.comboBox_2.addItem(rows3[i][0])

        # 设置配送子界面的comboBox_3:商品名称
        rows4=self.select('select 商品名称 from 商品 ORDER BY 商品ID',['商品名称'])[0]
        for i in range(len(rows4)):
            self.delivery_window.comboBox_3.addItem(rows4[i][0])

        # 配送:-- call delivery(2,4,1,10);
        sql="call delivery({},{},{},{});"
        self.delivery_window.delivery_btn.clicked.connect(
            lambda x: self.peisong(sql)
        )

        # 查看仓库存量
        sql2="call seeWareHouseInventory({})"
        sql_getColumns2=['GoodID', 'Inventory']
        self.seeWareHouseInventory.clicked.connect(
            lambda x:
            self.settableWidget(
                0,
                sql2.format(self.get_CurrentIndex(self.comboBox)),
                sql_getColumns2
            )
        )

        # 查看货柜的商品存量
        sql3='''
            select 商品名称,存放数量
            from 货柜,商品,`货柜商品信息`
            where `货柜`.`货柜ID`=`货柜商品信息`.`货柜ID`
            and `货柜商品信息`.`商品ID`=`商品`.`商品ID`
            and `货柜`.`货柜ID`={};
            '''
        sql_getColumns3=['商品名称','存放数量']
        self.seeContainerInventory.clicked.connect(
            lambda x:
            self.settableWidget(
                2,
                sql3.format(self.get_CurrentIndex(self.comboBox_2)),
                sql_getColumns3
            )
        )


    def peisong(self,sql):

        self.IDU(
            sql.format(
                self.get_CurrentIndex(self.delivery_window.comboBox) + 1,
                self.get_CurrentIndex(self.delivery_window.comboBox_2) + 1,
                self.get_CurrentIndex(self.delivery_window.comboBox_3) + 1,
                int(self.delivery_window.lineEdit.text())))
        self.delivery_window.close()

    def IDU(self, sql):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=password, db=db_name, charset='utf8')
        cursor = conn.cursor()
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            QMessageBox.information(self, "Message", "操作成功~", QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "Message", "Something Wrong!", QMessageBox.Yes)
            conn.rollback()
        cursor.close()
        conn.close()

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

    def settableWidget(self, tableWidgetidx, sql, sql_getColumns):
        # 获取rows和columns
        rows, columns=self.select(sql, sql_getColumns)
        len_x, len_y = len(rows), len(columns)
        # print(rows,columns)
        # 设置table格式
        if tableWidgetidx==0:
            self.tableWidget.clear()
            self.tableWidget.setRowCount(len_x)
            self.tableWidget.setColumnCount(len_y)
            self.tableWidget.setHorizontalHeaderLabels(columns)
            self.tableWidget.setAlternatingRowColors(True)  #行变色
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #列宽适应内容
            # 向table里插入数据
            for i in range(len_x):
                for j in range(len_y):
                    newItem = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget.setItem(i, j, newItem)

        if tableWidgetidx==2:
            self.tableWidget_2.clear()
            self.tableWidget_2.setRowCount(len_x)
            self.tableWidget_2.setColumnCount(len_y)
            self.tableWidget_2.setHorizontalHeaderLabels(columns)
            self.tableWidget_2.setAlternatingRowColors(True)  #行变色
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #列宽适应内容
            # 向table里插入数据
            for i in range(len_x):
                for j in range(len_y):
                    newItem = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget_2.setItem(i, j, newItem)


    # def get_CurrentText(self, comboBox):
    #     return comboBox.currentText()

    def get_CurrentIndex(self, comboBox):
        return comboBox.currentIndex()

    def delivery_clicked(self):
        self.delivery_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = delivery_main_window()
    window.show()

    sys.exit(app.exec_())
