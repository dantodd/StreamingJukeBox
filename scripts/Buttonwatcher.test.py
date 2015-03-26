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
import SJB_Podcasts as podcasts




# These are the default directory locations as they appear in the
# installation guide.
scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'



# configure the IO system for the buttons attached
# This shouldn't need any editing but if you can't use the defauly pins
# you will need to fix this section to reflect where you wired the buttons.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN) # Button1
GPIO.setup(19, GPIO.IN) # Button2
GPIO.setup(4, GPIO.IN) # ButtonDown
GPIO.setup(17, GPIO.IN) # ButtonUp
GPIO.setup(27, GPIO.IN) # Button5
GPIO.setup(22, GPIO.IN) # Button6





# You must add any new modules manualy to the "Modules" list below
# using the name of the module EXACTLY as you have imported it.
Modules = ['pandora', 'podcasts', 'test2', 'test3', 'test4']

# Set default module here. Again use the name exactly as you have imported it.
SJBModule = pandora
# SJBModule = podcasts
MenuSelect = 'no'

#TODO create source selectoin system in MainMenu function below

def MainMenu(MenuButton):
    global SJBModule
    if (MenuButton == "init"):
        a=0
        b=1
        display.updateMenu(Modules[a], Modules[b])
    if(MenuButton == "5"):
        SJBModule = str(Modules[a])
    if(MenuButton == "Up"):
       if(a==0):
           a = len(Modules())
           b = 0
       else:
           a = a - 1
           if (b == 0):
               b = len(Modules())
           else:
               b = b - 1
    if(MenuButton == "Down"):
        if (b == len(Modules())):
            b = 0
            a = a + 1
        else:
            b = b + 1
            if(a == len(Modules())):
                a = 0
            else:
                a = a + 1
    print Modules[0] + " and " + Modules[1]
   

    





# BEGIN SJBModue button calls
# These are the functions that get that pass the button information to
# the function "Button" in each module.
#
# The button values passed are as follows: '1', '2', 'Down', 'Up', '5', '6'
#
# When writing a new module please follow the convention of receiving all standard
# button press data into a function called Button. This will maximize interoperability.
#
# TODO delete teh print commands. They are there to tell me to which module
#      is passing data.


def Button1(channel):
    print "launching.Button1"
    print SJBModule
    if(MenuSelect == 'menu'):
        MainMenu('1')
    else:
        SJBModule.Button(1)
    
    
def Button2(channel):
    print "launching.Button2"
    if(MenuSelect == 'menu'):
        MainMenu('2')
    else:
        SJBModule.Button('2')
    
def ButtonDown(channel):
    print "launching.ButtonDown"
    if(MenuSelect == 'menu'):
        MainMenu('Down')
    else:
        SJBModule.Button('Down')
    print SJBModule


def ButtonUp(channel):
    print "launching.ButtonUp"
    if(MenuSelect == 'menu'):
        MainMenu('Up')
    else:
        SJBModule.Button('Up')
    print SJBModule


def Button5(channel):
    print "launching.Button5"
    if(MenuSelect == 'menu'):
        MainMenu('5')
    else:
        SJBModule.Button('5')
    print SJBModule


def Button6(channel):
    print "launching.Button(6)"
    if(MenuSelect == 'menu'):
        MainMenu('6')
    else:
        SJBModule.Button('6')
    print SJBModule
    
	
#  END SJBModule button module




# testing button long press functions for selection of a "Main Menu"
def Menu_test(channel):
    sleep(.2)
    i = 0
    if GPIO.input(22):
        while i < 4:
            sleep(.25)
            if GPIO.input(22):
                i= i + 1
                continue
            else:
                # print "gpio didn't poll high"
               Button6('a')
               break
        MenuSelect = 'menu'    
        MainMenu("init")
        

    else:
        # print "trying to run Button action 5"
        Button6('a')




# GPIO button interrupt detection
GPIO.add_event_detect(13, GPIO.RISING, callback=Button1, bouncetime=200)
GPIO.add_event_detect(19,GPIO.RISING,  callback=Button2, bouncetime=200) 
GPIO.add_event_detect(4, GPIO.RISING, callback=ButtonDown, bouncetime=200) 
GPIO.add_event_detect(17, GPIO.RISING, callback=ButtonUp, bouncetime=200) 
GPIO.add_event_detect(27, GPIO.RISING, callback=Button5, bouncetime=200) 
GPIO.add_event_detect(22, GPIO.RISING, callback=Menu_test, bouncetime=200) 
#GPIO.add_event_detect(22, GPIO.RISING, callback=Button6, bouncetime=200) 



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
