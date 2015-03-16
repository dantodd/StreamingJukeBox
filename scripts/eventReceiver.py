#!/usr/bin/env python
#Based on program of same name by Sean Ghering
#  http://www.shaungehring.com/2013/01/03/raspberry-pi-project-1-pandora-streamer/


import os, sys
import SJB_Pandora as pandora
from time import sleep

# recommended file locations for storing song and station infomation
nowplayingFile = '/home/pi/.config/pianobar/nowplaying'
stationFile = '/home/pi/.config/pianobar/station'
stationListFile = '/home/pi/.config/pianobar/stationList'


if __name__ == "__main__":

        # Read event type from command arguments
        event_type = sys.argv[1]

        # Read parameters from input
        params = {}
        
        for s in sys.stdin.readlines():
                param, value = s.split("=", 1)
                params[param.strip()] = value.strip()

        # Handle specific events
        if event_type == "songstart":

                info = {}
                info["song"] = params["title"]
                info["artist"] = params["artist"]
                info["album"] = params["album"]
                info["stationCount"] = params["stationCount"]
                info["stationName"] = params["stationName"]

                stations = []

                for i in range(0, int(params["stationCount"])):
                        stations.append(params["station"+str(i)])

                info["stations"] = stations

                # Write song and station info to files.
                n = open(nowplayingFile, 'w')
                n.write(info["song"] + ' -- ' + info['artist'])
                n.close()
                s = open(stationFile, 'w')
                s.write(info['stationName'])
                s.close()
                n.close()
                pandora.UpdateDisplay()

                
        elif event_type == "songfinish":
                pass
        elif event_type == "usergetstations":
                pass

