#!/usr/bin/env python
 
import os
import subprocess
fifo_folder_location = '/home/pi/.config/pianobar/ctl'


# Pianobar setup

#def main():

output = subprocess.check_output('pgrep pianobar', shell=True)
print output
print "what is happening here?"
if output > 0:
    os.system('echo "q" >> ' + fifo_folder_location)
else:
    os.system('pianobar&')

#figure out how to use PID to determine if pianobar is playing and take appropriate action
#    os.system('pianobar &')
