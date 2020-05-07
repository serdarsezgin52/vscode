import sys
from PyQt5 import QtWidgets
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo =self.ui.cbSehirler

        # combo.addItem("Ankara")
        # combo.addItem("İstanbul")
        # combo.addItem("İzmir")
        # combo.addItems(["Ordu","Kocaeli","Antalya","Giresun"])
        self.ui.btnLoadItem.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
        self.ui.btnClearItem.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)

    def LoadItems(self):
        sehirler = ["Ordu","Kocaeli","Antalya","Giresun"]

        self.ui.cbSehirler.addItems(sehirler)

    def GetItems(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())

        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))
    
    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def SelectedChangedIndex(self, index):
        print(index)

    def SelectedChangedText(self, text):
        print(text)


        




app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
app()