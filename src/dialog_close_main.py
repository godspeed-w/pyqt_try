# -*- coding: UTF-8 -*-

'''
@File       :   calculator.py
@Time       :   2021-04-26 23:44
@Author     :   wang jun
@Version    :   1.0
@Desc       :   None

'''

from ui.dialog_close_main_ui import Ui_Dialog
from PyQt5 import QtWidgets


class dialog_close_main(QtWidgets.QDialog):
    def __init__(self):
        super(dialog_close_main, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 添加事件



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    a = dialog_close_main()
    a.show()
    app.exec_()
