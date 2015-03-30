#!/usr/bin/env python
# TODO figure out menu sytem to select a channel from the list.
# New file to update from "pgrep" and fifo to direct shell interaction


import subprocess
import os
from time import sleep
import SJB_DisplayManager as display

#mp is the process file handle for the pandora module pianobar
mp = None

# Pianobar setup; wil definitely need manual setup.
total_stations = 16
current_station = total_stations - 1


# File locations, may need manual setup.
scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
fifo_folder_location = '/home/pi/.config/pianobar/ctl'

# Staions array
# Stations[] 

# MAIN MENU 
# If you instal all the modules required where directed nothing should need
# editing below this unless you want to change functionality

def UpdateDisplay():

    ## Station information and update
    stationfile = open(pianobar_folder_location + 'station')
    stationfile_text = stationfile.read()
    if stationfile_text > 16:
        station_line1 =  stationfile_text[:16]
        station_line2 = stationfile_text[16:]
    else:
        station_line1 =  stationfile_text[0:]
        station_line2 = ""
    display.update2lines(station_line1, station_line2)
    sleep(5)

    ## Song information and update
    songfile = open(pianobar_folder_location + 'nowplaying')
    songfile_text = songfile.read()
    songdataspace = songfile_text.find("--")
    if songdataspace > 16:
        song_line1 = songfile_text[:16]
        song_line2 = songfile_text[songdataspace +3:]
    else:
        song_line1 = songfile_text[0:songdataspace -1]
        song_line2 = songfile_text[songdataspace +3:]
    print song_line1 + " ------ " + song_line2
    display.update2lines(song_line1, song_line2)



# BEGIN Pianobar button controls
# pianobar, the Pandora program I am using, uses a fifo for programatic
# interaction. These simple functions simply write the proper commands to
# the fifo. We have to check to see if pianobar is running because when it 
# isn't running the Butonwatcher hangs on the fifo error.
#
# pgrep is a bit dangerous to use here but if installed as instructed it works well
#

def Button(ButtonVal):
    
    if ButtonVal == "1":
        print "LiveStreams Button1"
    if ButtonVal == "2":
        print "LiveStreams Button2"
    if ButtonVal == "Down":
        print "LiveStreams ButtonDown"
    if ButtonVal == "Up": # Volume up
        print "LiveStreams ButtonUp"
    if ButtonVal == "5": # Pause/play
        print "LiveStreams Button5"
    if ButtonVal == "6": # quit
        print "LiveStreams button6"
    return
        
def MenuButton(ButtonVal):
    print "placeholders"
        
def MenuButton(ButtonVal):
    print "placeholders"
