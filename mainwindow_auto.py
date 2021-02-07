# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 316)
        MainWindow.setMaximumSize(QtCore.QSize(800800, 78978))
        MainWindow.setStyleSheet("background-color: rgb(24, 40, 124);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(230, 20, 221, 221))
        self.toolBox.setMaximumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox.setFont(font)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet("border-color: rgb(15, 84, 244);\n"
"gridline-color: rgb(10, 38, 191);")
        self.toolBox.setObjectName("toolBox")
        self.Inputs = QtWidgets.QWidget()
        self.Inputs.setGeometry(QtCore.QRect(0, 0, 221, 101))
        self.Inputs.setObjectName("Inputs")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Inputs)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 0, 121, 109))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.gridLayout_3.addWidget(self.btn1, 1, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("")
        self.btn2.setObjectName("btn2")
        self.gridLayout_3.addWidget(self.btn2, 2, 0, 1, 1)
        self.toolBox.addItem(self.Inputs, "")
        self.Stocks = QtWidgets.QWidget()
        self.Stocks.setGeometry(QtCore.QRect(0, 0, 221, 101))
        self.Stocks.setObjectName("Stocks")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Stocks)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 0, 181, 87))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btnOff = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.btnOff.setFont(font)
        self.btnOff.setObjectName("btnOff")
        self.gridLayout_5.addWidget(self.btnOff, 2, 0, 1, 1)
        self.btnOn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.btnOn.setFont(font)
        self.btnOn.setObjectName("btnOn")
        self.gridLayout_5.addWidget(self.btnOn, 0, 0, 2, 1)
        self.toolBox.addItem(self.Stocks, "")
        self.nav = QtWidgets.QWidget()
        self.nav.setObjectName("nav")
        self.btn3 = QtWidgets.QPushButton(self.nav)
        self.btn3.setGeometry(QtCore.QRect(20, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.horizontalSlider = QtWidgets.QSlider(self.nav)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 70, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.toolBox.addItem(self.nav, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "Btn1"))
        self.btn2.setText(_translate("MainWindow", "Btn2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Inputs), _translate("MainWindow", "Input"))
        self.btnOff.setText(_translate("MainWindow", "OFF"))
        self.btnOn.setText(_translate("MainWindow", "ON"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Stocks), _translate("MainWindow", "test1"))
        self.btn3.setText(_translate("MainWindow", "Btn3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.nav), _translate("MainWindow", "Nav"))
