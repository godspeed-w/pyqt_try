import sys
import pymysql
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
try:
    from widgets.calcReturn.calcReturn_ui import Ui_Form
except:
    from calcReturn_ui import Ui_Form


class Table_template():
    def __init__(self, data=()):
        self.vest_id = str(data[0])
        self.prd_channel = str(data[1])
        self.prd_name = str(data[2])
        self.prd_rate = str(data[3])
        self.prd_status = str(data[4])
        self.buy_amt = str(data[5])
        self.buy_date = str(data[6])
        self.due_date = str(data[7])
        self.ac_date = str(data[8])
        self.current_amt = str(data[9])
        self.profit = str(data[10])
        self.days = str(data[11])
        self.real_rate = str(data[12])
        self.ts = str(data[13])

    def __str__(self):
        return self.prd_name + " " + str(self.current_amt) + " " + str(self.by_date)

class UiPageData():
    def __init__(self):
        self.prd_name = ""
        self.prd_channel = ""
        self.buy_amt = ""
        self.current_amt = ""
        self.due_date = ""
        self.buy_date = ""
        self.ac_date = ""
        self.prd_status = ""
        self.inqCondition_prdName = ""
        self.inqCondition_prdChannel = ""
    
    
    
class Item(QtWidgets.QWidget):
    def __init__(self):
        super(Item,self).__init__()
        self.setWindowTitle("Item")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.uiData = UiPageData()
        self.dbConfig = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'book_keeping',
            'charset': 'utf8'
        }
        self.ui.dateEdit_valDate.setDateTime(QDateTime.currentDateTime())
        self.ui.pushButton_inquery.clicked.connect(self.doDbSearch)
        self.ui.pushButton_save.clicked.connect(self.doDbSave)

    def getUiDataVale(self):
        self.uiData.prd_name = self.ui.lineEdit_prdName.text()
        self.uiData.prd_channel = self.ui.lineEdit_channel.text()
        self.uiData.buy_amt = self.ui.lineEdit_cost.text()
        self.uiData.current_amt = self.ui.lineEdit_amt.text()
        self.uiData.due_date = self.ui.dateEdit_maDate.date().toString("yyyy-MM-dd")
        self.uiData.buy_date = self.ui.dateEdit_buyDate.date().toString("yyyy-MM-dd")
        self.uiData.ac_date = self.ui.dateEdit_valDate.date().toString("yyyy-MM-dd")
        self.uiData.prd_status = self.ui.radioButton_statusY.text()
        self.uiData.inqCondition_prdName = self.ui.lineEdit_search_condition.text()
        self.uiData.inqCondition_prdChannel = self.ui.lineEdit_search_channel.text()
    

    def dbExcute(self, sql):
        try:
            conn = pymysql.connect(**self.dbConfig)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("执行成功")
        except Exception as e:
            print("执行失败:", e)
   
    
    def dbSearch(self, sql):
        try:
            conn = pymysql.connect(**self.dbConfig)
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.close()
            print("查询到数据量:", len(data))
            return data
        except Exception as e:
            print("查询失败:", e)
            return []
    
    def doDbSearch(self):
        self.getUiDataVale()
        sql = "select * from invest where prd_name like '%{}%' and prd_channel like '%{}%'".format(self.uiData.inqCondition_prdName, self.uiData.inqCondition_prdChannel)
        data = self.dbSearch(sql)
        self.ui.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            item = Table_template(data[i])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(item.prd_status))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item.prd_name))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(item.prd_channel))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(item.buy_amt))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(item.current_amt))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(item.profit))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(item.real_rate))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(item.days))
            self.ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(item.buy_date))
            self.ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(item.due_date))
            self.ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(item.ac_date))
            self.ui.tableWidget.setItem(i, 11, QtWidgets.QTableWidgetItem(item.ts))
            self.ui.tableWidget.setItem(i, 12, QtWidgets.QTableWidgetItem(item.vest_id))


    def doDbSave(self):
        # 计算收益率
        valDate = self.ui.dateEdit_valDate.date().toString("yyyy-MM-dd")
        sql = "select * from invest"
        data = self.dbSearch(sql)
        for i in range(len(data)):
            item = Table_template(data[i])
            if item.ac_date is None:
                item.ac_date = valDate
            
            item.real_rate = item.current_amt / item.buy_amt
            sql = "update invest set ac_date='{}', days={}, real_rate={} where id={}".format(item.ac_date, item.days, item.real_rate, item.vest_id)
            self.dbExcute(sql)
            print(sql)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = Item()
    login_window.show()
    sys.exit(app.exec_())