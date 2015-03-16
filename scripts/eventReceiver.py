#!/usr/bin/env python
#From Sean Ghering

import os, sys
import SJB_Pandora

##import sys, time, os, socket
##import pickle
##import pandoraUtils

nowplayingFile = '/home/pi/.config/pianobar/nowplaying'
stationFile = '/home/pi/.config/pianobar/station'

if __name__ == "__main__":

	# Read event type from command arguments
	if len(sys.argv) < 2:
		pandoraUtils.log("Error reading event type from command arguments")

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

		#pandoraUtils.setShared(info)
		f = open(nowplayingFile, 'w')
		f.write(info["song"] + ' -- ' + info['artist'])
		#os.system('echo ' + info['song'] + ' -- ' + info['artist'] + ' > /home/pi/.config/pianobar/nowplaying')
		s = open(stationFile, 'w')
		s.write(info['stationName'])
		#os.system('echo ' + info['stationName'] + ' > /home/pi/.config/pianobar/station')
		SJB_Pandora.UpdateDisplay()
 

		
	elif event_type == "songfinish":
		pass
	elif event_type == "usergetstations":
		pass

    
SJB_Pandora.UpdateDisplay()

