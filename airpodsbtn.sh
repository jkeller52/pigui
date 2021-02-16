#!/usr/bin/bash
blueutil --connect 3c-4d-be-9b-fe-b0

osascript <<EOD
tell application "Spotify"
    play
end tell
EOD
