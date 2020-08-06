import datetime
import os
import sys
import pymysql
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTableView, QHeaderView, \
    QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from src.stock_ui_window import Ui_stock_ui_window
from src.stock import stock_window
from src.add_good import add_good_window

'''
注意：
    按钮名字，
    搜索“修改”，改成你对应的
'''
# 修改
password = '123'
db_name = 'energystation'

class stock_main_window(QtWidgets.QMainWindow,Ui_stock_ui_window,stock_window,add_good_window):

    def __init__(self):
        super(stock_main_window, self).__init__()
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
        # 采购子界面
        self.stock_window = stock_window()  # 实例化子界面
        self.stock.clicked.connect(self.stock_clicked)  # 槽函数连接

        # 添加商品子界面
        self.add_good_window = add_good_window()  # 实例化子界面
        self.addGood.clicked.connect(self.add_good_clicked)  # 槽函数连接

        # 设置仓库combobox的内容
        rows0=self.select('select 仓库名称 from 仓库',['仓库名称'])[0]
        for i in range(len(rows0)):
            self.comboBox.addItem(rows0[i][0])

        # 设置货柜combobox的内容
        rows1=self.select('select 货柜名称 from 货柜',['货柜名称'])[0]
        for i in range(len(rows1)):
            self.comboBox_2.addItem(rows1[i][0])

        # 设置采购子界面的comboBox:供应商名称
        rows2=self.select('select 供应商名称 from 供应商',['供应商名称'])[0]
        for i in range(len(rows2)):
            self.stock_window.comboBox.addItem(rows2[i][0])

        # 设置采购子界面的comboBox_2:商品名称
        rows3=self.select('select 商品名称 from 商品',['商品名称'])[0]
        for i in range(len(rows3)):
            self.stock_window.comboBox_2.addItem(rows3[i][0])

        # 设置采购子界面的comboBox_3:仓库名称
        rows4=self.select('select 仓库名称 from 仓库',['仓库'])[0]
        for i in range(len(rows4)):
            self.stock_window.comboBox_3.addItem(rows4[i][0])

        # 采购:call stock('2019-12-22 00:01:26','2019-12-30',1,1,40,1,10,2);
        sql="call stock('{}',{},{},{},{},{},{},{});"
        StockAgentID = 1  # 采购员ID       # 修改
        SupplierID = self.get_CurrentIndex(self.stock_window.comboBox)+1
        GoodID = self.get_CurrentIndex(self.stock_window.comboBox_2)+1
        WareHouseID = self.get_CurrentIndex(self.stock_window.comboBox_3)+1
        self.stock_window.stock_btn.clicked.connect(
            lambda x:
            self.IDU(
                # "call stock('2019-12-22 00:01:26','2019-12-30',1,1,160,5,120,2);"
                sql.format(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    self.stock_window.lineEdit.text(),
                    StockAgentID,
                    SupplierID,

                    float(self.stock_window.lineEdit_2.text()),
                    GoodID,
                    int(self.stock_window.lineEdit_4.text()),
                    WareHouseID
                )
            )
        )

        # 添加商品
        sql1 = "call addGood('{}',{},'{}');"
        self.add_good_window.addGood.clicked.connect(
            lambda x:
            self.IDU(
                sql1.format(
                    self.add_good_window.lineEdit.text(),
                    self.add_good_window.lineEdit_1.text(),
                    self.add_good_window.lineEdit_2.text()
                )
            )
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
            select 货柜名称,商品名称,存放数量
            from 货柜,商品,`货柜商品信息`
            where `货柜`.`货柜ID`=`货柜商品信息`.`货柜ID`
            and `货柜商品信息`.`商品ID`=`商品`.`商品ID`
            and `货柜`.`货柜ID`={};
            '''
        sql_getColumns3=['货柜名称', '商品名称','存放数量']
        self.seeContainerInventory.clicked.connect(
            lambda x:
            self.settableWidget(
                2,
                sql3.format(self.get_CurrentIndex(self.comboBox_2)),
                sql_getColumns3
            )
        )

        # 查看货柜的热销商品
        sql4='''
            SELECT 商品.商品名称,SUM(数量*单价) AS 销售额 ,SUM(数量) AS 销售量 FROM 购买明细,购买订单,商品
            WHERE `购买订单`.`货柜ID`={}
            AND `购买明细`.`购买订单ID`=`购买订单`.`购买订单ID`
            AND `购买明细`.`商品ID`=`商品`.`商品ID`
            GROUP BY 商品名称
            ORDER BY 销售额 DESC
            LIMIT 3;
            '''
        sql_getColumns4=['商品名称', '销售额','销售量']
        self.seeContainerHotGood.clicked.connect(
            lambda x:
            self.settableWidget(
                2,
                sql4.format(self.get_CurrentIndex(self.comboBox_2)),
                sql_getColumns4
            )
        )
        # 画图
        filename='ContainerTop3HotGood.png'
        self.seeContainerHotGood.clicked.connect(
            lambda x:
            self.draw(sql4.format(self.get_CurrentIndex(self.comboBox_2)),sql_getColumns4,filename)
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

    def draw(self,sql, sql_getColumns,filename):
        # 获取rows和columns
        rows, columns=self.select(sql, sql_getColumns)
        # print(rows,columns)
        lst_name=[x[0] for x in rows]
        lst_sale = [x[1] for x in rows]
        # lst_sales_volume=[x[2] for x in rows]

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        fig=plt.figure()
        plt.bar(lst_name,lst_sale)
        plt.title(filename[:-4], fontsize=20)
        plt.xticks(lst_name, lst_name, fontsize=15)
        plt.yticks(lst_sale, lst_sale, fontsize=13)

        filepath=os.getcwd()+'\\'+filename
        fig.savefig(filepath, pad_inches=0, transparent=True)  # 去除图片周边空白
        plt.close(fig)

        self.graphicsView.setStyleSheet("border-image: url(D:/Pycharm_Project/SA/{});".format(filename))    # 修改

    def get_CurrentText(self, comboBox):
        return comboBox.currentText()

    def get_CurrentIndex(self, comboBox):
        return comboBox.currentIndex()

    def add_good_clicked(self):
        self.add_good_window.show()

    def stock_clicked(self):
        self.stock_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = stock_main_window()
    window.show()

    sys.exit(app.exec_())
