#!/bin/bash

#runs AppleScript to play music from 'Liked Songs' Playlist
osascript <<EOD
    tell application "Spotify"
 	pause "Liked Songs"
 end tell
EOD
