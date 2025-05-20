import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from datetime import datetime

# 设置 matplotlib 支持中文
plt.rcParams['font.family'] = ['SimHei']  # 指定支持中文的字体，如 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

class Item(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QtWidgets.QVBoxLayout()

        # 创建 Figure 和 Axes 对象
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # 示例会计日数据
        accounting_dates = ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01']
        dates = [datetime.strptime(date, '%Y-%m-%d') for date in accounting_dates]
        # 示例金额数据
        amounts = [1000, 1200, 1100, 1300, 1400]

        # 绘制折线图
        self.ax.plot(dates, amounts, 'r')

        # 设置 x 轴日期格式
        self.figure.autofmt_xdate()

        # 设置坐标轴标签
        self.ax.set_xlabel('会计日')
        self.ax.set_ylabel('金额')

        # 将画布添加到布局中
        layout.addWidget(self.canvas)

        # 设置布局
        self.setLayout(layout)
        self.setWindowTitle('Matplotlib 折线图')
        self.setGeometry(100, 100, 800, 600)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Item()
    window.show()
    sys.exit(app.exec_())