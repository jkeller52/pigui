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
        self.toolBox_2 = QtWidgets.QToolBox(self.MusicTab)
        self.toolBox_2.setGeometry(QtCore.QRect(0, 20, 311, 311))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox_2.setFont(font)
        self.toolBox_2.setObjectName("toolBox_2")
        self.Controls = QtWidgets.QWidget()
        self.Controls.setGeometry(QtCore.QRect(0, 0, 311, 231))
        self.Controls.setObjectName("Controls")
        self.btnOnplay = QtWidgets.QPushButton(self.Controls)
        self.btnOnplay.setGeometry(QtCore.QRect(80, 0, 162, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOnplay.setFont(font)
        self.btnOnplay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOnplay.setObjectName("btnOnplay")
        self.btnOffpause = QtWidgets.QPushButton(self.Controls)
        self.btnOffpause.setGeometry(QtCore.QRect(80, 140, 162, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOffpause.setFont(font)
        self.btnOffpause.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOffpause.setObjectName("btnOffpause")
        self.prevsong = QtWidgets.QPushButton(self.Controls)
        self.prevsong.setGeometry(QtCore.QRect(0, 70, 111, 61))
        self.prevsong.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.prevsong.setObjectName("prevsong")
        self.nextsong = QtWidgets.QPushButton(self.Controls)
        self.nextsong.setGeometry(QtCore.QRect(200, 70, 111, 61))
        self.nextsong.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.nextsong.setObjectName("nextsong")
        self.label = QtWidgets.QLabel(self.Controls)
        self.label.setGeometry(QtCore.QRect(120, 60, 81, 81))
        self.label.setStyleSheet("color: rgb(55, 125, 46);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/file-spotify-logo-png-4_2_150x150_1_50.png"))
        self.label.setObjectName("label")
        self.toolBox_2.addItem(self.Controls, "")
        self.Volume = QtWidgets.QWidget()
        self.Volume.setGeometry(QtCore.QRect(0, 0, 311, 231))
        self.Volume.setObjectName("Volume")
        self.pushButton0 = QtWidgets.QPushButton(self.Volume)
        self.pushButton0.setGeometry(QtCore.QRect(20, 10, 171, 61))
        self.pushButton0.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton0.setObjectName("pushButton0")
        self.pushButton25 = QtWidgets.QPushButton(self.Volume)
        self.pushButton25.setGeometry(QtCore.QRect(0, 80, 61, 51))
        self.pushButton25.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton25.setObjectName("pushButton25")
        self.pushButton50 = QtWidgets.QPushButton(self.Volume)
        self.pushButton50.setGeometry(QtCore.QRect(50, 80, 61, 51))
        self.pushButton50.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton50.setObjectName("pushButton50")
        self.pushButton75 = QtWidgets.QPushButton(self.Volume)
        self.pushButton75.setGeometry(QtCore.QRect(100, 80, 61, 51))
        self.pushButton75.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton75.setObjectName("pushButton75")
        self.pushButton100 = QtWidgets.QPushButton(self.Volume)
        self.pushButton100.setGeometry(QtCore.QRect(150, 80, 61, 51))
        self.pushButton100.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton100.setObjectName("pushButton100")
        self.japangif = QtWidgets.QLabel(self.Volume)
        self.japangif.setGeometry(QtCore.QRect(210, 0, 101, 251))
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
        self.toolBox_2.addItem(self.Volume, "")
        self.tabWidget.addTab(self.MusicTab, "")
        self.inputs = QtWidgets.QWidget()
        self.inputs.setObjectName("inputs")
        self.toolBox = QtWidgets.QToolBox(self.inputs)
        self.toolBox.setGeometry(QtCore.QRect(10, 30, 291, 291))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.video = QtWidgets.QWidget()
        self.video.setGeometry(QtCore.QRect(0, 0, 291, 211))
        self.video.setObjectName("video")
        self.DP = QtWidgets.QPushButton(self.video)
        self.DP.setGeometry(QtCore.QRect(60, 0, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.DP.setFont(font)
        self.DP.setStyleSheet("color: rgb(4, 1, 1);")
        self.DP.setIconSize(QtCore.QSize(32, 32))
        self.DP.setObjectName("DP")
        self.HDMI = QtWidgets.QPushButton(self.video)
        self.HDMI.setGeometry(QtCore.QRect(60, 100, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.HDMI.setFont(font)
        self.HDMI.setStyleSheet("color: rgb(9, 5, 3);")
        self.HDMI.setObjectName("HDMI")
        self.toolBox.addItem(self.video, "")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setGeometry(QtCore.QRect(0, 0, 291, 211))
        self.page_10.setObjectName("page_10")
        self.AirPods = QtWidgets.QPushButton(self.page_10)
        self.AirPods.setGeometry(QtCore.QRect(20, 0, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.AirPods.setFont(font)
        self.AirPods.setStyleSheet("color: rgb(4, 1, 1);")
        self.AirPods.setIconSize(QtCore.QSize(32, 32))
        self.AirPods.setObjectName("AirPods")
        self.FOSI = QtWidgets.QPushButton(self.page_10)
        self.FOSI.setGeometry(QtCore.QRect(20, 60, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.FOSI.setFont(font)
        self.FOSI.setStyleSheet("color: rgb(4, 1, 1);")
        self.FOSI.setIconSize(QtCore.QSize(32, 32))
        self.FOSI.setObjectName("FOSI")
        self.JBL = QtWidgets.QPushButton(self.page_10)
        self.JBL.setGeometry(QtCore.QRect(20, 120, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.JBL.setFont(font)
        self.JBL.setStyleSheet("color: rgb(9, 5, 3);")
        self.JBL.setObjectName("JBL")
        self.toolBox.addItem(self.page_10, "")
        self.tabWidget.addTab(self.inputs, "")
        self.Texting = QtWidgets.QWidget()
        self.Texting.setObjectName("Texting")
        self.toolBox_3 = QtWidgets.QToolBox(self.Texting)
        self.toolBox_3.setGeometry(QtCore.QRect(0, 0, 311, 331))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox_3.setFont(font)
        self.toolBox_3.setObjectName("toolBox_3")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 311, 211))
        self.page_3.setObjectName("page_3")
        self.text1 = QtWidgets.QPushButton(self.page_3)
        self.text1.setGeometry(QtCore.QRect(10, 30, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: rgb(4, 1, 1);")
        self.text1.setIconSize(QtCore.QSize(32, 32))
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QPushButton(self.page_3)
        self.text2.setGeometry(QtCore.QRect(10, 120, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2.setFont(font)
        self.text2.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2.setObjectName("text2")
        self.text3 = QtWidgets.QPushButton(self.page_3)
        self.text3.setGeometry(QtCore.QRect(160, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text3.setFont(font)
        self.text3.setStyleSheet("color: rgb(4, 1, 1);")
        self.text3.setIconSize(QtCore.QSize(32, 32))
        self.text3.setObjectName("text3")
        self.toolBox_3.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 311, 211))
        self.page_4.setObjectName("page_4")
        self.text2_2 = QtWidgets.QPushButton(self.page_4)
        self.text2_2.setGeometry(QtCore.QRect(10, 80, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2_2.setFont(font)
        self.text2_2.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2_2.setObjectName("text2_2")
        self.text1_2 = QtWidgets.QPushButton(self.page_4)
        self.text1_2.setGeometry(QtCore.QRect(10, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.text1_2.setFont(font)
        self.text1_2.setStyleSheet("color: rgb(4, 1, 1);")
        self.text1_2.setIconSize(QtCore.QSize(32, 32))
        self.text1_2.setObjectName("text1_2")
        self.text3_2 = QtWidgets.QPushButton(self.page_4)
        self.text3_2.setGeometry(QtCore.QRect(130, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text3_2.setFont(font)
        self.text3_2.setStyleSheet("color: rgb(4, 1, 1);")
        self.text3_2.setIconSize(QtCore.QSize(32, 32))
        self.text3_2.setObjectName("text3_2")
        self.text2_3 = QtWidgets.QPushButton(self.page_4)
        self.text2_3.setGeometry(QtCore.QRect(10, 140, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2_3.setFont(font)
        self.text2_3.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2_3.setObjectName("text2_3")
        self.toolBox_3.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.text2_7 = QtWidgets.QPushButton(self.page_5)
        self.text2_7.setGeometry(QtCore.QRect(20, 70, 221, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2_7.setFont(font)
        self.text2_7.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2_7.setObjectName("text2_7")
        self.text3_5 = QtWidgets.QPushButton(self.page_5)
        self.text3_5.setGeometry(QtCore.QRect(20, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text3_5.setFont(font)
        self.text3_5.setStyleSheet("color: rgb(4, 1, 1);")
        self.text3_5.setIconSize(QtCore.QSize(32, 32))
        self.text3_5.setObjectName("text3_5")
        self.text2_8 = QtWidgets.QPushButton(self.page_5)
        self.text2_8.setGeometry(QtCore.QRect(20, 130, 221, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.text2_8.setFont(font)
        self.text2_8.setStyleSheet("color: rgb(9, 5, 3);")
        self.text2_8.setObjectName("text2_8")
        self.toolBox_3.addItem(self.page_5, "")
        self.tabWidget.addTab(self.Texting, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action2_0 = QtWidgets.QAction(MainWindow)
        self.action2_0.setObjectName("action2_0")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.toolBox_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOnplay.setText(_translate("MainWindow", "PLAY"))
        self.btnOffpause.setText(_translate("MainWindow", "PAUSE"))
        self.prevsong.setText(_translate("MainWindow", "Prev. Song"))
        self.nextsong.setText(_translate("MainWindow", "Next Song"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Controls), _translate("MainWindow", "Controls"))
        self.pushButton0.setText(_translate("MainWindow", "0% (off)"))
        self.pushButton25.setText(_translate("MainWindow", "25%"))
        self.pushButton50.setText(_translate("MainWindow", "50%"))
        self.pushButton75.setText(_translate("MainWindow", "75%"))
        self.pushButton100.setText(_translate("MainWindow", "100%"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Volume), _translate("MainWindow", "Volume"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MusicTab), _translate("MainWindow", "Music"))
        self.DP.setText(_translate("MainWindow", "DP"))
        self.HDMI.setText(_translate("MainWindow", "HDMI"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.video), _translate("MainWindow", "Video"))
        self.AirPods.setText(_translate("MainWindow", "AirPods"))
        self.FOSI.setText(_translate("MainWindow", "FOSI"))
        self.JBL.setText(_translate("MainWindow", "JBL"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_10), _translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inputs), _translate("MainWindow", "Inputs"))
        self.text1.setText(_translate("MainWindow", "otw"))
        self.text2.setText(_translate("MainWindow", "call u back"))
        self.text3.setText(_translate("MainWindow", "1sec"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_3), _translate("MainWindow", "To Alex"))
        self.text2_2.setText(_translate("MainWindow", "call u back"))
        self.text1_2.setText(_translate("MainWindow", "otw"))
        self.text3_2.setText(_translate("MainWindow", "1sec"))
        self.text2_3.setText(_translate("MainWindow", "box in 30?"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_4), _translate("MainWindow", "To Tyler"))
        self.text2_7.setText(_translate("MainWindow", "call u back"))
        self.text3_5.setText(_translate("MainWindow", "1sec"))
        self.text2_8.setText(_translate("MainWindow", "in class"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_5), _translate("MainWindow", "To Aaron"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Texting), _translate("MainWindow", "Texts"))
        self.action2_0.setText(_translate("MainWindow", "2.0"))
