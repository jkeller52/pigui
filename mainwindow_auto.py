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
        MainWindow.resize(320, 480)
        MainWindow.setMaximumSize(QtCore.QSize(320, 480))
        MainWindow.setStyleSheet("border-top-color: rgb(26, 17, 9);\n"
"border-top-color: rgb(4, 51, 255);\n"
"gridline-color: rgba(36, 33, 139, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 291, 391))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("border-color: rgb(84, 150, 227);\n"
"color: rgba(3, 0, 0, 227);\n"
"alternate-background-color: rgb(62, 144, 235);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 212, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOn.setFont(font)
        self.btnOn.setStyleSheet("")
        self.btnOn.setObjectName("btnOn")
        self.horizontalLayout.addWidget(self.btnOn)
        self.btnOff = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOff.setFont(font)
        self.btnOff.setStyleSheet("")
        self.btnOff.setObjectName("btnOff")
        self.horizontalLayout.addWidget(self.btnOff)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 160, 175))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("color: rgb(4, 1, 1);")
        self.btn1.setObjectName("btn1")
        self.verticalLayout.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("color: rgb(9, 5, 3);")
        self.btn2.setObjectName("btn2")
        self.verticalLayout.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("color:rgb(8, 6, 3)")
        self.btn3.setObjectName("btn3")
        self.verticalLayout.addWidget(self.btn3)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action2_0 = QtWidgets.QAction(MainWindow)
        self.action2_0.setObjectName("action2_0")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOn.setText(_translate("MainWindow", "ON"))
        self.btnOff.setText(_translate("MainWindow", "OFF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "On/Off"))
        self.btn1.setText(_translate("MainWindow", "Btn1"))
        self.btn2.setText(_translate("MainWindow", "Btn2"))
        self.btn3.setText(_translate("MainWindow", "Btn3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Btns"))
        self.label.setText(_translate("MainWindow", "piGUI v0.3"))
        self.label_2.setText(_translate("MainWindow", "Page 1"))
        self.action2_0.setText(_translate("MainWindow", "2.0"))
