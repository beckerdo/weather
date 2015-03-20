#!/usr/bin/python
# Serial Talk
# Shows how Python can talk to serial port.
#   - Reads data from UART on Raspberry Pi (serial port speed 115200) 
#   - minicom check: minicom -b 115200 -o -D /dev/ttyAMA0
# Author Dan Becker dan@danbecker.info
# Based on PlantFriends by Dickson Chow http://dicksonchow.com

# Import modules
import time
import sys
import serial # allows us to use the serial port directly
import threading # allows us to do multithreading
import string

# Delare serial port settings
ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=0)
		
# Open the serial port.
ser.open()
try:
	while 1:
		
		time.sleep(1); #Sleep for 1 sec to prevent node spamming (if a node goes crazy)
		
		# Read the serial buffer.
		serdata = ser.readline()		
		
		# The serial port likes to insert random spaces so we just want the lines ones that actually have data.
		if len(serdata)>3:
					
			# Clean the data. Strip any extra spaces.
			data = serdata.strip()			
			
            # Perform data parse etc.
			ErrorLvl = 0
            
			# Check if the sensor node marked an error. Check the type of error. Generate message.
			if int(ErrorLvl) > 0:					
				# Reset the email message
				ErrorMsg = " \r\n"
								
				# Send out email. This gets spawned as a thread so it doesn't block.
				OhNos = threading.Thread(target=alertMail(ErrorMsg))
				OhNos.start()				
																	
except KeyboardInterrupt:
	ser.close()