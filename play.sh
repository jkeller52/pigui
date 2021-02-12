#!/bin/bash

#runs AppleScript to play music from 'Liked Songs' Playlist
osascript <<EOD
    tell application "Spotify"
 	play "Liked Songs"
 end tell
EOD
