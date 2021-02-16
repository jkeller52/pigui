#!/usr/bin/bash
blueutil --connect 7c-58-ca-00-17-3f

osascript <<EOD
tell application "Spotify"
    play
end tell
EOD
