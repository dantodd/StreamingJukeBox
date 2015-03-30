#!/usr/bin/env python
##  Buttonwatcher is the main director for the StreamingJukeBox project.
##  Buttonwatcher runs in ty4 at boot time.
##  It's primary job is to intercept your input via the 6 control buttons
##  It keeps track of your audio source selection and notifies the proper
##  program of your button presses.
##
##  Buttonwatcher's other job is to manage the main menu for source selection.


import sys
#import serial, os, socket
from time import sleep
import sys
import RPi.GPIO as GPIO


# Uncomment the modules you are using.
import SJB_DisplayManager as display
import SJB_Pandora as pandora
#import SJB_Podcasts as podcasts


# Global variable to store handle of current process that is playing
#mp = "module process"  


# These are the default directory locations as they appear in the
# installation guide.
scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'



# configure the IO system for the buttons attached
# This shouldn't need any editing but if you can't use the defauly pins
# you will need to fix this section to reflect where you wired the buttons.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
chan_list = [13, 19, 4, 17, 27, 22]
GPIO.setup(chan_list, GPIO.IN)

#GPIO.setup(13, GPIO.IN) # Button1
#GPIO.setup(19, GPIO.IN) # Button2
#GPIO.setup(4, GPIO.IN) # ButtonDown
#GPIO.setup(17, GPIO.IN) # ButtonUp
#GPIO.setup(27, GPIO.IN) # Button5
#GPIO.setup(22, GPIO.IN) # Button6



#TODO create source selectoin variables and selection system
SJBModule = "Pandora"



# MAIN MENU 

def Activate_menu():
    print "this is something"






# BEGIN SJBModue button calls
# These are the functions that get associated with the individual buttons
# Each button's function will determine which module to call and pass the
# button selection information.
#
# TODO delete teh print commands. They are there to tell me to which module
#      is passing data.


def Button1(channel):
    print "launching " + SJBModule + ".Button1"
    if SJBModule == "Pandora":
        pandora.Button1()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(1)

    
def Button2(channel):
    print "launching " + SJBModule + ".Button2"
    if SJBModule == "Pandora":
        pandora.Button2()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(2)


def ButtonDown(channel):
    print "launching " + SJBModule + ".ButtonDown"
    if SJBModule == "Pandora":
        pandora.ButtonDown()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(Down)


def ButtonUp(channel):
    print "launching " + SJBModule + ".ButtonUp"
    if SJBModule == "Pandora":
        pandora.ButtonUp()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(Up)


def Button5(channel):
    print "launching " + SJBModule + ".Button5"
    if SJBModule == "Pandora":
        pandora.Button5()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(5)


def Button6(channel):
    print "launching " + SJBModule + ".Button6"
    if SJBModule == "Pandora":
        pandora.Button6()
    elif SJBModule == "Podcasts":
        SJBPodcasts.Button(6)
	
#  END SJBModule button module



# testing button long press functions for selection of a "Main Menu"
def Menu_test(channel):
    # print "hit menu_test function"
    #sleep(.2)
    if GPIO.input(22):
        # print "gpio polled high"
        sleep(1.5)
        if GPIO.input(22):
            print Activate_menu()
        else:
            # print "gpio didn't poll high"
            print Button6()
    else:
        # print "trying to run Button action 6"
        print Button6()




# GPIO button interrupt detection
GPIO.add_event_detect(13, GPIO.RISING, callback=Button1, bouncetime=200)
GPIO.add_event_detect(19,GPIO.RISING,  callback=Button2, bouncetime=200) 
GPIO.add_event_detect(4, GPIO.RISING, callback=ButtonDown, bouncetime=200) 
GPIO.add_event_detect(17, GPIO.RISING, callback=ButtonUp, bouncetime=200) 
GPIO.add_event_detect(27, GPIO.RISING, callback=Button5, bouncetime=200) 
#GPIO.add_event_detect(22, GPIO.RISING, callback=Menu_test, bouncetime=200) 
GPIO.add_event_detect(22, GPIO.RISING, callback=Button6, bouncetime=200) 



# Keeps the program infinitely busy so it never ends and captures keyboard interupts
test_count = 0
try:
    while(test_count < 100):
        test_count = test_count +1
        sleep(6)
        if (test_count > 50):
            test_count = 0
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit   
