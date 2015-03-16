#!/usr/bin/env python

from time import sleep
import sys
import lcddriver
songfile_text = "-1"
stationfile_text = "-1"
lcd = lcddriver.lcd()
pianobar_folder_location = '/home/pi/.config/pianobar/'


def update2lines(screen_line1, screen_line2):
    lcd.lcd_clear()
    lcd.lcd_display_string(screen_line1, 1)
    lcd.lcd_display_string(screen_line2, 2)

def StationUpdate():
    global stationfile_text
    stationfile = open(pianobar_folder_location + 'station')
    stationfile_text = stationfile.read()
    screen_line1 = stationfile_text[:16]
    screen_line2 = stationfile_text[16:-1]
    lcd.lcd_clear()
    lcd.lcd_display_string(screen_line1, 1)
    lcd.lcd_display_string(screen_line2, 2)
    sleep(5)

def SongUpdate():
    global songfile_text
    songfile = open(pianobar_folder_location + 'nowplaying')
    songfile_text = songfile.read()
    dataspace = songfile_text.find("--")
    if dataspace > 16:
        screen_line1 = songfile_text[:16]
    else:
        screen_line1 = songfile_text[0:dataspace -1]
    screen_line2 = songfile_text[dataspace +3:-1]
    lcd.lcd_clear()
    lcd.lcd_display_string(screen_line1, 1)
    lcd.lcd_display_string(screen_line2, 2)

