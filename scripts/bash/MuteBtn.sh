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