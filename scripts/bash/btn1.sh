#!/bin/bash
export PATH=/bin:/usr/bin:/usr/local/bin
#changes monitor input to displayport using ddcctl in other script
ssh -T jacobkeller@mbp.wowway.com '/Users/jacobkeller/Documents/GitHub/pigui/dp.sh'
