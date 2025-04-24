from widgets.test_but.test_btn import Ui_Form
from PyQt5.QtWidgets import QWidget,QMessageBox

class Item(Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test_btn)
    def test_btn(self):
        print("test_btn")