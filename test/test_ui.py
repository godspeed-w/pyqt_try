# -*- coding: UTF-8 -*- 

'''
@File       :   test_ui.py
@Time       :   2021-04-27 10:10
@Author     :   wang jun
@Version    :   1.0
@Desc       :   None

'''
from PySide2 import QtWidgets,QtCore
from PySide2.QtUiTools import QUiLoader
from src.calculator import calculator
import os,sys
from ui.calculator_ui import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)





if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    homePage = Main()
    homePage.show()
    app.exec_()
