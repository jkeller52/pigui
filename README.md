# piGUI
piGUI is an open-source automation project meant to enable beginner programmers and hobbyists to turn a Raspberry-Pi into a touchscreen Graphical User Interface (GUI) that can run control various IoT devices (smart lights, speakers/Spotify API, changing monitor inputs, etc). 

Using a few simple python and bash scripts, you can make a multi-page graphical interface using PyQt5, a variant of Qt Creator GUI software. This tutorial will use PyQt5 to generate boilerplate code for GUI elements, perfect for reducing load on beginner programmers interested in simple GUI applicatitons. 


A 3.5" Waveshare TFT LCD Touchscreen is connected to a Raspberry Pi 3 Model B via GPIO shield


Requirements:
- 3.5" Raspberry Pi TFT LCD Touchscreen (Waveshare Model B used in this tutorial)
- Raspberry Pi 3b+ or higher
- Python 3
- Terminal/Command Line Interface Access

 # Table of Contents:
- [Operating System and Configuration](https://github.com/jkeller52/pigui/blob/main/README.md#operating-system-and-configuration)
- [Touchscreen Configuration](https://github.com/jkeller52/pigui/blob/main/README.md#touchscreen-configuration)
- [Graphical User Interface (GUI) Creation](https://github.com/jkeller52/pigui/blob/main/README.md#configuring-ssh-keys-for-communication-between-pi-and-main-device-optional)
- [Configuring SSH Keys](https://github.com/jkeller52/pigui/blob/main/README.md#configuring-ssh-keys)
- [Configuring Python/Bash Files](https://github.com/jkeller52/pigui/blob/main/README.md#configuring-pythonbash-files)



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

>0 degree rotation
 ```
 cd LCD-show
 ./LCD35B-show-V2 0
 ```

>90 degree rotation
 ```
 cd LCD-show/
 ./LCD35B-show-V2 90
 ```

>180 degree rotation
 ```
 cd LCD-show/
 ./LCD35B-show-V2 180
 ```

>270 degree rotation
 ```
 cd LCD-show/
 ./LCD35B-show-V2 270
 ```

### Touchscreen Calibration




## Graphical User Interface (GUI) Creation 
Now, we will follow steps to create a functional user interface for our Pi. We will use the software PyQt, an adaptation of Qt that includes Python boilerplate code and an interactive prototyping interface.

### Downloading PyQt5
To download PyQt5, we will use pip3:
```
pip3 install --upgrade setuptools
pip3 install pyqt5
```

Then follow this:
https://www.baldengineer.com/raspberry-pi-gui-tutorial.html

On your development device, open up QtCreator. 




### GUI Autoboot

To boot the GUI automatically when the Pi starts, we'll have to exable X Windows. note: need to fix this part - Running on Startup: https://ozzmaker.com/enable-x-windows-on-piscreen/

Run:
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
  
and add this below bottom line:
```
sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
@/usr/bin/python3 /home/pi/pigui/init.py
```
Then exit and type:
`sudo reboot`

Now, gui should boot on startup. 

#Tested adding '@' before "sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh" in "/etc/xdg/lxsession/LXDE-pi/autostart".
This might have fixed the issue. Rebooting again to see if calibration changes.


-----

## Configuring Python/Bash Files

The architecture supporting the application will work as follows:
- The Python GUI recognizes when buttons are pressed
- The init.py file underlying the GUI includes functions run to bash (.sh) scripts on the pi for each button push
- The bash scripts on the pi include code which triggers an ssh connection into the development device/computer using ssh keys and executes a different bash file according to which button was pressed. This bash file runs an associated Python script to achieve the desired outcome of the button press.

The Python file executed on the main device will trigger the action desired, bypassing limitations of the Raspberry Pi and using it as a simple command-and-control system to automate tasks that are ran through your main device. On my Mac OSX device, this also allowed me to use AppleScript commands to interact with my devices. 



Example Scripts:


For example, pressing the "Mute" button invokes the code `subprocess.call("/home/pi/pigui/scripts/bash/Mute.sh")`, calling:

>Mute.sh
```
#!/bin/bash
export PATH=/bin:/usr/bin:/usr/local/bin
ssh -T jacobkeller@localhost '/Users/jacobkeller/Documents/GitHub/pigui/MuteBtn.sh'
```
Mute.sh ssh's into the main device, then runs MuteBtn.sh, an AppleScripts command to mute volume on Mac OSX:

>MuteBtn.sh
```
#!/bin/bash
#Applescript - won't work for Windows 10
#runs AppleScript to play/pause music
osascript <<EOD
tell application "System Events"
	set MyList to (name of every process)
end tell
if (MyList contains "Spotify") is true then
	tell application "Spotify"
		set volcheck to get sound volume
		set volcheck to volcheck - 30
		set sound volume to volcheck
	end tell
end if
EOD
```

This architecture is followed for each command and can be replicated to include new functions. Instead of Applescript being invoked in final file, you can also use Python, as some other examples in pigui do. For the testing phase, it is recommended to test the GUI using 'print' functions, then incorporate `subprocess.call("/home/pi/pigui/scripts/bash/file.sh")` and the aforementioned code. 



#### Troubleshooting:
any time a .sh file says 'file not found', add this to the beginning of the file:
`export PATH=/bin:/usr/bin:/usr/local/bin`
If you experience permissions errors when running bash files, be sure to cd into the /pigui/scripts/bash directory and run `sudo chmod +x filename.sh`, then try again. 




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



------
v2: SSH'ing into Windows

