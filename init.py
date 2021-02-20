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
=======

 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedbtnOnplay(self):
        print ("Pressed On!")
        subprocess.call("/home/pi/pigui/pause.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/playbtn.sh") #uncommenting local path to pigui folder enables local gui testing
        #pausebtn.sh works as a play/pause reverse switch

    def pressedbtnOffpause(self):
        print ("Pressed Off!")
        subprocess.call("/home/pi/pigui/pause.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/pausebtn.sh")

    def pressedprevsong(self):
        print ("prevsong pressed")
        subprocess.call("/home/pi/pigui/playprev.sh")
        #applescript/bash to change the song to the previous one (Spotify-based)

    def pressednextsong(self):
        print ("nextsong pressed")
        subprocess.call("/home/pi/pigui/playnext.sh")
        #applescript/bash to change the song to the next one (Spotify-based)

    def pressedDP(self):
        print ("DP")
        subprocess.call("/home/pi/pigui/btn1.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/btn1.sh")

    def pressedHDMI(self):
        print ("HDMI")
        subprocess.call("/home/pi/pigui/btn2.sh")

    def pressedAirPods(self):
        print ("AirPods pressed")
        subprocess.call("/home/pi/pigui/airpods.sh")
        #applescript/bash to change input to airpods
        #these inputs probably still need work

    def pressedFOSI(self):
        print ("FOSI pressed")
        #subprocess.call("/home/pi/pigui/fosi.sh")
        #applescript/bash to change input to fosi audio

    def pressedMute(self):
        #print ("pushButton0 pressed")
        subprocess.call("/home/pi/pigui/Mute.sh")
        #applescript/bash to change input to set audio volume to 0% 

    def pressedVolDown(self):
        #print ("pushButtonVolDown pressed")
        subprocess.call("/home/pi/pigui/VolDown.sh")
        #applescript/bash to change input to decrease audio volume

    def pressedVolUp(self):
        #print ("pushButtonVolUp pressed")
        subprocess.call("/home/pi/pigui/VolUp.sh")
        #applescript/bash to change input to increase audio volume

    def pressedRed(self):
        subprocess.call("/home/pi/pigui/red.sh")

    def pressedOn(self):
        subprocess.call("/home/pi/pigui/on.sh")

    def pressedOff(self):
        subprocess.call("/home/pi/pigui/Off.sh")

    def pressedScene(self):
        subprocess.call("/home/pi/pigui/scene.sh")

    def pressedWhite(self):
        subprocess.call("/home/pi/pigui/white.sh")

    def pressedColour(self):
        subprocess.call("/home/pi/pigui/colour.sh")

    def pressedInput(self):
        print("Input Tab Selected")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        ### Hooks to for buttons
        self.btnOnplay.clicked.connect(lambda: self.pressedbtnOnplay())
        self.btnOffpause.clicked.connect(lambda: self.pressedbtnOffpause())
        self.DP.clicked.connect(lambda: self.pressedDP())
        self.HDMI.clicked.connect(lambda: self.pressedHDMI())
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
>>>>>>> parent of 5138138 (testing using a module for init.py's functions)

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
