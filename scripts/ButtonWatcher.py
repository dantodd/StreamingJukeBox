#!/usr/bin/env python
 
import sys, serial, time, os, socket
from time import sleep
#from random import randint
from subprocess import Popen
import pickle
import sys
import RPi.GPIO as GPIO
#import lcddriver

#lcd = lcddriver.lcd()



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(13, GPIO.IN) # Skip Song
GPIO.setup(19, GPIO.IN) # Change Station
GPIO.setup(4, GPIO.IN) # Vol -
GPIO.setup(17, GPIO.IN) # Vol +
GPIO.setup(27, GPIO.IN) # Play/Pause
GPIO.setup(22, GPIO.IN) # Menu

scripts_folder_location = '/home/pi/.config/pianobar/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
fifo_folder_location = '/home/pi/.config/pianobar/ctl'
#fifo_folder_location = '/home/pi/.config/pianobar/test.txt'


SJBModule_active = "Pianobar"

# Pianobar setup and variables
total_stations = 16
current_station = 7
playing_stream = "Playing"
pianobar_on = "0"
songfile_text = "-1"
stationfile_text = "-1"


def main():
    global playing_stream
    global current_station
    global pianobar_on 
    global songfile_text
    sleep(4)
    	


# MAIN MENU 

def Activate_menu():
    print "this is something"






# BEGIN Pianobar button module

def skip_song(channel):
    os.system('echo "n" >> ' + fifo_folder_location)
    sleep(.20)
#    screen_update()
    subprocess.Popen("python /home/pi/StreamingJukeBox/DisplayManager.py")
def next_station(channel):
    sleep(.2)
    global current_station
    old_station = current_station
    if (old_station < total_stations):
        current_station = old_station + 1
    else:
        current_station = 0

    sleep(.2)
    os.system('echo "s' + str(current_station) + '" >> ' + fifo_folder_location)
#    screen_update()
    subprocess.Popen(~/StreamingJukebox/DisplayManager.py)

def volume_down(channel):
    sleep(.20)
    os.system('echo "(" >> ' + fifo_folder_location)
#    screen_update()
    subprocess.Popen(~/StreamingJukebox/DisplayManager.py)

def volume_up(channel):
    sleep(.20)
    os.system('echo ")" >> ' + fifo_folder_location)
#    screen_update()
    subprocess.Popen(~/StreamingJukebox/DisplayManager.py)


def pause_play(channel):
    sleep(.20)
    os.system('echo "p" >> ' + fifo_folder_location)
#    screen_update()
    subprocess.Popen(~/StreamingJukebox/DisplayManager.py)
			

def quit_pianobar():
    global pianobar_on
    if (pianobar_on == "1"):
        os.system('echo "q" >> ' + fifo_folder_location)
        pianobar_on = "0" 
    else:
        os.system('pianobar &')
        pianobar_on = "1"
    sleep(.20)
#    screen_update()
    subprocess.Popen(~/StreamingJukebox/DisplayManager.py)
	
#  END Pianobar button module


# Paste module specific Function Arrays here:

#Pianobar button function array
Pianobar_buttons=[skip_song, next_station, volume_down, volume_up, pause_play, quit_pianobar]


# Main Menu Button Function array
Main_Menu_buttons=[skip_song, next_station, volume_down, volume_up, pause_play, quit_pianobar]

if SJBModule_active == "Pianobar":
    Button_function = Pianobar_buttons
elif SJBModule_active == "MainMenu":
    Button_function = Main_Menu_buttons
    

def getIPAddress():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    IPaddr = s.getsockname()[0]

#def screen_update():
#    global songfile_text
#    global stationfile_text
#    stationfile_text_old = stationfile_text
#    stationfile = open(pianobar_folder_location + 'station')
#    stationfile_text = stationfile.read()
#    if stationfile_text != stationfile_text_old:
#        screen_line1 = stationfile_text[:16]
#        screen_line2 = stationfile_text[16:-1]
#        lcd.lcd_clear()
#        lcd.lcd_display_string(screen_line1, 1)
#        lcd.lcd_display_string(screen_line2, 2)
#        time.sleep(5)
#
#
#    songfile_text_old = songfile_text
#    songfile = open(pianobar_folder_location + 'nowplaying')
#    songfile_text = songfile.read()
#    dataspace = songfile_text.find("--")
#    if songfile_text != songfile_text_old:
#        if dataspace > 16:
#            screen_line1 = songfile_text[:16]
#        else:
#            screen_line1 = songfile_text[0:dataspace -1]
#        screen_line2 = songfile_text[dataspace +3:-1]
#        lcd.lcd_clear()
#        lcd.lcd_display_string(screen_line1, 1)
#        lcd.lcd_display_string(screen_line2, 2)


def Menu_test(channel):
    # print "hit menu_test function"
    sleep(.2)
    if GPIO.input(22):
        # print "gpio polled high"
        sleep(1.5)
        if GPIO.input(22):
            print Activate_menu()
        else:
            # print "gpio didn't poll high"
            print Button_function[5]()
    else:
        # print "trying to run Button action 5"
        print Button_function[5]()




# GPIO button interrupts

GPIO.add_event_detect(13, GPIO.RISING, callback=Button_function[0], bouncetime=200)
GPIO.add_event_detect(19,GPIO.RISING,  callback=Button_function[1], bouncetime=200) 
GPIO.add_event_detect(4, GPIO.RISING, callback=Button_function[2], bouncetime=200) 
GPIO.add_event_detect(17, GPIO.RISING, callback=Button_function[3], bouncetime=200) 
GPIO.add_event_detect(27, GPIO.RISING, callback=Button_function[4], bouncetime=200) 
GPIO.add_event_detect(22, GPIO.RISING, callback=Menu_test, bouncetime=200) 






#while True:
#    screen_update()
#    sleep(10)

test_count = 0
try:
    while(test_count < 100):
        test_count = test_count +1
        sleep(6)
        screen_update()
        if (test_count > 50):
            test_count = 0
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit   
