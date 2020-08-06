import os
import sys

import numpy as np
import pymysql
from PyQt5.QtGui import QImage, QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTableView, QHeaderView, \
    QPushButton, QGraphicsScene, QGraphicsView
from PyQt5 import QtCore, QtGui, QtWidgets
from src.finance_ui_window import Ui_finance_ui_window
import matplotlib.pyplot as plt

# 修改
password = '123'
db_name = 'energystation'

class finance_main_window(QtWidgets.QMainWindow, Ui_finance_ui_window):

    def __init__(self):
        super(finance_main_window, self).__init__()
        self.setupUi(self)
        self.graphicsView_2.setStyleSheet(
            "border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//caiwu.png);")

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

        # 设置combobox的内容
        rows0=self.select('select 货柜名称 from 货柜',['货柜名称'])[0]
        for i in range(len(rows0)):
            self.comboBox.addItem(rows0[i][0])

        # # 查看总销售额
        # sql='call seeTotalSales'
        # sql_getColumns=['TotalSales']   #即使是一个列名，也要用list格式而非str
        # self.seeTotalSales.clicked.connect(lambda x: self.settableWidget(sql, sql_getColumns))

        # 按月份查看销售额
        sql='call seeContainerMonthSales()'
        sql_getColumns=['月份','月份总销售额']   #即使是一个列名，也要用list格式而非str
        self.seeContainerMonthSales.clicked.connect(lambda x: self.settableWidget(sql, sql_getColumns))
        # 画图
        filename='ContainerMonthSales.png'
        self.seeContainerMonthSales.clicked.connect(
            lambda x:
            self.draw(sql,sql_getColumns,filename)
        )

        # 查看货柜的销售额
        sql1 = 'call seeContainerSales({});'
        sql_getColumns1 =['ContainerID', 'ContainerSales']  #因为是生成表，所以同样不能用sql获取列名
        self.seeContainerSales.clicked.connect(
            lambda x: self.settableWidget(sql1.format(
                self.get_CurrentIndex(self.comboBox)
            ),
                sql_getColumns1)
        )
        # 画图
        filename1='ContainerSale.png'
        self.seeContainerSales.clicked.connect(
            lambda x:
            self.draw(sql1.format(self.get_CurrentIndex(self.comboBox)),sql_getColumns1,filename1)
        )

        # 查看货柜的商品销售额
        sql2 = 'call seeContainerGoodSales({})'
        sql_getColumns2 = ['GoodID', 'ContainerGoodSales', '销售额','销售量']
        self.seeContainerGoodSales.clicked.connect(
            lambda x:
            self.settableWidget(sql2.format(self.get_CurrentIndex(self.comboBox)),sql_getColumns2),
        )
        # 画图
        filename2='ContainerGoodSale.png'
        self.seeContainerGoodSales.clicked.connect(
            lambda x:
            self.draw(sql2.format(self.get_CurrentIndex(self.comboBox)),sql_getColumns2,filename2)
        )

        # 查看商品的销售额
        sql3 = 'call seeGoodSales'
        sql_getColumns3 = ['GoodID', 'GoodSales']
        self.seeGoodSales.clicked.connect(lambda x: self.settableWidget(sql3, sql_getColumns3))


    def select(self, sql, sql_getColumns):
        # print('select: ',sql)
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

    def settableWidget(self,sql, sql_getColumns):
        # 获取rows和columns
        rows, columns=self.select(sql, sql_getColumns)
        len_x, len_y = len(rows), len(columns)
        # 设置table格式
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

    def draw(self,sql, sql_getColumns,filename):
        # 获取rows和columns
        rows, columns=self.select(sql, sql_getColumns)
        # print(rows,columns)
        if filename=='ContainerSale.png':
            lst_name =['ContainerSale']
            lst_sale=[x[1] for x in rows]
            if lst_sale[0]==None:
                lst_sale[0]=0
        if filename=='ContainerGoodSale.png':
            lst_name = [x[1] for x in rows]
            lst_sale = [x[2] for x in rows]
        if filename =='ContainerMonthSales.png':
            lst_name = [x[0] for x in rows]
            lst_sale = [x[1] for x in rows]

        #计算y轴刻度
        if len(lst_sale)==0:
            y_ticks=[0]
        else:
            if filename=='ContainerSale.png':
                y_ticks=[max(lst_sale)]
            else:
                y_ticks = [round(x, 2) for x in np.linspace(0, max(lst_sale) * 6 / 5, 5)]


        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        fig=plt.figure()
        plt.bar(lst_name,lst_sale,color='#FF7F0E')
        plt.title(filename[:-4],fontsize =15)
        plt.xticks(lst_name, fontsize =12)
        plt.yticks(y_ticks, fontsize =13)
        plt.xticks(rotation=12)

        if filename == 'ContainerSale.png':
            line_y = self.select("select avg(货柜销售额) from (select 货柜.货柜名称,SUM(单价*数量) AS 货柜销售额 from 商品,购买订单,购买明细,货柜 where `购买订单`.`购买订单ID`=`购买明细`.`购买订单ID` and `购买明细`.`商品ID`=`商品`.`商品ID` and `购买订单`.`货柜ID`=`货柜`.`货柜ID` GROUP BY 货柜.货柜ID) as a ;"
                               , ['货柜销售额']
                               )[0][0]
            plt.hlines(line_y, -3, 3,color="blue",linestyles='-.') #横线
            plt.text(-3, line_y[0], round(line_y[0],2), fontsize=15)

        filepath=os.getcwd()+'\\'+filename  # 第一个\是转义，filepath为：D:\Pycharm_Project\SA\***.png
        fig.savefig(filepath, pad_inches=0.5, transparent=True)  # 去除图片周边空白
        plt.close(fig)

        # 添加图片时只能用\\或者/，不能直接用filepath
        self.graphicsView.setStyleSheet("border-image: url(C:/Users/Ben/Desktop/xf/facial_emotion_recognition__EMOJIFIER-master/src/{});".format(filename))


    def get_CurrentText(self, comboBox):
        return comboBox.currentText()

    def get_CurrentIndex(self, comboBox):
        return comboBox.currentIndex()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = finance_main_window()
    window.show()

    sys.exit(app.exec_())


