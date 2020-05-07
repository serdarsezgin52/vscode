# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_sayi1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi1.setGeometry(QtCore.QRect(111, 92, 47, 14))
        self.lbl_sayi1.setObjectName("lbl_sayi1")
        self.lbl_sayi2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi2.setGeometry(QtCore.QRect(112, 131, 47, 14))
        self.lbl_sayi2.setObjectName("lbl_sayi2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(167, 85, 200, 32))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(166, 124, 200, 32))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(113, 168, 75, 24))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(193, 168, 75, 24))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carmpa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carmpa.setGeometry(QtCore.QRect(272, 168, 75, 24))
        self.btn_carmpa.setObjectName("btn_carmpa")
        self.btn_bolma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolma.setGeometry(QtCore.QRect(351, 168, 75, 24))
        self.btn_bolma.setObjectName("btn_bolma")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(211, 221, 170, 16))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
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
        self.lbl_sayi1.setText(_translate("MainWindow", "Sayı 1"))
        self.lbl_sayi2.setText(_translate("MainWindow", "Sayı 2"))
        self.btn_toplama.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_carmpa.setText(_translate("MainWindow", "Çarpma"))
        self.btn_bolma.setText(_translate("MainWindow", "Bölme"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç"))
