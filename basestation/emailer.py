#!/usr/bin/python
# Base Station
# Performs the function of a base station for receiving and publishing data.
#   - Reads data from UART on Raspberry Pi (serial port speed 115200)
#   - Validates and parses data
#   - Inserts the data into MYSQL database
#   - Sends out email alerts
#   - minicom check: minicom -b 115200 -o -D /dev/ttyAMA0
# Author Dan Becker dan@danbecker.info
# Based on PlantFriends by Dickson Chow http://dicksonchow.com

# Import modules
import time
import sys
import threading
import string
import smtplib
import getpass
from datetime import datetime

# Information for email. This will be used to send out emails.
emailSubj = 'Weather Station KTXAUSTI464 Alert'
emailFrom = 'dan.o.becker@gmail.com'
emailSMTP = 'smtp.gmail.com:587' #TLS/STARTTLS
# emailSMTP = 'smtp.gmail.com:465' #SSL
# emailPass = 'yourpassword'
emailPass = getpass.getpass( 'Enter ' + emailFrom + ' password: ')
# These are email address that you want to send alerts TO.
# emailList = ['personal_email@address.com','PHONENUMBER@yourMobileCarrier.com']
emailList = ['dan@danbecker.info']
emailSig = 'Thanks, Dan Becker at KTXAUSTI464'

# This function is for sending out emails.
def alertEmail(msg):
    for emailDest in emailList:
        emailBody = string.join((
			"From: %s" % emailFrom,
			"To: %s" % emailDest,
			"Subject: %s" % emailSubj,
			"",
			msg + "\r\n\r\n%s\r\n\r\n" % emailSig,
			), "\r\n")
        # print 'email body=\n' + emailBody
        server = smtplib.SMTP(emailSMTP) # Gmail SMTP server address
        server.ehlo()
        server.starttls()
        server.login(emailFrom, emailPass)
        server.sendmail(emailFrom, [emailDest], emailBody)
        server.quit()

# Send an email with a thread
emailMsg = 'At ' + datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S') + ' the temperature is 72F.'
asyncSend = threading.Thread(target=alertEmail(emailMsg))
asyncSend.start()
