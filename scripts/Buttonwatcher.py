#!/usr/bin/env python
 
import sys, serial, time, os, socket
from time import sleep
#from random import randint
import pickle
import sys
import RPi.GPIO as GPIO
#import lcddriver


# Uncomment the modules you are using.
import SJB_DisplayManager as display
import SJB_Pandora as Pandora



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(13, GPIO.IN) # Skip Song
GPIO.setup(19, GPIO.IN) # Change Station
GPIO.setup(4, GPIO.IN) # Vol -
GPIO.setup(17, GPIO.IN) # Vol +
GPIO.setup(27, GPIO.IN) # Play/Pause
GPIO.setup(22, GPIO.IN) # Menu

scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
#fifo_folder_location = '/home/pi/.config/pianobar/ctl'
#fifo_folder_location = '/home/pi/.config/pianobar/test.txt'


SJBModule_active = "Pianobar"


def main():
    print "testing the main loop"

# MAIN MENU 

def Activate_menu():
    print "this is something"






# BEGIN Pianobar button module

def Button1(channel):
    print "launching Pandora.Button1"
    sleep(.2)
    Pandora.Button1()
    display.StationUpdate()


def Button2(channel):
    print "launching Pandora.Button2"
    sleep(.2)
    Pandora.Button2()
    display.SongUpdate()


def ButtonDown(channel):
    print "launching Pandora.ButtonDown"
    sleep(.20)
    Pandora.Button2()
    display.SongUpdate()


def ButtonUp(channel):
    print "launching Pandora.ButtonUp"
    sleep(.20)
    Pandora.ButtonUp()
    display.SongUpdate()


def Button5(channel):
    print "launching Pandora.Button5"
    sleep(.0)
    Pandora.Button5()
    display.SongUpdate()


def Button6(channel):
    print "launching Pandora.Button6"
    sleep(.2)
    Pandora.Button6()
    display.SongUpdate()
	
#  END Pianobar button module


# Paste module specific Function Arrays here:




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
            print Button6()
    else:
        # print "trying to run Button action 5"
        print Button6()




# GPIO button interrupts

GPIO.add_event_detect(13, GPIO.RISING, callback=Button1, bouncetime=200)
GPIO.add_event_detect(19,GPIO.RISING,  callback=Button2, bouncetime=200) 
GPIO.add_event_detect(4, GPIO.RISING, callback=ButtonDown, bouncetime=200) 
GPIO.add_event_detect(17, GPIO.RISING, callback=ButtonUp, bouncetime=200) 
GPIO.add_event_detect(27, GPIO.RISING, callback=Button5, bouncetime=200) 
#GPIO.add_event_detect(22, GPIO.RISING, callback=Menu_test, bouncetime=200) 
GPIO.add_event_detect(22, GPIO.RISING, callback=Button6, bouncetime=200) 






#while True:
#    screen_update()
#    sleep(10)

test_count = 0
try:
    while(test_count < 100):
        test_count = test_count +1
        sleep(6)
#        screen_update()
#        display.SongUpdate()
        if (test_count > 50):
            test_count = 0
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit   
