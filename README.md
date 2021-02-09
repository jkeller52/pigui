# pigui


Follow this: 
https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(B)#Image


Then this:
https://www.baldengineer.com/raspberry-pi-gui-tutorial.html

then:
pip3 install --upgrade setuptools
pip3 install pyqt5

#No issues with calibration until this next step. Seems that X-input calibrator is problematic.
Running on Startup:
	https://ozzmaker.com/enable-x-windows-on-piscreen/
  
  
  
  
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
  
  
  
add this below bottom line:
sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
 
@/usr/bin/python3 /home/pi/pigui/init.py


sudo reboot

Now, gui should autoboot. 

#Note: touchscreen settings worked this time around. 
not sure how to configure this to stay.

#Tested adding '@' before "sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh" in "/etc/xdg/lxsession/LXDE-pi/autostart".
This might have fixed the issue. Rebooting again to see if calibration changes.
