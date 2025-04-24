import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,QTabWidget, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QFileDialog
import json
import importlib

CONFIG = {}
try:
    CONFIG = json.load(open("init.json", "r",encoding="utf-8"))
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

        self.setWindowTitle("mytools")
        self.setGeometry(100, 100, 300, 200)

        menubar = self.menuBar()
        # Help menu
        help_menu = menubar.addMenu("帮助")
        act_about = QAction("关于", self)
        help_menu.addAction(act_about)
        act_about.triggered.connect(self.show_about)
        help_menu.addAction("Exit", self.close)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.initMenu()
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)  # 使标签页可关闭
        self.tab_widget.tabCloseRequested.connect(self.close_current_tab)  # 连接关闭标签页的信号
        self.setCentralWidget(self.tab_widget)

    
    def initMenu(self):
        # 初始化菜单栏
        conf_menubar = CONFIG.get("menubar")
        for item_menu in conf_menubar:
            conf_menu = self.menuBar().addMenu(item_menu["menu"])
            for item_action in item_menu["menuAction"]:
                conf_action = QAction(item_action["action"], self)
                conf_action.triggered.connect(self.add_tabWidget)

    def add_tabWidget(self):
        clicked_action = self.sender().text()
        module_name = findConfigByAction(clicked_action).get("src")
        try:
            metaclass = importlib.import_module(module_name)
            tab = metaclass().Item()
            self.tab_widget.addTab(tab, clicked_action)
            self.tab_widget.setCurrentWidget(tab)
            print("模块导入成功")
        except Exception as e:
            print("导入模块失败:", e)

    def add_tabWidget(self):
        self.tab_widget = QTabWidget()
        # 设置 QTabWidget 为中央部件
        self.setCentralWidget(self.tab_widget)
        # 初始添加一个标签页
        self.add_new_tab()

    def add_new_tab(self):
        new_widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel("这是一个新标签页")
        layout.addWidget(label)
        new_widget.setLayout(layout)
        index = self.tab_widget.addTab(new_widget, f"Tab {self.tab_widget.count() + 1}")
        self.tab_widget.setCurrentIndex(index)

    def close_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index >= 0:
            self.tab_widget.removeTab(current_index)
    def show_about(self):
        QMessageBox.about(self, "About", "This is a simple application.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = MainWindow()
    login_window.show()
    sys.exit(app.exec_())
