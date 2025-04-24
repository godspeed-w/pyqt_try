import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QAction,
    QTabWidget,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
import json
import importlib

CONFIG = {}
try:
    CONFIG = json.load(open("init.json", "r", encoding="utf-8"))
    # print(CONFIG)
except Exception as e:
    print("读取配置文件失败:", e)


def findConfigByAction(action):
    for item_menu in CONFIG.get("menubar"):
        for item_action in item_menu["menuAction"]:
            if item_action["action"] == action:
                return item_action
    return {}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("mytools")

        # 定义menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        help_menu = menubar.addMenu("帮助")
        act_about = QAction("关于", self)
        help_menu.addAction(act_about)
        act_about.triggered.connect(self.show_about)
        help_menu.addAction("Exit", self.close)
        self.initMenu()

        # 定义标签页
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.setTabsClosable(True)  # 使标签页可关闭
        self.tabWidget.tabCloseRequested.connect(self.closeTab)  # 连接关闭标签页的信号

        tab1 = QWidget()
        self.tabWidget.addTab(tab1, "首页")
        self.tabWidget.setLayout(QVBoxLayout())
        tipLable = QLabel(tab1)
        tipLable.setText("这是首页")
        tipLable.move(100, 100)

    def initMenu(self):
        """初始化菜单栏"""
        if CONFIG is None:
            return
        conf_menubar = CONFIG["menubar"]
        for item_menu in conf_menubar:
            conf_menu = self.menuBar().addMenu(item_menu["menu"])
            for item_action in item_menu["menuAction"]:
                conf_action = QAction(item_action["action"], self)
                conf_menu.addAction(conf_action)
                conf_action.triggered.connect(self.add_tabWidget)

    def add_tabWidget(self):
        """添加标签页"""
        clicked_actionName = self.sender().text()
        module_name = findConfigByAction(clicked_actionName).get("src")
        try:
            metaclass = importlib.import_module(module_name)
            tab = metaclass.Item()
            self.tabWidget.addTab(tab, clicked_actionName)
            self.tabWidget.setCurrentWidget(tab)
            print("导入模块成功:", module_name)
        except Exception as e:
            print("导入模块失败:", e)

    def closeTab(self, index):
        """关闭当前标签页"""
        if index != 0:
            self.tabWidget.removeTab(index)

    def show_about(self):
        """显示关于信息"""
        QMessageBox.about(self, "About", "This is a simple application.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    indexWindow = MainWindow()
    indexWindow.show()
    sys.exit(app.exec_())
