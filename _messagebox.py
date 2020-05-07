import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _masgboxForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnExit.clicked.connect(self.ShowDialog)

    def ShowDialog(self):
        result = QMessageBox.question(self, "Close Aplication","Are You Sure?",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,QMessageBox.Cancel )
        if result == QMessageBox.Ok:
            print("Yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("No clicked")
    #     msg = QMessageBox()

    #     msg.setWindowTitle("Close Application")
    #     msg.setText("Are You Sure?")
    #     msg.setIcon(QMessageBox.Question)
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
    #     msg.setDefaultButton(QMessageBox.Cancel)
    #     msg.setDetailedText("detaylar.....")
    #     msg.buttonClicked.connect(self.PopupButton)

    #     x =msg.exec_()
    #     print(x)

    # def PopupButton(self, i):
    #     print(i.text())
    #     if i.text() == "OK":
    #         print("Tamam")
    #         QtWidgets.qApp.quit()
    #     elif i.text() == "Cancel":
    #         print("Vazgeç")
    #     elif i.text() == "Ignore":
    #         print("Zorla")


        




        




app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
app()