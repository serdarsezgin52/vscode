# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableProducts = QtWidgets.QTableWidget(self.centralwidget)
        self.tableProducts.setGeometry(QtCore.QRect(7, 14, 366, 410))
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(392, 24, 225, 258))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lnIsim = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lnIsim.setObjectName("lnIsim")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lnIsim)
        self.lnFiyat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lnFiyat.setObjectName("lnFiyat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lnFiyat)
        self.lblsim = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblsim.setObjectName("lblsim")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblsim)
        self.lblFiyat = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblFiyat.setObjectName("lblFiyat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblFiyat)
        self.btnKaydet = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnKaydet.setObjectName("btnKaydet")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnKaydet)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblsim.setText(_translate("MainWindow", "İsim"))
        self.lblFiyat.setText(_translate("MainWindow", "Fiyat"))
        self.btnKaydet.setText(_translate("MainWindow", "Kaydet"))
