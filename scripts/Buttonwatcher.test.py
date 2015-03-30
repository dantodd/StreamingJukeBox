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
import importlib


# These are the functional modules needed by StreamingJukeBox
import SJB_DisplayManager as display

# List Modules to load here.
# 1) The Modules must all be in the same directory as the Buttonwatch file.
# 2) They must be listed exactly as they appear in the filename excluding
#     the "SJB" portion and the file extension.
# for example the module SJB_Pandora.py is entered as 'Pandora'
# The modules will be listed in the display in the order you enter them here.

Modules = ['Pandora', 'Spotify', 'Podcasts', 'LiveStreams']



#These are the default directory locations as they appear in the
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






# Import modules listed above and generate list of modules.
i=0
ModuleNames = []
while i < len(Modules):
    ModuleNames.insert(i, str(Modules[i]))
    Modules[i] = __import__('SJB_' + Modules[i])
    print Modules[i]
    i = i + 1

# Set default module here. Again use the name exactly as you have imported it.
#SJBSource = Pandora
SJBSource = Modules[0]
MenuSelect = 'no'

#TODO create source selection system in MainMenu function below

def MainMenu(MenuButton):
    global MenuSelect
    a = 0
    b = 1
    global SJBSource

    if (MenuButton == "init"):
        print "MainMenu init"
        a=0
        b=1
        display.updateMenu (ModuleNames[a], ModuleNames[b])
        print "MenuSelect = " + MenuSelect
    if(MenuButton == "5"):
        print 'a = ' + a
        print Modules[a]
        print SJBSource
        MenuSelect = "no"
        display.clear()
        print SJBSource
    if(MenuButton == "Up"):
        if(a == 0):
           a = (len(Modules) -1)
           b = 0
           display.updateMenu(ModuleNames[a], ModuleNames[b])
        else:
            a = a - 1
            if (b == 0):
                b = (len(Modules)-1)
            else:
                b = b - 1
            display.updateMenu(ModuleNames[a], ModuleNames[b])
    if(MenuButton == "Down"):
        if (b == (len(Modules) - 1)):
            b = 0
            a = a + 1
            display.updateMenu(ModuleNames[a], ModuleNames[b])
        else:
            b = b + 1
            if(a == (len(Modules) - 1)):
                a = 0
            else:
                a = a + 1
            display.updateMenu(ModuleNames[a], ModuleNames[b])
    print a, b
    print "a = " + ModuleNames[a] + " and b = " + ModuleNames[b]
   

    





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
    if(MenuSelect == 'menu'):
        MainMenu('1')
    else:
        print "launching.Button1"
        print SJBSource
        SJBSource.Button('1')
                        
    
    
def Button2(channel):
    if(MenuSelect == 'menu'):
        MainMenu('2')
    else:
        print "launching.Button2"
        print SJBSource
        SJBSource.Button('2')
    
def ButtonDown(channel):
    if(MenuSelect == 'menu'):
        MainMenu('Down')
    else:
        print "launching.ButtonDown"
        print SJBSource
        SJBSource.Button('Down')


def ButtonUp(channel):
    if(MenuSelect == 'menu'):
        MainMenu('Up')
    else:
        print "launching.ButtonUp"
        print SJBSource
        SJBSource.Button('Up')


def Button5(channel):
    if(MenuSelect == 'menu'):
        MainMenu('5')
    else:
        print "launching.Button5"
        print SJBSource
        SJBSource.Button('5')


def Button6(channel):
    if(MenuSelect == 'menu'):
        MainMenu('6')
    else:
        print "launching.Button6"
        print SJBSource
        SJBSource.Button('6')
    #print SJBSource
    
    
#  END SJBSource button module




# testing button long press functions for selection of a "Main Menu"
def Menu_test(channel):
    global MenuSelect
    sleep(.25)
    i = 0
    if GPIO.input(22):
        while i < 7:
            sleep(.25)
            if GPIO.input(22):
                i= i + 1
            else:
                # print "gpio didn't poll high"
               Button6(channel)
               break
        MenuSelect = 'menu'    
        MainMenu("init")
    else:
        Button6(channel)
    



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
