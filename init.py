#init.py(main substitute), is basically main 
# always seem to need this
import sys
import os
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from PyQt5.QtCore import pyqtSlot

# This is our window from QtCreator
import mainwindow_auto

#now, how do I execute ssh commands...
import paramiko

hostname = "@jacobs-mbp.wowway.com"
username = "jacobkeller"
password = "1943"
#now what...



 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")

    def pressedbtn1(self):
        print ("Button1")
        #subprocess.run(["ssh jacobkeller@jacobs-mbp.wowway.com python -u - < hdmi1.py"])

    def pressedbtn2(self):
        print ("Button2")

    def pressedbtn3(self):
        print ("Button3")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        ### Hooks to for buttons
        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())
        self.btn1.clicked.connect(lambda: self.pressedbtn1())
        self.btn2.clicked.connect(lambda: self.pressedbtn2())
        self.btn3.clicked.connect(lambda: self.pressedbtn3())
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