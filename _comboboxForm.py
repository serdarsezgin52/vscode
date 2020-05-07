# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(19, 18, 145, 40))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(183, 19, 192, 28))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(20, 81, 147, 41))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItem.setGeometry(QtCore.QRect(186, 81, 147, 41))
        self.btnLoadItem.setObjectName("btnLoadItem")
        self.btnClearItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearItem.setGeometry(QtCore.QRect(20, 138, 147, 41))
        self.btnClearItem.setObjectName("btnClearItem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 21))
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
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItem.setText(_translate("MainWindow", "Load Item"))
        self.btnClearItem.setText(_translate("MainWindow", "Clear Items"))
