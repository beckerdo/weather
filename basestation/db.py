#!/usr/bin/python
# DB
# Demonstrates some basic DB work#   - Reads data from UART on Raspberry Pi (serial port speed 115200)
#   - Creates dummy data (timestamp)
#   - Inserts the data into MYSQL database
# Author Dan Becker dan@danbecker.info
# Based on PlantFriends by Dickson Chow http://dicksonchow.com

# Import modules
import time
import sys
import serial # allows us to use the serial port directly
import threading # allows us to do multithreading
import string
import smtplib # allows us to send out emails
import MySQLdb as mdb # interact with MySQL

# Declare database variables. Change accordingly.
con = mdb.connect('localhost', 'dummyuser', 'password', 'dummydb');

# Continue til killed.		
while 1:
	time.sleep(11); # Sleep to prevent excess data 
		
	# Create dummy data
	ErrorLvl = 0
	SoilMoist = 1
	TempC = 22
	Humid = 55
	Voltage = 33
					
	# Check if a table for the NodeID exits. If not, create one.
	tableCheck = "SHOW TABLES LIKE '{}'".format (AliasID)

	with con:
		cur = con.cursor()
		cur.execute(tableCheck)
		tableResult = cur.fetchone()
					
		# Doesn't exist, create table. (invert boolean)
		if not tableResult:
			# print "no"
			with con:
				# Create the table
				nodeTable = "CREATE TABLE {}(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, DateTime TIMESTAMP, ErrorLvl INT, SoilMoist INT, TempC INT, Humid INT, Voltage FLOAT)".format (AliasID)
			    # Insert dummy data for the first row
				nodeDummy = "INSERT INTO {}(DateTime, ErrorLvl, SoilMoist, TempC, Humid, Voltage) VALUES (CURRENT_TIMESTAMP,'0','0','0','0','0')".format (AliasID)
				cur = con.cursor()
				cur.execute(nodeTable)
				cur.execute(nodeDummy)
			
			
			# Insert sensor node data into the database
			datasql = "INSERT INTO {}(DateTime, ErrorLvl, SoilMoist, TempC, Humid, Voltage) VALUES (CURRENT_TIMESTAMP,'{}','{}','{}','{}','{}')".format (AliasID,ErrorLvl,SoilMoist,TempC,Humid,Voltage)
			with con:
				cur = con.cursor()
				cur.execute(datasql)