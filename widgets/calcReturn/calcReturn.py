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
        self.isnew = str(data[13])
        self.ts = str(data[14])

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
        self.profit = ""
        self.real_rate = ""
        self.prd_status = ""
        self.inqCondition_prdName = ""
        self.inqCondition_prdChannel = ""
        self.inqRadioButton_exist = ""
    
    
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
        self.lastCurrentAmt = 0
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
        # 查询数据库
        self.ui.lineEdit_prdName.textChanged.connect(self.doFill)
        # 设置表格选择行为为整行选择
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 绑定点击事件
        self.ui.tableWidget.itemClicked.connect(self.on_table_row_clicked)

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
        self.uiData.profit = self.ui.lineEdit_profit.text().strip()
        self.uiData.real_rate = self.ui.lineEdit_rate.text().strip()
        self.uiData.prd_status = "Y" if self.ui.radioButton_statusY.isChecked() else "N"
        self.uiData.inqCondition_prdName = self.ui.lineEdit_search_condition.text().strip()
        self.uiData.inqCondition_prdChannel = self.ui.lineEdit_search_channel.text().strip()
        self.uiData.inqRadioButton_exist = "Y" if self.ui.radioButton_exist.isChecked() else "N"
   
    def on_table_row_clicked(self, item):
        """表格行点击事件处理函数"""
        row = item.row()
        # 获取该行所有单元格的数据
        row_data = []
        for col in range(self.ui.tableWidget.columnCount()):
            cell_item = self.ui.tableWidget.item(row, col)
            if cell_item:
                row_data.append(cell_item.text())
            else:
                row_data.append("")
        print("选中行的数据:", row_data)
        # 在这里添加你需要执行的操作

    def uiDataCheck(self):
        self.getUiDataVale()
        if self.uiData.current_amt != "" or self.uiData.buy_amt != "" :
            if not self.is_number(self.uiData.buy_amt) or not self.is_number(self.uiData.current_amt):
                QtWidgets.QMessageBox.warning(self, "错误", "输入的金额不是数字")
                return False
        return True
        
    def dbExcute(self, sql):
        try:
            print("执行语句:",sql)
            conn = pymysql.connect(**self.dbConfig)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("执行成功")
            return True
        except Exception as e:
            print("执行失败:", e)
            return False
   
    def dbSearch(self, sql):
        try:
            print("查询语句:",sql)
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
        sql = "select * from invest where prd_name like '%{}%' and prd_channel like '%{}%' and prd_status != 'Y' and isnew='Y'".format(self.uiData.inqCondition_prdName, self.uiData.inqCondition_prdChannel)
        if self.uiData.inqRadioButton_exist == "N":
            sql = "select * from invest where prd_name like '%{}%' and prd_channel like '%{}%' order by ac_date desc".format(self.uiData.inqCondition_prdName, self.uiData.inqCondition_prdChannel)
        data = self.dbSearch(sql)
        self.ui.tableWidget.setRowCount(len(data))
        totalValue, openAmt, closeAmt, profit , status= 0, 0, 0, 0, ""
        today = datetime.date.today()
        for i in range(len(data)):
            item = Invest_dbView(data[i])
            ma_date_obj = datetime.datetime.strptime(item.ma_date, "%Y-%m-%d").date()
            if item.prd_status == "Y":
                status = "已赎回"
            elif ma_date_obj <= today:
                status = "到期可赎"
            else:
                status = "封闭期"
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(status))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(item.prd_name))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(item.prd_channel))
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(item.buy_amt))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(item.current_amt))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(item.real_rate))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(item.profit))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(item.days))
            self.ui.tableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(item.buy_date))
            self.ui.tableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(item.ma_date))
            self.ui.tableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(item.ac_date))
            self.ui.tableWidget.setItem(i, 11, QtWidgets.QTableWidgetItem(item.ts))
            self.ui.tableWidget.setItem(i, 12, QtWidgets.QTableWidgetItem(item.vest_id))
            totalValue += float(item.current_amt)
            profit += float(item.profit)
            if status == "封闭期":
                closeAmt += float(item.current_amt)
            if status == "到期可赎":
                openAmt += float(item.buy_amt)
        if self.uiData.inqRadioButton_exist == "Y":
            self.ui.lineEdit_search_totalValue.setText(str(round(totalValue,2)))
            self.ui.lineEdit_search_openAmt.setText(str(round(openAmt,2)))
            self.ui.lineEdit_search_closeAmt.setText(str(round(closeAmt,2)))
            self.ui.lineEdit_search_profit.setText(str(round(profit,2)))
        else:
            self.ui.lineEdit_search_totalValue.setText("")
            self.ui.lineEdit_search_openAmt.setText("")
            self.ui.lineEdit_search_closeAmt.setText("")
            self.ui.lineEdit_search_profit.setText("")

    def doFill(self):
        self.getUiDataVale()
        sql = "select * from invest where prd_name = '{}' and isnew='Y' limit 1".format(self.uiData.prd_name)
        data = self.dbSearch(sql)
        if len(data) > 0:
            formatResData = Invest_dbView(data[0])
            self.ui.lineEdit_channel.setText(formatResData.prd_channel)
            self.ui.lineEdit_cost.setText(formatResData.buy_amt)
            self.ui.lineEdit_amt.setText(formatResData.current_amt)
            self.ui.dateEdit_maDate.setDate(QDateTime.fromString(formatResData.ma_date, "yyyy-MM-dd").date())
            self.ui.dateEdit_buyDate.setDate(QDateTime.fromString(formatResData.buy_date, "yyyy-MM-dd").date())
            self.ui.dateEdit_acDate.setDate(QDateTime.currentDateTime().date())
            self.ui.radioButton_statusY.setChecked(True) if formatResData.prd_status == "Y" else self.ui.radioButton_statusN.setChecked(True)
            self.lastCurrentAmt = float(formatResData.current_amt)
        else:
            self.ui.lineEdit_channel.setText("")
            self.ui.lineEdit_cost.setText("0")
            self.ui.lineEdit_amt.setText("0")
            self.ui.dateEdit_maDate.setDate(QDateTime.fromString("9999-12-31", "yyyy-MM-dd").date())
            self.ui.dateEdit_buyDate.setDate(QDateTime.currentDateTime().date())
            self.ui.dateEdit_acDate.setDate(QDateTime.currentDateTime().date())
            self.ui.lineEdit_days.setText("0")
            self.ui.lineEdit_profit.setText("0")
            self.ui.lineEdit_rate.setText("0")
            self.ui.radioButton_statusN.setChecked(True)
            self.lastCurrentAmt = 0

    def doDbSave(self):
        self.getUiDataVale()
        if self.uiData.prd_name == "":
            QtWidgets.QMessageBox.information(self, "提示", "请输入产品名称")
            return
        if self.uiDataCheck() == False:
            print("数据校验失败")
            return
        serNewestPrdSql = "select * from invest where prd_name='{}' and buy_date='{}' and isnew='Y'".format(self.uiData.prd_name, self.uiData.buy_date)
        maxPrdAcDate = datetime.datetime.strptime("9999-12-31", "%Y-%m-%d").date()
        newPrdInfo = self.dbSearch(serNewestPrdSql)
        if len(newPrdInfo) > 0:
            # 计算最大的ac_date
            maxPrd = Invest_dbView(newPrdInfo[0])
            maxPrdAcDate = datetime.datetime.strptime(maxPrd.ac_date, "%Y-%m-%d").date()
        # 每个ac_date只允许插入一条
        serPrdSql = "select * from invest where prd_name='{}' and buy_date='{}' and ac_date='{}' limit 1".format(self.uiData.prd_name, self.uiData.buy_date, self.uiData.ac_date)
        prdInfo = self.dbSearch(serPrdSql)
        if len(prdInfo) > 0:
            formatResData = Invest_dbView(prdInfo[0])
            updSql = "update invest set prd_channel='{}',prd_status='{}',buy_amt='{}',ma_date='{}',current_amt='{}',profit='{}',days='{}',real_rate='{}' where vest_id='{}'"
            updSql = updSql.format(self.uiData.prd_channel, self.uiData.prd_status, self.uiData.buy_amt, self.uiData.ma_date, self.uiData.current_amt, self.uiData.profit, self.uiData.days, self.uiData.real_rate, formatResData.vest_id) 
            flg = self.dbExcute(updSql)
            if flg == False:
                QtWidgets.QMessageBox.information(self, "提示", "更新失败")
            else:
                QtWidgets.QMessageBox.information(self, "提示", "更新成功")
        else:
            insSql, isnew = "",""
            maxDate = datetime.datetime.strptime("9999-12-31", "%Y-%m-%d").date()
            if maxPrdAcDate == maxDate:
                isnew = "Y"
            elif maxPrdAcDate < datetime.datetime.strptime(self.uiData.ac_date, "%Y-%m-%d").date():
                isnew = "Y"
                updmaxPrdAcDateSql = "update invest set isnew='N' where prd_name='{}' and buy_date='{}' and isnew='Y'".format(self.uiData.prd_name, self.uiData.buy_date)
                self.dbExcute(updmaxPrdAcDateSql)
            else:
                isnew = "N"
            insSql = "insert into invest (prd_channel,prd_name,prd_status,buy_amt,buy_date,ma_date,ac_date,current_amt,profit,days,real_rate,isnew) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            insSql = insSql.format(self.uiData.prd_channel, self.uiData.prd_name, self.uiData.prd_status, self.uiData.buy_amt, self.uiData.buy_date, self.uiData.ma_date, self.uiData.ac_date, self.uiData.current_amt, self.uiData.profit, self.uiData.days, self.uiData.real_rate,isnew) 
            flg = self.dbExcute(insSql)
            if flg == False:
                QtWidgets.QMessageBox.information(self, "提示", "保存失败")
            else:
                QtWidgets.QMessageBox.information(self, "提示", "保存成功")
        self.doDbSearch()
    
    def calcDays(self):
        self.getUiDataVale()
        days = (datetime.datetime.strptime(self.uiData.ac_date, "%Y-%m-%d") - datetime.datetime.strptime(self.uiData.buy_date, "%Y-%m-%d")).days
        self.ui.lineEdit_days.setText(str(days))
        self.calcProfit()
    
    def calcProfit(self):
        self.getUiDataVale()
        self.ui.lineEdit_lastProfit.setText("0")
        if self.uiData.current_amt != "" and self.uiData.buy_amt != "" and self.is_number(self.uiData.buy_amt) and self.is_number(self.uiData.current_amt):
            current_amt = float(self.uiData.current_amt)
            buy_amt = float(self.uiData.buy_amt)
            days = int(self.uiData.days)
            profit = round(current_amt - buy_amt,2)
            self.ui.lineEdit_profit.setText(str(profit))
            if days == 0 or buy_amt == 0:
                self.ui.lineEdit_rate.setText("0")
                return
            real_rate = round((profit / days * 365) / buy_amt * 100,2)
            self.ui.lineEdit_rate.setText(str(real_rate))
            if self.lastCurrentAmt != 0:
                lastProfit = round(current_amt - self.lastCurrentAmt,2)
                self.ui.lineEdit_lastProfit.setText(str(lastProfit))
        else:
            self.ui.lineEdit_profit.setText("0")
            self.ui.lineEdit_rate.setText("0")
            self.ui.lineEdit_lastProfit.setText("0")
            self.lastCurrentAmt == 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = Item()
    login_window.show()
    sys.exit(app.exec_())