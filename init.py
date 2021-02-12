#init.py(main substitute), is basically main 

import sys
import os
import subprocess #for calling bas scripts
import PyQt5 # This gets the Qt stuff for the GUI
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from PyQt5.QtCore import pyqtSlot
import mainwindow_auto    # This is our window from QtCreator

 
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
        #print ("Pressed Off!")
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

    def pressedtext1(self):
        print ("text 1 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")

    def pressedtext2(self):
        print ("text 2 pressed")
       #subprocess.call("/home/pi/pigui/***.sh")

    def pressedtext3(self):
        print ("text 3 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")

    def pressedAirPods(self):
        print ("AirPods pressed")
        subprocess.call("/home/pi/pigui/airpods.sh")
        #applescript/bash to change input to airpods
        #these inputs probably still need work

    def pressedJBL(self):
        print ("JBL pressed")
        subprocess.call("/home/pi/pigui/jbl.sh")
        #applescript/bash to change input to JBL Charge 3

    def pressedFOSI(self):
        print ("FOSI pressed")
        #subprocess.call("/home/pi/pigui/fosi.sh")
        #applescript/bash to change input to fosi audio

    def pressedMute(self):
        #print ("pushButton0 pressed")
        subprocess.call("/home/pi/pigui/pushButton0.sh")
        #applescript/bash to change input to set audio volume to 0% 

    def pressedpushButtonVolDown(self):
        #print ("pushButtonVolDown pressed")
        subprocess.call("/home/pi/pigui/pushButtonVolDown.sh")
        #applescript/bash to change input to decrease audio volume

    def pressedpushButtonVolUp(self):
        #print ("pushButtonVolUp pressed")
        subprocess.call("/home/pi/pigui/pushButtonVolUp.sh")
        #applescript/bash to change input to increase audio volume


    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        ### Hooks to for buttons
        self.btnOnplay.clicked.connect(lambda: self.pressedbtnOnplay())
        self.btnOffpause.clicked.connect(lambda: self.pressedbtnOffpause())
        self.DP.clicked.connect(lambda: self.pressedDP())
        self.HDMI.clicked.connect(lambda: self.pressedHDMI())
        self.text1.clicked.connect(lambda: self.pressedtext1())
        self.text2.clicked.connect(lambda: self.pressedtext2())
        self.text3.clicked.connect(lambda: self.pressedtext3())
        self.AirPods.clicked.connect(lambda: self.pressedAirPods())
        self.JBL.clicked.connect(lambda: self.pressedJBL())
        self.FOSI.clicked.connect(lambda: self.pressedFOSI())
        self.pushButtonVolDown.clicked.connect(lambda: self.pressedpushButtonVolDown())
        self.pushButtonVolUp.clicked.connect(lambda: self.pressedpushButtonVolUp()
        self.Mute.clicked.connect(lambda: self.pressedMute())
        self.nextsong.clicked.connect(lambda: self.pressednextsong())
        self.prevsong.clicked.connect(lambda: self.pressedprevsong())
        ## Add toolbar and items
        
    def pressedInput(self):
    	print("Input Tab Selected")

    def pressedtest1(self):
    	print('test1 tab selected')


    #toolbox = QToolBox()
     #   layout.addWidget(toolbox, 0, 0)
      #  label = QLabel()
       # toolbox.addItem(label, "Students")
        #label = QLabel()
        #toolbox.addItem(label, "Teachers")
        #label = QLabel()
        #toolbox.addItem(label, "Directors")

 
# I feel better having one of these
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
