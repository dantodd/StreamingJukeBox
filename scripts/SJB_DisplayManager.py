#!/usr/bin/env python

# This is a really short file. It is here priarily so that someone can simply
# write a new module for a different lcd driver and use the same function name(s)
# making this drop in not requiring ANY changes to the other components
# The other "Update" functions have been moved to the SJB_Pandora module to keep
# portability higher and keep this file as general as possible.


from time import sleep
import sys
import lcddriver

lcd = lcddriver.lcd()
pianobar_folder_location = '/home/pi/.config/pianobar/'


def update2lines(screen_line1, screen_line2):
    lcd.lcd_clear()
    lcd.lcd_display_string(screen_line1, 1)
    lcd.lcd_display_string(screen_line2, 2)

def updateMenu(screen_line1, screen_line2):
    lcd.lcd_clear()
    #lcd.lcd_write_four_bits(0x01 | 0x08)
#    lcd.lcd_strobe(0x00)
    lcd.lcd_display_string( '-> ' + screen_line1, 1)
#    lcd.lcd_write(0x01, 0x01)
    lcd.lcd_display_string(screen_line2, 2)



##def StationUpdate():
##    global stationfile_text
##    stationfile = open(pianobar_folder_location + 'station')
##    stationfile_text = stationfile.read()
##    screen_line1 = stationfile_text[:16]
##    screen_line2 = stationfile_text[16:-1]
##    lcd.lcd_clear()
##    lcd.lcd_display_string(screen_line1, 1)
##    lcd.lcd_display_string(screen_line2, 2)
##    sleep(5)
##
##def SongUpdate():
##    global songfile_text
##    songfile = open(pianobar_folder_location + 'nowplaying')
##    songfile_text = songfile.read()
##    dataspace = songfile_text.find("--")
##    if dataspace > 16:
##        screen_line1 = songfile_text[:16]
##    else:
##        screen_line1 = songfile_text[0:dataspace -1]
##    screen_line2 = songfile_text[dataspace +3:-1]
##    lcd.lcd_clear()
##    lcd.lcd_display_string(screen_line1, 1)
##    lcd.lcd_display_string(screen_line2, 2)
##
