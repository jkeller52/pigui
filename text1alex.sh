
osascript <<EOD
    on run {targetBuddyPhone, targetMessage}
    -- handles conversation not started
    -- does not handle contact not existing
    set hasError to false

    tell application "Messages"
        -- if Messages.app was not running, launch it
        set wasRunning to true
        if it is not running then
            set wasRunning to false
            launch
            close window 1
            my waitUntilRunning("Messages", 1)
            close window 1
        end if

        log "trying via imessage"
        try
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            log "sent via imessage"
        on error
            log "trying via SMS"
            try
                set targetService to service "SMS"
                set targetBuddy to buddy targetBuddyPhone of targetService
                send targetMessage to targetBuddy
                log "sent via SMS"
            on error
                set hasError to true
            end try
        end try

        -- if the app was not running, close the window
        if not wasRunning
            close window 1
        end if
    end tell

    if hasError
        log "trying via new conversation"
        try
            createMessagesConversation(targetBuddyPhone,targetMessage)
            log "sent via new conversation"
        on error
            log "contact does not exist, can not send message"
        end try
    end if
end run

EOD

