# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 508)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_percent.setObjectName("btn_percent")
        self.gridLayout.addWidget(self.btn_percent, 4, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName("btn_multiply")
        self.gridLayout.addWidget(self.btn_multiply, 0, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_devide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_devide.setObjectName("btn_devide")
        self.gridLayout.addWidget(self.btn_devide, 0, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout.addWidget(self.btn_back)
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setObjectName("btn_subtract")
        self.verticalLayout.addWidget(self.btn_subtract)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setObjectName("btn_result")
        self.verticalLayout.addWidget(self.btn_result)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算器"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_percent.setText(_translate("MainWindow", "%"))
        self.btn_percent.setShortcut(_translate("MainWindow", "%"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_dot.setShortcut(_translate("MainWindow", "."))
        self.btn_multiply.setText(_translate("MainWindow", "X"))
        self.btn_multiply.setShortcut(_translate("MainWindow", "*"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_devide.setText(_translate("MainWindow", "➗"))
        self.btn_devide.setShortcut(_translate("MainWindow", "/"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_clear.setShortcut(_translate("MainWindow", "Shift+C"))
        self.btn_back.setText(_translate("MainWindow", "←"))
        self.btn_back.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_subtract.setText(_translate("MainWindow", "-"))
        self.btn_subtract.setShortcut(_translate("MainWindow", "-"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_add.setShortcut(_translate("MainWindow", "+"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_result.setShortcut(_translate("MainWindow", "Enter"))
