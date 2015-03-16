#!/usr/bin/env python
# TODO fix Button6 so it toggles pianobar
 
import subprocess
import os
from time import sleep
import SJB_DisplayManager as display

# Pianobar setup
total_stations = 16
current_station = total_stations - 1


songfile_text = "Dan's Favorite Song"
stationfile_text = "Dan's Favorite Station"


scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
fifo_folder_location = '/home/pi/.config/pianobar/ctl'
#fifo_folder_location = '/home/pi/.config/pianobar/test.txt'






# MAIN MENU 

# BEGIN Pianobar button module

def UpdateDisplay():
    global stationfile_text
    global songfile_text
    stationfile_text_old =  stationfile_text
    stationfile_text = open(pianobar_folder_location + 'station').read()
    songfile_text = open(pianobar_folder_location + 'nowplaying').read()
    if stationfile_text != stationfile_text_old:
        screen_line1 = stationfile_text[:16]
        screen_line2 = stationfile_text[16:-1]
        display.update2lines(screen_line1, screen_line2)
        sleep(5)
    songdataspace = songfile_text.find("--")
    if songdataspace > 16:
        screen_line1 = songfile_text[:16]
        screen_line2 = songfile_text[dataspace +3:-1]
    else:
        screen_line1 = songfile_text[0:dataspace -1]
        screen_line2 = ""
    display.update2lines(screen_line1, screen_line2)


def Button1(): #Skip Song
    try:
        subprocess.check_output('pgrep pianobar', shell=True)        
    except Exception:
        print "Pianobar isn't running"

    else:
        os.system('echo "n" >> ' + fifo_folder_location)
#        sleep(15)    
#        UpdateDisplay()


def Button2(): # Next station
    try:
        subprocess.check_output('pgrep pianobar', shell=True)
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
        sleep(15)
#        UpdateDisplay()




def ButtonDown(): # Volume down
    try:
        subprocess.check_output('pgrep pianobar', shell=True)
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo "(" >> ' + fifo_folder_location)

def ButtonUp(): # Volume up
    try:
        subprocess.check_output('pgrep pianobar', shell=True)
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo ")" >> ' + fifo_folder_location)

def Button5(): # Pause/play
    try:
        subprocess.check_output('pgrep pianobar', shell=True)
    except Exception:
        print "Pianobar isn't running"
    else:
        os.system('echo "p" >> ' + fifo_folder_location)
			

def Button6():
    try:
        subprocess.check_output('pgrep pianobar', shell=True)
    except Exception:
        os.system('pianobar &')
        sleep(16)
        stationfile_text = "Dan's Test"
        songfile_text = "Dan's Test"
#        UpdateDisplay()

    else:
        os.system('echo "q" >> ' + fifo_folder_location)
