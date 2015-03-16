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
import SJB_Pandora as pandora



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(13, GPIO.IN) # Button1
GPIO.setup(19, GPIO.IN) # Button2
GPIO.setup(4, GPIO.IN) # ButtonDown
GPIO.setup(17, GPIO.IN) # ButtonUp
GPIO.setup(27, GPIO.IN) # Button5
GPIO.setup(22, GPIO.IN) # Button6

scripts_folder_location = '/home/pi/StreamingJukeBox/scripts/'
pianobar_folder_location = '/home/pi/.config/pianobar/'
#fifo_folder_location = '/home/pi/.config/pianobar/ctl'
#fifo_folder_location = '/home/pi/.config/pianobar/test.txt'


SJBModule = "Pandora"



# MAIN MENU 

##def Activate_menu():
##    print "this is something"
##
##
##def Menu_test(channel):
##    # print "hit menu_test function"
##    #sleep(.2)
##    if GPIO.input(22):
##        # print "gpio polled high"
##        sleep(1.5)
##        if GPIO.input(22):
##            print Activate_menu()
##        else:
##            # print "gpio didn't poll high"
##            print Button6()
##    else:
##        # print "trying to run Button action 5"
##        print Button6()




# GPIO button interrupts
GPIO.add_event_detect(13, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(19,GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(4, GPIO.RISING, bouncetime=200) 
GPIO.add_event_detect(17, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(27, GPIO.RISING, bouncetime=200) 
GPIO.add_event_detect(22, GPIO.RISING, bouncetime=200) 



while True:
        
#    GPIO.add_event_detect(13, GPIO.RISING, bouncetime=200)
    if GPIO.event_detected(13):
        print "launching " + SJBModule + ".Button1"
        if SJBModule == "Pandora":
            pandora.Button1()
        elif SJBModule == "Podcasts":
            SJBPodcasts.Button1()
        
#    GPIO.add_event_detect(19,GPIO.RISING, bouncetime=200)
    if GPIO.event_detected(19):
        print "launching " + SJBModule + ".Button2"
        if SJBModule == "Pandora":
            pandora.Button2()
        elif SJBModule == "Podcasts":
            SJBPodcasts.Button2()

    
#    GPIO.add_event_detect(4, GPIO.RISING, bouncetime=200) 
    if GPIO.event_detected(4):
        print "launching " + SJBModule + ".ButtonDown"
        if SJBModule == "Pandora":
            pandora.ButtonDown()
        elif SJBModule == "Podcasts":
            SJBPodcasts.ButtonDown()


#    GPIO.add_event_detect(17, GPIO.RISING, bouncetime=200) 
    if GPIO.event_detected(17):
        print "launching " + SJBModule + ".ButtonUp"
        if SJBModule == "Pandora":
            pandora.ButtonUp()
        elif SJBModule == "Podcasts":
            SJBPodcasts.ButtonUp()


#    GPIO.add_event_detect(27, GPIO.RISING, bouncetime=200) 
    if GPIO.event_detected(27):
        print "launching " + SJBModule + ".Button5"
        if SJBModule == "Pandora":
            pandora.Button5()
        elif SJBModule == "Podcasts":
            SJBPodcasts.Button5()


    #GPIO.add_event_detect(22, GPIO.RISING, callback=Menu_test, bouncetime=200) 

#    GPIO.add_event_detect(22, GPIO.RISING, bouncetime=200) 
    if GPIO.event_detected(22):
        print "launching " + SJBModule + ".Button6"
        if SJBModule == "Pandora":
            pandora.Button6()
        elif SJBModule == "Podcasts":
            SJBPodcasts.Button6()
            
