# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 320)
        MainWindow.setMaximumSize(QtCore.QSize(460, 320))
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
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 461, 271))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tabWidget.setStyleSheet("color: rgb(22, 22, 57);")
        self.tabWidget.setObjectName("tabWidget")
        self.Lights = QtWidgets.QWidget()
        self.Lights.setObjectName("Lights")
        self.On = QtWidgets.QPushButton(self.Lights)
        self.On.setGeometry(QtCore.QRect(100, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.On.setFont(font)
        self.On.setStyleSheet("color: rgb(9, 5, 3);")
        self.On.setObjectName("On")
        self.Scene = QtWidgets.QPushButton(self.Lights)
        self.Scene.setGeometry(QtCore.QRect(210, 130, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.Scene.setFont(font)
        self.Scene.setStyleSheet("color: rgb(4, 1, 1);")
        self.Scene.setIconSize(QtCore.QSize(32, 32))
        self.Scene.setObjectName("Scene")
        self.Off = QtWidgets.QPushButton(self.Lights)
        self.Off.setGeometry(QtCore.QRect(240, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.Off.setFont(font)
        self.Off.setStyleSheet("color: rgb(9, 5, 3);")
        self.Off.setObjectName("Off")
        self.Red = QtWidgets.QPushButton(self.Lights)
        self.Red.setGeometry(QtCore.QRect(110, 130, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.Red.setFont(font)
        self.Red.setStyleSheet("color: rgb(4, 1, 1);")
        self.Red.setIconSize(QtCore.QSize(32, 32))
        self.Red.setObjectName("Red")
        self.Colour = QtWidgets.QPushButton(self.Lights)
        self.Colour.setGeometry(QtCore.QRect(330, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.Colour.setFont(font)
        self.Colour.setStyleSheet("color: rgb(4, 1, 1);")
        self.Colour.setIconSize(QtCore.QSize(32, 32))
        self.Colour.setObjectName("Colour")
        self.White = QtWidgets.QPushButton(self.Lights)
        self.White.setGeometry(QtCore.QRect(10, 130, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.White.setFont(font)
        self.White.setStyleSheet("color: rgb(4, 1, 1);")
        self.White.setIconSize(QtCore.QSize(32, 32))
        self.White.setObjectName("White")
        self.tabWidget.addTab(self.Lights, "")
        self.MusicTab = QtWidgets.QWidget()
        self.MusicTab.setObjectName("MusicTab")
        self.toolBox_2 = QtWidgets.QToolBox(self.MusicTab)
        self.toolBox_2.setGeometry(QtCore.QRect(20, 10, 411, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox_2.setFont(font)
        self.toolBox_2.setObjectName("toolBox_2")
        self.Controls = QtWidgets.QWidget()
        self.Controls.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.Controls.setObjectName("Controls")
        self.btnOnplay = QtWidgets.QPushButton(self.Controls)
        self.btnOnplay.setGeometry(QtCore.QRect(120, 0, 162, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOnplay.setFont(font)
        self.btnOnplay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOnplay.setObjectName("btnOnplay")
        self.btnOffpause = QtWidgets.QPushButton(self.Controls)
        self.btnOffpause.setGeometry(QtCore.QRect(120, 60, 162, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnOffpause.setFont(font)
        self.btnOffpause.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnOffpause.setObjectName("btnOffpause")
        self.prevsong = QtWidgets.QPushButton(self.Controls)
        self.prevsong.setGeometry(QtCore.QRect(0, 30, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.prevsong.setFont(font)
        self.prevsong.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.prevsong.setObjectName("prevsong")
        self.nextsong = QtWidgets.QPushButton(self.Controls)
        self.nextsong.setGeometry(QtCore.QRect(290, 30, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nextsong.setFont(font)
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
        self.Volume.setGeometry(QtCore.QRect(0, 0, 411, 131))
        self.Volume.setObjectName("Volume")
        self.Mute = QtWidgets.QPushButton(self.Volume)
        self.Mute.setGeometry(QtCore.QRect(200, 30, 171, 61))
        self.Mute.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.Mute.setObjectName("Mute")
        self.VolDown = QtWidgets.QPushButton(self.Volume)
        self.VolDown.setGeometry(QtCore.QRect(40, 60, 131, 71))
        self.VolDown.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.VolDown.setObjectName("VolDown")
        self.VolUp = QtWidgets.QPushButton(self.Volume)
        self.VolUp.setGeometry(QtCore.QRect(40, 0, 131, 71))
        self.VolUp.setStyleSheet("background-color: rgba(43, 43, 43, 194);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.VolUp.setObjectName("VolUp")
        self.toolBox_2.addItem(self.Volume, "")
        self.tabWidget.addTab(self.MusicTab, "")
        self.inputs = QtWidgets.QWidget()
        self.inputs.setObjectName("inputs")
        self.toolBox = QtWidgets.QToolBox(self.inputs)
        self.toolBox.setGeometry(QtCore.QRect(20, 10, 421, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.video = QtWidgets.QWidget()
        self.video.setGeometry(QtCore.QRect(0, 0, 421, 131))
        self.video.setObjectName("video")
        self.DP = QtWidgets.QPushButton(self.video)
        self.DP.setGeometry(QtCore.QRect(30, 0, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.DP.setFont(font)
        self.DP.setStyleSheet("color: rgb(4, 1, 1);")
        self.DP.setIconSize(QtCore.QSize(32, 32))
        self.DP.setObjectName("DP")
        self.HDMI = QtWidgets.QPushButton(self.video)
        self.HDMI.setGeometry(QtCore.QRect(200, 0, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.HDMI.setFont(font)
        self.HDMI.setStyleSheet("color: rgb(9, 5, 3);")
        self.HDMI.setObjectName("HDMI")
        self.toolBox.addItem(self.video, "")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setGeometry(QtCore.QRect(0, 0, 421, 131))
        self.page_10.setObjectName("page_10")
        self.AirPods = QtWidgets.QPushButton(self.page_10)
        self.AirPods.setGeometry(QtCore.QRect(0, 0, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.AirPods.setFont(font)
        self.AirPods.setStyleSheet("color: rgb(4, 1, 1);")
        self.AirPods.setIconSize(QtCore.QSize(32, 32))
        self.AirPods.setObjectName("AirPods")
        self.FOSI = QtWidgets.QPushButton(self.page_10)
        self.FOSI.setGeometry(QtCore.QRect(0, 60, 241, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.FOSI.setFont(font)
        self.FOSI.setStyleSheet("color: rgb(4, 1, 1);")
        self.FOSI.setIconSize(QtCore.QSize(32, 32))
        self.FOSI.setObjectName("FOSI")
        self.toolBox.addItem(self.page_10, "")
        self.tabWidget.addTab(self.inputs, "")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.On.setText(_translate("MainWindow", "On"))
        self.Scene.setText(_translate("MainWindow", "Scene"))
        self.Off.setText(_translate("MainWindow", "Off"))
        self.Red.setText(_translate("MainWindow", "Red"))
        self.Colour.setText(_translate("MainWindow", "Color"))
        self.White.setText(_translate("MainWindow", "White"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Lights), _translate("MainWindow", "Lights"))
        self.btnOnplay.setText(_translate("MainWindow", "PLAY"))
        self.btnOffpause.setText(_translate("MainWindow", "PAUSE"))
        self.prevsong.setText(_translate("MainWindow", "Prev. Song"))
        self.nextsong.setText(_translate("MainWindow", "Next Song"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Controls), _translate("MainWindow", "Controls"))
        self.Mute.setText(_translate("MainWindow", "Mute"))
        self.VolDown.setText(_translate("MainWindow", "Vol. Down"))
        self.VolUp.setText(_translate("MainWindow", "Vol. Up"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.Volume), _translate("MainWindow", "Volume"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MusicTab), _translate("MainWindow", "Music"))
        self.DP.setText(_translate("MainWindow", "DP"))
        self.HDMI.setText(_translate("MainWindow", "HDMI"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.video), _translate("MainWindow", "Video"))
        self.AirPods.setText(_translate("MainWindow", "AirPods"))
        self.FOSI.setText(_translate("MainWindow", "FOSI"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_10), _translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inputs), _translate("MainWindow", "Inputs"))
        self.action2_0.setText(_translate("MainWindow", "2.0"))
