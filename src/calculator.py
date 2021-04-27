# -*- coding: UTF-8 -*- 

'''
@File       :   calculator.py
@Time       :   2021-04-26 23:44
@Author     :   wang jun
@Version    :   1.0
@Desc       :   None

'''

from ui.calculator_ui import Ui_MainWindow
from PyQt5 import QtWidgets


class calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 添加事件
        self.ui.btn_0.clicked.connect(self.clicked_btn_0)
        self.ui.btn_1.clicked.connect(self.clicked_btn_1)
        self.ui.btn_2.clicked.connect(self.clicked_btn_2)
        self.ui.btn_3.clicked.connect(self.clicked_btn_3)
        self.ui.btn_4.clicked.connect(self.clicked_btn_4)
        self.ui.btn_5.clicked.connect(self.clicked_btn_5)
        self.ui.btn_6.clicked.connect(self.clicked_btn_6)
        self.ui.btn_7.clicked.connect(self.clicked_btn_7)
        self.ui.btn_8.clicked.connect(self.clicked_btn_8)
        self.ui.btn_9.clicked.connect(self.clicked_btn_9)
        self.ui.btn_percent.clicked.connect(self.clicked_btn_percent)
        self.ui.btn_dot.clicked.connect(self.clicked_btn_dot)
        self.ui.btn_clear.clicked.connect(self.clicked_btn_clear)
        self.ui.btn_add.clicked.connect(self.clicked_btn_add)
        self.ui.btn_subtract.clicked.connect(self.clicked_btn_sub)
        self.ui.btn_multiply.clicked.connect(self.clicked_btn_mult)
        self.ui.btn_devide.clicked.connect(self.clicked_btn_devide)
        self.ui.btn_result.clicked.connect(self.clicked_btn_result)
        self.ui.btn_back.clicked.connect(self.clicked_btn_back)

    def clicked_btn_0(self):
        s = str(self.ui.lineEdit.text())
        if s != '0':
            self.ui.lineEdit.setText(s+"0")

    def clicked_btn_1(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "1")

    def clicked_btn_2(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "2")

    def clicked_btn_3(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "3")

    def clicked_btn_4(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "4")

    def clicked_btn_5(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "5")

    def clicked_btn_6(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "6")

    def clicked_btn_7(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "7")

    def clicked_btn_8(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "8")

    def clicked_btn_9(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "9")

    def clicked_btn_percent(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "/100")

    def clicked_btn_dot(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + ".")

    def clicked_btn_add(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "+")

    def clicked_btn_sub(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "-")

    def clicked_btn_mult(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "*")

    def clicked_btn_devide(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s + "/")

    def clicked_btn_back(self):
        s = str(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(s[:-1])

    def clicked_btn_clear(self):
        self.ui.lineEdit.setText('')

    def clicked_btn_result(self):
        s = str(self.ui.lineEdit.text())
        if s == 'error':
            self.ui.lineEdit.setText('')
        else:
            try:
                self.ui.lineEdit.setText(str(eval(s)))
            except BaseException:
                self.ui.lineEdit.setText('error')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    a = calculator()
    a.show()
    app.exec_()
