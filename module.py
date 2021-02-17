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