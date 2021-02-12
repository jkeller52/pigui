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
    def pressedOnButton(self):
        print ("Pressed On!")
        subprocess.call("/home/pi/pigui/playbtn.sh")
        #subprocess.call("/users/jacobkeller/documents/github/pigui/playbtn.sh") #uncommenting local path to pigui folder enables local gui testing

    def pressedOffButton(self):
        print ("Pressed Off!")
        #subprocess.call("/home/pi/pigui/playbtn.sh")
        subprocess.call("/users/jacobkeller/documents/github/pigui/pausebtn.sh")

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

    def pressedairpods(self)
        print ("airpods pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to airpods

    def pressedJBL(self)
        print ("jbl pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to JBL Charge 3

    def pressedFOSI(self)
        print ("fosi pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to fosi audio

    def pressedpushButton25(self)
        print ("pushButton25 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to increase audio volume 25%

    def pressedpushButton50(self)
        print ("pushButton50 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to increase audio volume 50%

     def pressedpushButton75(self)
        print ("pushButton75 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to increase audio volume 75%

     def pressedpushButton100(self)
        print ("pushButton100 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to increase audio volume 100%    

     def pressedpushButton0(self)
        print ("pushButton0 pressed")
        #subprocess.call("/home/pi/pigui/***.sh")
        #applescript/bash to change input to set audio volume to 0% 

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        ### Hooks to for buttons
        self.btnOnplay.clicked.connect(lambda: self.pressedOnButton())
        self.btnOffpause.clicked.connect(lambda: self.pressedOffButton())
        self.DP.clicked.connect(lambda: self.pressedDP())
        self.HDMI.clicked.connect(lambda: self.pressedHDMI())
        self.text1.clicked.connect(lambda: self.pressedtext1())
        self.text2.clicked.connect(lambda: self.pressedtext2())
        self.text3.clicked.connect(lambda: self.pressedtext3())
        #saved for texts 3-6
        #
        #
        self.airpods.clicked.connect(lambda: self.airpods())
        self.JBL.clicked.connect(lambda: self.JBL())
        self.FOSI.clicked.connect(lambda: self.FOSI())

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
