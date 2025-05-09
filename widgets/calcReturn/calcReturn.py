import sys
import pymysql
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
try:
    from widgets.calcReturn.calcReturn_ui import Ui_Form
except:
    from calcReturn_ui import Ui_Form


class Invest_dbView():
    def __init__(self, data=()):
        self.vest_id = str(data[0])
        self.prd_channel = str(data[1])
        self.prd_name = str(data[2])
        self.prd_rate = str(data[3])
        self.prd_status = str(data[4])
        self.buy_amt = str(data[5])
        self.buy_date = str(data[6])
        self.ma_date = str(data[7])
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
        self.ma_date = ""
        self.buy_date = ""
        self.ac_date = ""
        self.days = ""
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
        today = QDateTime.currentDateTime()
        self.ui.dateEdit_acDate.setDateTime(today)
        self.ui.dateEdit_buyDate.setDateTime(today)
        # 事件绑定
        self.ui.pushButton_inquery.clicked.connect(self.doDbSearch)
        self.ui.pushButton_save.clicked.connect(self.doDbSave)
        self.ui.dateEdit_buyDate.dateChanged.connect(self.calcDays)
        self.ui.dateEdit_acDate.dateChanged.connect(self.calcDays)
        # 计算收益与收益率
        self.ui.lineEdit_cost.textChanged.connect(self.calcProfit)
        self.ui.lineEdit_amt.textChanged.connect(self.calcProfit)

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def getUiDataVale(self):
        self.uiData.prd_name = self.ui.lineEdit_prdName.text().strip()
        self.uiData.prd_channel = self.ui.lineEdit_channel.text().strip()
        self.uiData.buy_amt = self.ui.lineEdit_cost.text().strip()
        self.uiData.current_amt = self.ui.lineEdit_amt.text().strip()
        self.uiData.ma_date = self.ui.dateEdit_maDate.date().toString("yyyy-MM-dd")
        self.uiData.buy_date = self.ui.dateEdit_buyDate.date().toString("yyyy-MM-dd")
        self.uiData.ac_date = self.ui.dateEdit_acDate.date().toString("yyyy-MM-dd")
        self.uiData.days = self.ui.lineEdit_days.text().strip()
        self.uiData.prd_status = self.ui.radioButton_statusY.text().strip()
        self.uiData.inqCondition_prdName = self.ui.lineEdit_search_condition.text().strip()
        self.uiData.inqCondition_prdChannel = self.ui.lineEdit_search_channel.text().strip()

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
            item = Invest_dbView(data[i])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(item.prd_status))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item.prd_name))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(item.prd_channel))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(item.buy_amt))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(item.current_amt))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(item.profit))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(item.real_rate))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(item.days))
            self.ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(item.buy_date))
            self.ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(item.ma_date))
            self.ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(item.ac_date))
            self.ui.tableWidget.setItem(i, 11, QtWidgets.QTableWidgetItem(item.ts))
            self.ui.tableWidget.setItem(i, 12, QtWidgets.QTableWidgetItem(item.vest_id))

    def doDbSave(self):
        self.getUiDataVale()
        if self.uiData.prd_name == "":
            QtWidgets.QMessageBox.information(self, "提示", "请输入产品名称")
            return
        serSql = "select * from invest where prd_name='{}' and ac_date='{}'".format(self.uiData.prd_name, self.uiData.ac_date)
        data = self.dbSearch(serSql)
        print(data)
        profit = float(self.uiData.current_amt) - float(self.uiData.buy_amt)
        days = (datetime.datetime.strptime(self.uiData.ac_date, "%Y-%m-%d") - datetime.datetime.strptime(self.uiData.buy_date, "%Y-%m-%d")).days
        real_rate = profit / float(self.uiData.buy_amt) * 100
        if len(data) > 0:
            formatResData = Invest_dbView(data[0])
            updSql = "update invest set prd_channel='{}',prd_name='{}',prd_status='{}',buy_amt='{}',buy_date='{}',ma_date='{}',ac_date='{}',current_amt='{}',profit='{}',days='{}',real_rate='{}' where vest_id='{}'"
            updSql = updSql.format(self.uiData.prd_channel, self.uiData.prd_name, self.uiData.prd_status, self.uiData.buy_amt, self.uiData.buy_date, self.uiData.ma_date, self.uiData.ac_date, self.uiData.current_amt, profit, days, real_rate, formatResData.vest_id) 
            self.dbExcute(updSql)
            QtWidgets.QMessageBox.information(self, "提示", "更新成功")
        else:
            insSql = "insert into invest (prd_channel,prd_name,prd_status,buy_amt,buy_date,ma_date,ac_date,current_amt,profit,days,real_rate) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            insSql = insSql.format(self.uiData.prd_channel, self.uiData.prd_name, self.uiData.prd_status, self.uiData.buy_amt, self.uiData.buy_date, self.uiData.ma_date, self.uiData.ac_date, self.uiData.current_amt, profit, days, real_rate) 
            self.dbExcute(insSql)
            QtWidgets.QMessageBox.information(self, "提示", "保存成功")
        self.doDbSearch()
    
    def calcDays(self):
        self.getUiDataVale()
        print(self.uiData.buy_date, self.uiData.ac_date)
        days = (datetime.datetime.strptime(self.uiData.ac_date, "%Y-%m-%d") - datetime.datetime.strptime(self.uiData.buy_date, "%Y-%m-%d")).days
        self.ui.lineEdit_days.setText(str(days))
        self.calcProfit()
    
    def calcProfit(self):
        self.getUiDataVale()
        if self.uiData.current_amt != "" and self.uiData.buy_amt != "":
            if self.is_number(self.uiData.buy_amt) and self.is_number(self.uiData.current_amt):
                current_amt = float(self.uiData.current_amt)
                buy_amt = float(self.uiData.buy_amt)
                days = int(self.uiData.days)
                profit = current_amt - buy_amt
                self.ui.lineEdit_profit.setText(str(profit))
                if days == 0:
                    self.ui.lineEdit_rate.setText("0")
                    return
                real_rate = round((profit / days * 365) / buy_amt,2)
                self.ui.lineEdit_rate.setText(str(real_rate))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = Item()
    login_window.show()
    sys.exit(app.exec_())