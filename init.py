#init.py(main substitute), is basically main 
import sys
import os
import subprocess #for calling bas scripts
import PyQt5 # This gets the Qt stuff for the GUI
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QSlider
from PyQt5.QtCore import pyqtSlot
import mainwindow_auto    # This is our window from QtCreator
import tinytuya
import module
from module import QMainWindow

def __init__(self):
    super(self.__class__, self).__init__()
    self.setupUi(self) # gets defined in the UI file
    ### Hooks to for buttons
    self.btnOnplay.clicked.connect(lambda: self.module(pressedbtnOnplay()))
    self.btnOffpause.clicked.connect(lambda: self.module(pressedbtnOffpause()))
    self.DP.clicked.connect(lambda: self.module(pressedDP()))
    self.HDMI.clicked.connect(lambda: self.module(pressedHDMI()))
    self.AirPods.clicked.connect(lambda: self.pressedAirPods())
    self.FOSI.clicked.connect(lambda: self.pressedFOSI())
    self.VolDown.clicked.connect(lambda: self.pressedVolDown())
    self.VolUp.clicked.connect(lambda: self.pressedVolUp())
    self.Mute.clicked.connect(lambda: self.pressedMute())
    self.nextsong.clicked.connect(lambda: self.pressednextsong())
    self.prevsong.clicked.connect(lambda: self.pressedprevsong())
    self.Red.clicked.connect(lambda: self.pressedRed())
    self.On.clicked.connect(lambda: self.pressedOn())
    self.Off.clicked.connect(lambda: self.pressedOff())
    self.Scene.clicked.connect(lambda: self.pressedScene())
    self.White.clicked.connect(lambda: self.pressedWhite())
    self.Colour.clicked.connect(lambda: self.pressedColour())

        ## Add toolbar and items


#Horizontal Slider
  #  def __init__(self):
   #     super().__init__()

    #    mySlider = QSlider(horizontallider1.Horizontal, self)
    #    mySlider.setGeometry(30, 40, 200, 30)
    #    mySlider.valueChanged[int].connect(self.changeValue)

    #    self.setGeometry(50,50,320,200)
    #    self.setWindowTitle("Checkbox Example")
    #    self.show()

    #def changeValue(self, value):
    #    print(value)


    #toolbox = QToolBox()
     #   layout.addWidget(toolbox, 0, 0)
      #  label = QLabel()
       # toolbox.addItem(label, "Students")
        #label = QLabel()
        #toolbox.addItem(label, "Teachers")
        #label = QLabel()
        #toolbox.addItem(label, "Directors")

def main():
 # a new app instance
 app = QApplication(sys.argv)
 form = MainWindow()
 form.show()
 #without this, the script exits immediately.
 sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
 main()

  # without this, the script exits immediately.



  #error when running on raspberry pi: 
  #qt.qpa.screen: QXcbConnection: Could not connect to display :0.0
  #Could not connect to any X display.

  #solution: https://www.itsolutionstuff.com/post/solved-qxcbconnection-could-not-connect-to-display-wkhtmltopdf-ubuntuexample.html
