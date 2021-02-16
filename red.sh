#!/bin/bash
export PATH=/bin:/usr/bin:/usr/local/bin
#ssh -T  'python3 /Users/jacobkeller/Documents/GitHub/pigui/redbtn.py'


ssh -T jacobkeller@mbp.wowway.com 'sudo . ~/.bashrc; /Users/jacobkeller/Documents/GitHub/pigui/redbtn.py'