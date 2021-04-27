# -*- coding: UTF-8 -*- 

'''
@File       :   main.py
@Time       :   2021-04-26 23:03
@Author     :   wang jun
@Version    :   1.0
@Desc       :   None

'''
import sys

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

from src.calculator import calculator
from ui import index_ui


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = index_ui.Ui_mainWindow()
        self.ui.setupUi(self)

        self.allwindows = []
        self.ui.btn_calculator.clicked.connect(self.createWindow)
        self.ui.btn_color.clicked.connect(self.noDone)
        self.ui.btn_dataset.clicked.connect(self.noDone)

    # 未完成
    def noDone(self):
        QMessageBox.question(self, "message", "该功能尚未实现...", QMessageBox.Yes,
                             QMessageBox.Yes)

    # 创建子窗口
    def createWindow(self):
        self.allwindows.append(calculator())
        self.allwindows[-1].show()

    # 推出前询问
    def closeEvent(self, event):
        print("退出前还有窗口{}".format(len(self.allwindows)))
        if len(self.allwindows) != 0:
            reply = QMessageBox.question(self, "常用软件集合", "还有程序尚未退出，是否要退出主程序？", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                sys.exit(0)
            else:
                event.ignore()

    # 轮询检测子窗口是否关闭(未实现)
    # def set_interval(self):
    #     timer_online = threading.Timer(3, self.set_interval)
    #     timer_online.start()
    #     print("轮询")
    #     # calculator().close()
    #     for window in self.allwindows:
    #         if window is None:
    #             print("guanbi")
    #             self.allwindows.remove(window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    homePage = Main()
    # homePage.set_interval()
    homePage.show()
    sys.exit(app.exec_())
