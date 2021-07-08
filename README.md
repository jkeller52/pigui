# piGUI
piGUI is an open-source automation project meant to enable beginner programmers and hobbyists to turn a Raspberry-Pi into a touchscreen Graphical User Interface (GUI) that can run control various IoT devices (smart lights, speakers/Spotify API, changing monitor inputs, etc). 

Using a few simple python and bash scripts, you can make a multi-page graphical interface using PyQt5, a variant of Qt Creator GUI software. This tutorial will use PyQt5 to generate boilerplate code for GUI elements, perfect for reducing load on beginner programmers interested in simple GUI applicatitons. 


A 3.5" Waveshare TFT LCD Touchscreen is connected to a Raspberry Pi 3 Model B via GPIO shield


Requirements:
- 3.5" Raspberry Pi TFT LCD Touchscreen (Waveshare Model B used in this tutorial)
- Raspberry Pi 3b+ or higher
- Python 3
- Terminal/Command Line Interface Access

Table of Contents:
- Operating System and Configuration
- Touchscreen Configuration
- Graphical User Interface (GUI) Creation
- Configuring SSH Keys
- Configuring Python/Bash Files





# Tutorial

## Operating System and Configuration
This tutorial will asume that you are beginning with Raspian, the standard Raspberry Pi OS, installed. If you don't have Raspian installed or don't know what that means, follow [this tutorial](https://www.raspberrypi.org/documentation/installation/installing-images/)


### Enabling SSH on the Pi
If you have a fresh install of Raspbian, you'll need to follow [this documentation](https://www.raspberrypi.org/documentation/remote-access/ssh/) to enable SSH so that we can connect to the Pi from our computer. This makes development easier.


### Connecting to the Raspberry Pi via SSH
Below are links to the official Raspberry Pi documentation to connect via SSH.
[Using Windows 10](https://www.raspberrypi.org/documentation/remote-access/ssh/windows10.md)
[Using MacOS (or Linux)](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)


## Touchscreen Configuration
For the purposes of this tutorial, Waveshare's 3.5inch Raspberry Pi LCD (B) was used. Your touchscreen documentation may differ.
[Official Waveshare Documentation](https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(B)#Image)

Open up Terminal application on your Pi. From there:
```
git clone https://github.com/waveshare/LCD-show.git
cd LCD-show/
```

Then run:
```
chmod +x LCD35B-show-V2
./LCD35B-show-V2 
 ```


The touch function will work after the pi restarts. You can set the screen orientation based on how you plan to use your Pi. 

0 degree rotation
```
cd LCD-show
./LCD35B-show-V2 0
```

90 degree rotation
```
cd LCD-show/
./LCD35B-show-V2 90
```

180 degree rotation
```
cd LCD-show/
./LCD35B-show-V2 180
```

270 degree rotation

```
cd LCD-show/
./LCD35B-show-V2 270
```



## Graphical User Interface (GUI) Creation 
Now, we will follow steps to create a functional user interface for our Pi. We will use the software PyQt, an adaptation of Qt that includes Python boilerplate code and an interactive prototyping interface.


### Downloading PyQt5 
Then this:
https://www.baldengineer.com/raspberry-pi-gui-tutorial.html

Now, we will upgrade python setuptools and make sure pip recognizes pyqt5. 
```
pip3 install --upgrade setuptools
pip3 install pyqt5
```



To boot the GUI automatically when the Pi starts, we'll have to exable X Windows. note: need to fix this part - Running on Startup: https://ozzmaker.com/enable-x-windows-on-piscreen/

Run:
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
  
and add this below bottom line:
```
sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
@/usr/bin/python3 /home/pi/pigui/init.py
```
then exit and type:
`sudo reboot`

Now, gui should boot on startup. 

# Note: touchscreen settings worked this time around. 
not sure how to configure this to stay.

#Tested adding '@' before "sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh" in "/etc/xdg/lxsession/LXDE-pi/autostart".
This might have fixed the issue. Rebooting again to see if calibration changes.




## Configuring SSH Keys for communication between Pi and main device (Optional)
In order to seamlessly automate GUI functions, we will need to configure SSH keys so that the Pi can access and execute bash scripts on our primary device.

to enable ssh from the pi to the computer:
`pi@raspberrypi: ssh-keygen -t rsa`
press enter twice to leave password blank

now, you need to copy this key to your main device. I used a Mac OSX device, but ran into several permissions issues on the pi and mac. 
To avoid this, you'll need to change some permissions settings.

On both the Pi and other device:
`chmod 0700 ~/.ssh`


On the Mac OSX:
```
sudo chown jacobkeller .ssh
sudo chown jacobkeller .ssh/authorized_keys
```


Biggest hurdle with pi SSH --> couldn't get permissions set right to allow the ssh key on the macbook to write. 
Error messages i couldn't get past: 
permission denied on authorized_key file
sh: .ssh/authorized_keys: Permission denied --> Indicative of permissions issue on my pi

After this, we will attempt to transfer the ssh key we generated on the pi to the other device:
`scp ~/.ssh/id_rsa.pub user@hostname:~/.ssh/authorized_keys`

I the following error when attempting to transfer the ssh key:
scp: /Users/jacobkeller/.ssh/authorized_keys: Permission denied
It was indicative of a permissions issue on my Mac for the authorized keys folder, which i resolved with running:
`sudo chown jacobkeller .ssh/authorized_keys`

Once I did this, the above command worked, trasnferring the ssh key from the pi to the mac, allowing password-less login to my computer from the pi. 




From here, we have to figure out how to send bash commands to your main device (computer) from the functioning gui embedded in the python script. 
now: writing bash script to ssh when a button is pressed
https://stackoverflow.com/questions/13745648/running-bash-script-from-within-python/13745968







Now we need to tell the python script controlling the gui to call the bash script when the button of choice is pressed. For this we'll use subprocess:

Example: 
```
import subprocess
print "start"
subprocess.call("sleep.sh")
print "end"
```


Code I used: 
```
import subprocess
subprocess.call"hdmi.sh")
```


I'm now thinking that using ssh to execute bash or python files stored on the computer is the best way to do this. When a gui button is pressed, it calls the python file init.py; init.py knows when buttons are being pressed, and executes the file stored on the mac 
#This simplifies the stress placed on the ssh connection by storing programs locally to be called upon when needed and excecute in the background.

to run a bash file on your computer, you'll need to give it privileges:
`chmod +x script-name-here.sh`

so far:
```
chmod +x hdmi.sh
chmod +x redirect.sh
chmod +x btn1.sh`
```

make sure to change in the directory before settting permissions with chmod +x:
`cd /github/pigui`

This also may be required when testing/using bash scripts on the pi. use this any time you encounter a "permission denied" error during this stage.

Before moving on, test your bash scripts on your main device. Once you've established their functionality, we should attempt to remotely run the bash script from the Pi.

## Configuring Python/Bash Files

create a bash script on your main device. open it using the direct path to test it works. If you are unfamiliar with the direct path, on Mac OS X you can locate the file in finder, and click and drag its icon into terminal, which leaves you with the full path. 
This is what I used:
MBP:~ jacobkeller$ /Users/jacobkeller/Documents/GitHub/pigui/hdmi.sh


currently, on raspberry pi the hdmi.sh bash script is reponsbile for ssh'ing into the Mac. It then executes a locally held (on the mac) bash script titled redirect.sh

Name changes: 
hdmi.sh --> btn1.sh
redirect.sh --> btn1redirect.sh


an issue i was running into was that i forgot to change the file destinations in init.py to be bash scripts hosted on the pi. Once I changed this, btn1.sh worked upon hitting button 1 in the gui.After you do this, you'll have to be comfortable testing on the pi itself, as you will be unable to run the gui on your pc from >>python3 init.py

any time a .sh file says 'file not found', add this to the beginning of the file:
`export PATH=/bin:/usr/bin:/usr/local/bin`




------
v2: SSH'ing into Windows

