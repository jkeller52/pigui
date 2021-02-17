#module.py
### functions for the buttons to call
def pressedbtnOnplay(self):
	subprocess.call("/home/pi/pigui/pause.sh")

def pressedbtnOffpause(self):
	subprocess.call("/home/pi/pigui/pause.sh")

def pressedprevsong(self):
	subprocess.call("/home/pi/pigui/playprev.sh")

def pressednextsong(self):
	subprocess.call("/home/pi/pigui/playnext.sh")

def pressedDP(self):
	print ("DP")
	subprocess.call("/home/pi/pigui/btn1.sh")

def pressedHDMI(self):
	print ("HDMI")
	subprocess.call("/home/pi/pigui/btn2.sh")

def pressedAirPods(self):
	subprocess.call("/home/pi/pigui/airpods.sh")

def pressedFOSI(self):
	print ("FOSI pressed")

def pressedMute(self):
	subprocess.call("/home/pi/pigui/Mute.sh")

def pressedVolDown(self):
	subprocess.call("/home/pi/pigui/VolDown.sh")

def pressedVolUp(self):
	subprocess.call("/home/pi/pigui/VolUp.sh")

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