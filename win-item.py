import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Serdar ilk Pencere")
        self.setGeometry(200,200,700,500)
        self.setToolTip("my tooltip")
        #self.setWindowIcon(QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50,30)
    
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(150,150)
        self.lbl_result.resize(250,50)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.move(150,110)
        self.btn_save.setText("Kaydet")
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText("Ad:  "+ self.txt_name.text() + "  Soyad:  "+ self.txt_surname.text())
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
        
    win.show()
    sys.exit(app.exec_())
window()