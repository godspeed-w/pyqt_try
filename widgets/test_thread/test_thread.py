import sys
from PyQt5 import QtWidgets, QtCore, Qt
import threading, time
try:
    from widgets.test_thread.test_thread_ui import Ui_Form
except:
    from test_thread_ui import Ui_Form

class Mysignal(QtCore.QObject):
    text_print = Qt.pyqtSignal(str)

class Item(QtWidgets.QWidget):
    def __init__(self):
        super(Item,self).__init__()
        self.setWindowTitle("Item")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ms = Mysignal()    
        self.ui.pushButton.clicked.connect(self.test_btn)
        self.ms.text_print.connect(self.showMsg)
    

    def test_btn(self):
        def run():
            for i in range(3):
                self.ms.text_print.emit("msg{}".format(i))
                time.sleep(1)
        t = threading.Thread(target=run)
        t.start()

    def showMsg(self, text):
        self.ui.textBrowser.append(str(text))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = Item()
    login_window.show()
    sys.exit(app.exec_())