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
        MainWindow.resize(320, 460)
        MainWindow.setMaximumSize(QtCore.QSize(320, 460))
        font = QtGui.QFont()
        font.setPointSize(36)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 321, 391))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tabWidget.setStyleSheet("color: rgb(22, 22, 57);")
        self.tabWidget.setObjectName("tabWidget")
        self.MusicTab = QtWidgets.QWidget()
        self.MusicTab.setObjectName("MusicTab")
        self.stackedWidget = QtWidgets.QStackedWidget(self.MusicTab)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 281, 321))
        self.stackedWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.japangif = QtWidgets.QLabel(self.page)
        self.japangif.setGeometry(QtCore.QRect(10, 0, 154, 191))
        self.japangif.setMaximumSize(QtCore.QSize(154, 300))
        self.japangif.setAutoFillBackground(False)
        self.japangif.setLineWidth(2)
        self.japangif.setText("")
        self.japangif.setTextFormat(QtCore.Qt.RichText)
        self.japangif.setPixmap(QtGui.QPixmap("../../../Downloads/gif animations/601d08ef97647985814841.gif"))
        self.japangif.setScaledContents(True)
        self.japangif.setWordWrap(False)
        self.japangif.setOpenExternalLinks(False)
        self.japangif.setObjectName("japangif")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 190, 162, 116))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Playpause = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Playpause.setContentsMargins(0, 0, 0, 0)
        self.Playpause.setObjectName("Playpause")
        self.btnOnplay = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOnplay.setFont(font)
        self.btnOnplay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOnplay.setObjectName("btnOnplay")
        self.Playpause.addWidget(self.btnOnplay)
        self.btnOffpause = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOffpause.setFont(font)
        self.btnOffpause.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOffpause.setObjectName("btnOffpause")
        self.Playpause.addWidget(self.btnOffpause)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(170, 210, 81, 81))
        self.label.setStyleSheet("color: rgb(55, 125, 46);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/file-spotify-logo-png-4_2_150x150_1_50.png"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3.raise_()
        self.label.raise_()
        self.japangif.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton25 = QtWidgets.QPushButton(self.page_2)
        self.pushButton25.setGeometry(QtCore.QRect(0, 130, 61, 51))
        self.pushButton25.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton25.setObjectName("pushButton25")
        self.pushButton_50 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_50.setGeometry(QtCore.QRect(70, 130, 61, 51))
        self.pushButton_50.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_75 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_75.setGeometry(QtCore.QRect(140, 130, 61, 51))
        self.pushButton_75.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_75.setObjectName("pushButton_75")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_2.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton0 = QtWidgets.QPushButton(self.page_2)
        self.pushButton0.setGeometry(QtCore.QRect(50, 70, 171, 61))
        self.pushButton0.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton0.setObjectName("pushButton0")
        self.nextsong = QtWidgets.QPushButton(self.page_2)
        self.nextsong.setGeometry(QtCore.QRect(130, 200, 111, 61))
        self.nextsong.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.nextsong.setObjectName("nextsong")
        self.nextsong_2 = QtWidgets.QPushButton(self.page_2)
        self.nextsong_2.setGeometry(QtCore.QRect(30, 200, 111, 61))
        self.nextsong_2.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.nextsong_2.setObjectName("nextsong_2")
        self.pushButton_100 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_100.setGeometry(QtCore.QRect(210, 130, 61, 51))
        self.pushButton_100.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_100.setObjectName("pushButton_100")
        self.stackedWidget.addWidget(self.page_2)
        self.tabWidget.addTab(self.MusicTab, "")
        self.inputs = QtWidgets.QWidget()
        self.inputs.setObjectName("inputs")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.inputs)
        self.stackedWidget_2.setGeometry(QtCore.QRect(20, 20, 241, 291))
        self.stackedWidget_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 26, 241, 271))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.airpods = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.airpods.setFont(font)
        self.airpods.setStyleSheet("color: rgb(4, 1, 1);")
        self.airpods.setIconSize(QtCore.QSize(32, 32))
        self.airpods.setObjectName("airpods")
        self.verticalLayout_3.addWidget(self.airpods)
        self.jbl = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.jbl.setFont(font)
        self.jbl.setStyleSheet("color: rgb(9, 5, 3);")
        self.jbl.setObjectName("jbl")
        self.verticalLayout_3.addWidget(self.jbl)
        self.fosi = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.fosi.setFont(font)
        self.fosi.setStyleSheet("color: rgb(4, 1, 1);")
        self.fosi.setIconSize(QtCore.QSize(32, 32))
        self.fosi.setObjectName("fosi")
        self.verticalLayout_3.addWidget(self.fosi)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 231, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DP = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        self.DP.setFont(font)
        self.DP.setStyleSheet("color: rgb(4, 1, 1);")
        self.DP.setIconSize(QtCore.QSize(32, 32))
        self.DP.setObjectName("DP")
        self.verticalLayout.addWidget(self.DP)
        self.HDMI = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        self.HDMI.setFont(font)
        self.HDMI.setStyleSheet("color: rgb(9, 5, 3);")
        self.HDMI.setObjectName("HDMI")
        self.verticalLayout.addWidget(self.HDMI)
        self.stackedWidget_2.addWidget(self.page_3)
        self.tabWidget.addTab(self.inputs, "")
        self.Texting = QtWidgets.QWidget()
        self.Texting.setObjectName("Texting")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.Texting)
        self.stackedWidget_4.setGeometry(QtCore.QRect(20, 20, 231, 301))
        self.stackedWidget_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.page_8)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 30, 231, 268))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.text1 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: rgb(4, 1, 1);")
        self.text1.setIconSize(QtCore.QSize(32, 32))
        self.text1.setObjectName("text1")
        self.verticalLayout_7.addWidget(self.text1)
        self.text2 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2.setFont(font)
        self.text2.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2.setObjectName("text2")
        self.verticalLayout_7.addWidget(self.text2)
        self.text3 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.text3.setFont(font)
        self.text3.setStyleSheet("color: rgb(4, 1, 1);")
        self.text3.setIconSize(QtCore.QSize(32, 32))
        self.text3.setObjectName("text3")
        self.verticalLayout_7.addWidget(self.text3)
        self.stackedWidget_4.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.page_9)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 50, 247, 221))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text4 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(80)
        self.text4.setFont(font)
        self.text4.setStyleSheet("color: rgb(4, 1, 1);")
        self.text4.setIconSize(QtCore.QSize(32, 32))
        self.text4.setObjectName("text4")
        self.verticalLayout_6.addWidget(self.text4)
        self.text5 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(80)
        self.text5.setFont(font)
        self.text5.setStyleSheet("color: rgb(9, 5, 3);")
        self.text5.setObjectName("text5")
        self.verticalLayout_6.addWidget(self.text5)
        self.stackedWidget_4.addWidget(self.page_9)
        self.tabWidget.addTab(self.Texting, "")
        self.Shortcuts = QtWidgets.QWidget()
        self.Shortcuts.setObjectName("Shortcuts")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.Shortcuts)
        self.stackedWidget_3.setGeometry(QtCore.QRect(20, 30, 241, 271))
        self.stackedWidget_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.page_5)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 50, 181, 178))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.verticalLayoutWidget_5.setFont(font)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sc1 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(64)
        self.sc1.setFont(font)
        self.sc1.setStyleSheet("color: rgb(4, 1, 1);")
        self.sc1.setIconSize(QtCore.QSize(32, 32))
        self.sc1.setObjectName("sc1")
        self.verticalLayout_4.addWidget(self.sc1)
        self.sc2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(64)
        self.sc2.setFont(font)
        self.sc2.setStyleSheet("color: rgb(9, 5, 3);")
        self.sc2.setObjectName("sc2")
        self.verticalLayout_4.addWidget(self.sc2)
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.page_6)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 50, 231, 277))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sc3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(64)
        self.sc3.setFont(font)
        self.sc3.setStyleSheet("color: rgb(4, 1, 1);")
        self.sc3.setIconSize(QtCore.QSize(32, 32))
        self.sc3.setObjectName("sc3")
        self.verticalLayout_5.addWidget(self.sc3)
        self.sc4 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        self.sc4.setFont(font)
        self.sc4.setStyleSheet("color: rgb(9, 5, 3);")
        self.sc4.setObjectName("sc4")
        self.verticalLayout_5.addWidget(self.sc4)
        self.sc5 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(64)
        self.sc5.setFont(font)
        self.sc5.setStyleSheet("color: rgb(4, 1, 1);")
        self.sc5.setIconSize(QtCore.QSize(32, 32))
        self.sc5.setObjectName("sc5")
        self.verticalLayout_5.addWidget(self.sc5)
        self.stackedWidget_3.addWidget(self.page_6)
        self.tabWidget.addTab(self.Shortcuts, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action2_0 = QtWidgets.QAction(MainWindow)
        self.action2_0.setObjectName("action2_0")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOnplay.setText(_translate("MainWindow", "PLAY"))
        self.btnOffpause.setText(_translate("MainWindow", "PAUSE"))
        self.pushButton25.setText(_translate("MainWindow", "25%"))
        self.pushButton_50.setText(_translate("MainWindow", "50%"))
        self.pushButton_75.setText(_translate("MainWindow", "75%"))
        self.label_2.setText(_translate("MainWindow", "Volume"))
        self.pushButton0.setText(_translate("MainWindow", "0% (off)"))
        self.nextsong.setText(_translate("MainWindow", "Next Song"))
        self.nextsong_2.setText(_translate("MainWindow", "Prev. Song"))
        self.pushButton_100.setText(_translate("MainWindow", "100%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MusicTab), _translate("MainWindow", "Music"))
        self.airpods.setText(_translate("MainWindow", "AirPods"))
        self.jbl.setText(_translate("MainWindow", "JBL"))
        self.fosi.setText(_translate("MainWindow", "FOSI"))
        self.DP.setText(_translate("MainWindow", "DP"))
        self.HDMI.setText(_translate("MainWindow", "HDMI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inputs), _translate("MainWindow", "Inputs"))
        self.text1.setText(_translate("MainWindow", "otw"))
        self.text2.setText(_translate("MainWindow", "call u back"))
        self.text3.setText(_translate("MainWindow", "1sec"))
        self.text4.setText(_translate("MainWindow", "text4"))
        self.text5.setText(_translate("MainWindow", "text5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Texting), _translate("MainWindow", "Texts"))
        self.sc1.setText(_translate("MainWindow", "sc1"))
        self.sc2.setText(_translate("MainWindow", "sc2"))
        self.sc3.setText(_translate("MainWindow", "sc3"))
        self.sc4.setText(_translate("MainWindow", "sc4"))
        self.sc5.setText(_translate("MainWindow", "sc5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Shortcuts), _translate("MainWindow", "Shortcuts"))
        self.action2_0.setText(_translate("MainWindow", "2.0"))
