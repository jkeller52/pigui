#init.py(main substitute), is basically main 
import sys
import os
import subprocess #for calling bas scripts
import PyQt5 # This gets the Qt stuff for the GUI
import mainwindow_auto    # This is our window from QtCreator
import tinytuya
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QSlider
from PyQt5.QtCore import pyqtSlot


#import my functions
#from functions import MainWindow



# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedbtnOnplay(self):
        print ("Pressed On!")
        #subprocess.call("/home/pi/pigui/scripts/bash/pause.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/playbtn.sh") #uncommenting local path to pigui folder enables local gui testing
        #pausebtn.sh works as a play/pause reverse switch

    def pressedbtnOffpause(self):
        print ("Pressed Off!")
        #subprocess.call("/home/pi/pigui/scripts/bash/pause.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/pausebtn.sh")

    def pressedprevsong(self):
        print ("prevsong pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/playprev.sh")
        #applescript/bash to change the song to the previous one (Spotify-based)

    def pressednextsong(self):
        print ("nextsong pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/playnext.sh")
        #applescript/bash to change the song to the next one (Spotify-based)

    def pressedDP(self):
        print ("DP")
        #subprocess.call("/home/pi/pigui/scripts/bash/btn1.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/btn1.sh")

    def pressedHDMI(self):
        print ("HDMI")
        #subprocess.call("/home/pi/pigui/scripts/bash/btn2.sh")

    def pressedAirPods(self):
        print ("AirPods pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/airpods.sh")
        #applescript/bash to change input to airpods
        #these inputs probably still need work

    def pressedFOSI(self):
        print ("FOSI pressed")
        #subprocess.call("/home/pi/pigui/fosi.sh")
        #applescript/bash to change input to fosi audio

    def pressedMute(self):
        print ("pushButton0 pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/Mute.sh")
        #applescript/bash to change input to set audio volume to 0% 

    def pressedVolDown(self):
        print ("pushButtonVolDown pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/VolDown.sh")
        #applescript/bash to change input to decrease audio volume

    def pressedVolUp(self):
        print ("pushButtonVolUp pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/VolUp.sh")
        #applescript/bash to change input to increase audio volume

    def pressedRed(self):
        print ("Red pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/red.sh")

    def pressedOn(self):
        print ("On pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/on.sh")

    def pressedOff(self):
        print ("Off pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/Off.sh")

    def pressedScene(self):
        print ("Scene pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/scene.sh")

    def pressedWhite(self):
        print ("White presesed")
        #subprocess.call("/home/pi/pigui/scripts/bash/white.sh")

    def pressedColour(self):
        print ("Colour pressed")
        #subprocess.call("/home/pi/pigui/scripts/bash/colour.sh")

    def pressedInput(self):
        print("Input Tab Selected")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        ### Hooks for buttons
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
  # without this, the script exits immediately.

def main():
 # a new app instance
 app = QApplication(sys.argv)
 form = MainWindow()
 form.show()
 #without this, the script exits immediately.
 sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
    main()

  #error when running on raspberry pi: 
  #qt.qpa.screen: QXcbConnection: Could not connect to display :0.0
  #Could not connect to any X display.

  #solution: https://www.itsolutionstuff.com/post/solved-qxcbconnection-could-not-connect-to-display-wkhtmltopdf-ubuntuexample.html
