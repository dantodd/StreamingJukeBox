#!/usr/bin/env python
# TODO figure out menu sytem to select a channel from the list.
 
import subprocess
import os
from time import sleep
import SJB_DisplayManager as display

# Pianobar setup; wil definitely need manual setup.
total_stations = 16
current_station = total_stations - 1


# File locations, may need manual setup.
scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
fifo_folder_location = '/home/pi/.config/pianobar/ctl'



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

def Button1(): #Skip Song
    try:
        subprocess.check_output('pgrep pianobar', shell=True)  # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:
        print "Pianobar isn't running"

    else:
        os.system('echo "n" >> ' + fifo_folder_location)



def Button2(): # Next station
    try:
        subprocess.check_output('pgrep pianobar', shell=True)  # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:
        print "Pianobar isn't running"
    else:
        global current_station
        old_station = current_station
        if (old_station < (total_stations -1)):
            current_station = old_station + 1     
        else:
            current_station = 0
        os.system('echo "s' + str(current_station) + '" >> ' + fifo_folder_location)



def ButtonDown(): # Volume down
    try:
        subprocess.check_output('pgrep pianobar', shell=True) # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo "(" >> ' + fifo_folder_location)


def ButtonUp(): # Volume up
    try:
        subprocess.check_output('pgrep pianobar', shell=True)  # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo ")" >> ' + fifo_folder_location)


def Button5(): # Pause/play
    try:
        subprocess.check_output('pgrep pianobar', shell=True) # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo "p" >> ' + fifo_folder_location)
            

def Button6():  
    try:
        subprocess.check_output('pgrep pianobar', shell=True)  # check if pianobar is running This may not work if you don't launch pianobar as instructed      
    except Exception:  # start pianobar if it isn't running
        print "About to start pianobar"
        os.system('pianobar &')
        # TODO Need to extract and write list of stations here.
        
    else: # if pianobar is running turn it off (essentially toggles pianobar)
        os.system('echo "q" >> ' + fifo_folder_location)
