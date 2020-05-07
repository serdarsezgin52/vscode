import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _listForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





        




        




app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
app()