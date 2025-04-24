import sys
from test_btn_ui import Ui_Form
# from widgets.test_btn.test_btn_ui import Ui_Form
from PyQt5 import QtWidgets

class Item(QtWidgets.QWidget):
    def __init__(self):
        super(Item,self).__init__()
        self.setWindowTitle("Item")
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.test_btn)

    def test_btn(self):
        print("test_btn")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = Item()
    login_window.show()
    sys.exit(app.exec_())