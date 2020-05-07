import sys
from PyQt5 import QtWidgets
from _tableForm import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProducts()
        self.ui.btnKaydet.clicked.connect(self.kayitProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(),item.column(),item.text())

    def kayitProduct(self):
        name = self.ui.lnIsim.text()
        price = self.ui.lnFiyat.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            print(rowCount)
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1,QTableWidgetItem(price))


    def loadProducts(self):

        products = [
            {"Name":"Samsung S5","Price": 2000},
            {"Name":"Samsung S6","Price": 3000},
            {"Name":"Samsung S7","Price": 4000},
            {"Name":"Samsung S8","Price": 5000}
            
        ]
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.tableProducts.setColumnWidth(0,150)
        self.ui.tableProducts.setColumnWidth(1,75)

        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(product["Name"]))
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(product["Price"])))
            rowIndex += 1


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
app()