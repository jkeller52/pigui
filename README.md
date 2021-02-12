# piGUI
piGUI is an open-source automation project meant to enable beginner programmers and hobbyists to turn a Raspberry-Pi into a functional touchscreen that can run programs on either device, or an unlimited number of IoT applications (smart lights, speakers/Spotify API, changing monitor inputs; you could   . Using a few simple python and bash scripts, you can make a multi-page graphical interface.



Examples/Inspiriation


Follow this: 
https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(B)#Image


Then this:
https://www.baldengineer.com/raspberry-pi-gui-tutorial.html

Now, updgrade python setuptools and make sure pip recognizes pyqt5. 
pip3 install --upgrade setuptools
pip3 install pyqt5

#No issues with calibration until this next step. Seems that X-input calibrator is problematic.
Running on Startup:
	https://ozzmaker.com/enable-x-windows-on-piscreen/
  
  
  
  
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
  
  
  
add this below bottom line:
sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
 
@/usr/bin/python3 /home/pi/pigui/init.py


then type:
sudo reboot

Now, gui should autoboot. 

#Note: touchscreen settings worked this time around. 
not sure how to configure this to stay.

#Tested adding '@' before "sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh" in "/etc/xdg/lxsession/LXDE-pi/autostart".
This might have fixed the issue. Rebooting again to see if calibration changes.



to enable ssh from the pi to the computer so we can skip being prompted for a password (allows us to automate some gui functions being performed better):
pi@raspberrypi: ssh-keygen -t rsa
press enter twice to leave password blank

now, you need to copy this key to your main device. I used a Mac OS X device, but ran into several permissions issues on the pi and mac. 
To avoid this, you'll need to change some permissions settings.

On both the pi and other device:
chmod 0700 ~/.ssh


on the mac os x:
sudo chown jacobkeller .ssh
sudo chown jacobkeller .ssh/authorized_keys


Biggest hurdle with pi SSH --> couldn't get permissions set right to allow the ssh key on the macbook to write. 
Error messages i couldn't get past: 
permission denied on authorized_key file
sh: .ssh/authorized_keys: Permission denied --> Indicative of permissions issue on my pi

After this, we will attempt to transfer the ssh key we generated on the pi to the other device:
scp ~/.ssh/id_rsa.pub user@hostname:~/.ssh/authorized_keys

I the following error when attempting to transfer the ssh key:
scp: /Users/jacobkeller/.ssh/authorized_keys: Permission denied
It was indicative of a permissions issue on my Mac for the authorized keys folder, which i resolved with running:
sudo chown jacobkeller .ssh/authorized_keys

Once I did this, the above command worked, trasnferring the ssh key from the pi to the mac, allowing password-less login to my computer from the pi. 




From here, we have to figure out how to send bash commands to your main device (computer) from the functioning gui embedded in the python script. 
now: writing bash script to ssh when a button is pressed
https://stackoverflow.com/questions/13745648/running-bash-script-from-within-python/13745968







Now we need to tell the python script controlling the gui to call the bash script when the button of choice is pressed. For this we'll use subprocess:

Example: 
import subprocess
print "start"
subprocess.call("sleep.sh")
print "end"




Code I used: 
import subprocess
subprocess.call"hdmi.sh")
