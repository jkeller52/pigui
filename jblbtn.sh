#!/bin/bash

osascript <<EOD
    tell application "System Events"
	tell process "ControlCenter"
		set bt to (first menu bar item whose title is "Bluetooth") of menu bar 1
		click bt
		set btCheckbox to checkbox 1 of scroll area 1 of group 1 of window "Control Center" whose title contains "JBL Charge 3"
		set btCheckboxValue to value of btCheckbox
		tell btCheckbox to click
		tell bt to click
	end tell
end tell

EOD