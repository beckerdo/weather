#!/usr/bin/python
# FileParse
#   - Reads a file line by line.
#   - Filters good lines that meet a certain pattern
#   - Extracts fields of good lines.
#   - Aggregate/Map/Reduce
# Author Dan Becker dan@danbecker.info

# Import modules
import time
import sys
import threading
import string
import smtplib
import getpass
from datetime import datetime
import re

lineFilter = '^\s*R\[.+'
lineFilterRE = re.compile(lineFilter)
fields= '^\s*R\[(?P<packet>\d+)\]\[(?P<device>\d+)\]\s*\"(?P<properties>[^\"]*)\" - ack ts=(?P<timestamp>.*).*'
timeStampRE = '((1\d{3})|(20\d{2}))-((0\d)|(1[0-2]))-(([1-2]\d)|(3[0-1])) (([0-1]\d)|(2[0-3])):([0-5]\d):([0-5]\d)'
fieldsRE = re.compile( fields )
keyAggr = ['tid','sid']

# Returns a dict organized by given data keys
# For example, consider a file along these lines.
#    R[1][2] "tid=t1, sid=s0, tf=68.1, hp=72, vvr=5.44, tm=594" - ack ts=2015-03-19 09:51:45.
#    R[2][2] "tid=t1, sid=s1, tf=67.2, pia=29.03, pir=29.94" - ack ts=2015-03-19 09:51:55.
# Results
# values={
    't1.s2.uvi': [('2015-03-19 09:52:05', '0.02'), ('2015-03-19 09:54:05', '0.04')], 
    't1.s1.pia': [('2015-03-19 09:51:55', '29.03'), ('2015-03-19 09:53:55', '29.22')]}
def parseSamples(filename):
  values = {} # Contains the returned values.
  input_file = open(filename, 'r')
  for line in input_file:
    # Filter out candidate lines with an easy RE.
    lineMatch = lineFilterRE.match(line)
    if lineMatch:
      # Match on packet, devvice, properties, timestamp group
      groups = fieldsRE.match(line)
      if groups:
         packet = groups.group('packet')
         timestamp = groups.group('timestamp')
         properties = groups.group('properties')
         print 'packet,time,props=' + packet + ',' + timestamp + ',' + properties
         # Break properties into keys,values list
         words = re.findall(r"[\w\.]+", properties )
         # print 'words=' + str( words )
         keyComp = ''
         # Go through list two at a time.
         for i  in range( 0, len( words ), 2 ):
            key = words[ i ] 
            value = words[ i + 1 ] 
            if key in keyAggr:
                # Build a dot delimited compound key out of the values.
                if len( keyComp ) > 0:
                    keyComp += '.'
                keyComp += value
            else:
                # Build a dot delimited compund key with this key.
                # print 'keyComp,value=' + keyComp + '.' + key + '=' + value
                keyCurr = keyComp + '.' + key
                if keyCurr in values:
                    # Add a (time,value) tuple to this list.
                    currValue = values[ keyCurr ]
                    currValue.append( (timestamp,value) )
                    values[ keyCurr ] = currValue
                else:
                    # Create a (time,value) tuple list.
                    values[ keyCurr ] = [ (timestamp, value) ] 
  input_file.close()  # Not strictly required, but good form.
  return values

# Given two timestamps, makes wild cards of dissimilar fields
# Once a wild card occurs, all following digits have wild cards
# For example, 2015-03-15 10:31:25 and 2015-03-15 10:32:05 yields 2015-03-15 10:3X:XX 
def timeStampWild(ts1,ts2,wildChar='X'):
    delimiters = [ '-', ':', '/' ]
    goneWild = False
    ts = ''
    for t1,t2 in zip(ts1,ts2):
        if t1 in delimiters:
            ts += t1
        elif (t1 != t2) or goneWild:
            ts += wildChar 
            goneWild = True
        else:
            ts += t1 
    return ts
 
# Basic command line argument parsing code
# For example ./fileParser.py ../data/scripts/data.json
def main():
  if len(sys.argv) != 3:
    print 'usage: ./fileParser.py {--option1 | --option2} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  # Use options to perform fancy things.
  if option == '--option1':
    print 'values=' + str( parseSamples(filename) )
  elif option == '--option1':
    print 'values=' + str( parseSamples(filename) )
  else:
    print 'unknown option: ' + option
    sys.exit(1)
    
  # Test capabilities of timeStampWild.    
  t1 = '2015-03-15 10:31:04'
  t2 = '2015/03/15 10:32:44'
  print 't1 (' + t1 + ') or t2(' + t2 + ') => ' + timeStampWild( t1, t2 )

if __name__ == '__main__':
  main()