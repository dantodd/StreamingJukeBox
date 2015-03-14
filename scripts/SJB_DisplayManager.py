#!/usr/bin/env python

import sys
import lcddriver
songfile_text = "-1"
stationfile_text = "-1"
lcd = lcddriver.lcd()
pianobar_folder_location = '/home/pi/.config/pianobar'

void main():
    global songfile_text
    global stationfile_text
    stationfile_text_old = stationfile_text
    stationfile = open(pianobar_folder_location + 'station')
    stationfile_text = stationfile.read()
    if stationfile_text != stationfile_text_old:
        screen_line1 = stationfile_text[:16]
        screen_line2 = stationfile_text[16:-1]
        lcd.lcd_clear()
        lcd.lcd_display_string(screen_line1, 1)
        lcd.lcd_display_string(screen_line2, 2)
        time.sleep(5)


    songfile_text_old = songfile_text
    songfile = open(pianobar_folder_location + 'nowplaying')
    songfile_text = songfile.read()
    dataspace = songfile_text.find("--")
    if songfile_text != songfile_text_old:
        if dataspace > 16:
            screen_line1 = songfile_text[:16]
        else:
            screen_line1 = songfile_text[0:dataspace -1]
        screen_line2 = songfile_text[dataspace +3:-1]
        lcd.lcd_clear()
        lcd.lcd_display_string(screen_line1, 1)
        lcd.lcd_display_string(screen_line2, 2)
