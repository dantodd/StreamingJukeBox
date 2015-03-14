#!/usr/bin/env python
 
# import sys, serial, time, os, socket
import sys
import os
#from time import sleep
#from random import randint
import pickle
import sys
import SJB_DisplayManager as display

# Pianobar setup
total_stations = 16
current_station = 4

playing_stream = "Playing"
pianobar_on = "0"
songfile_text = "-1"
stationfile_text = "-1"


scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
fifo_folder_location = '/home/pi/.config/pianobar/ctl'
#fifo_folder_location = '/home/pi/.config/pianobar/test.txt'



def main():
    global playing_stream
    global current_station
    global pianobar_on 
    global songfile_text



# MAIN MENU 

# BEGIN Pianobar button module

def Button1(): #Skip Song
    os.system('echo "n" >> ' + fifo_folder_location)


def Button2(): # Next station
    global current_station
    old_station = current_station
    if (old_station < total_stations):
        current_station = old_station + 1
    else:
        current_station = 0

    os.system('echo "s' + str(current_station) + '" >> ' + fifo_folder_location)


def ButtonDown(): # Volume down
    os.system('echo "(" >> ' + fifo_folder_location)


def ButtonUp(): # Volume up
    os.system('echo ")" >> ' + fifo_folder_location)


def Button5(): # Pause/play
    os.system('echo "p" >> ' + fifo_folder_location)
			

def Button6():
#figure out how to use PID to determine if pianobar is playing and take appropriate action
    os.system('pianobar &')
