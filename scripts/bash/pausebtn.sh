#!/bin/bash

#runs AppleScript to play/pause music
osascript <<EOD
tell application "System Events"
	set MyList to (name of every process)
end tell
if (MyList contains "Spotify") is true then
	tell application "Spotify" to playpause
end if
EOD