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
fields= '^\s*R\[(?P<packet>\d+)\]\[(?P<device>\d+)\]\s*\"(?P<properties>[^\"]*)\" - ack now=(?P<timestamp>.*).*'
fieldsRE = re.compile( fields )
propDelim = ','
keyValDelim = '='
keyAggr = ['tid','sid']

# Returns a dict organized by given data keys
# For example, consider a file along these lines.
#    R[1][2] "tid=t1, sid=s0, tf=68.1, hp=72, vvr=5.44, tm=594" - ack now=2015-03-19 09:51:45.
#    R[2][2] "tid=t1, sid=s1, tf=67.2, pia=29.03, pir=29.94" - ack now=2015-03-19 09:51:55
# Results
# dict key  val       
# t1.s0.tf  [68.1,69.2,70.2,71.0]
# t1.s0.hp  [72,73,74,78,80,81]
# t1.s1.pia [29.03,29.04,29.44,]
def parseFile(filename):
  values = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    lineMatch = lineFilterRE.match(line)
    if lineMatch:
      # print line
      groups = fieldsRE.match(line)
      if groups:
         packet = groups.group('packet')
         timestamp = groups.group('timestamp')
         properties = groups.group('properties')
         print 'packet,time,props=' + packet + ',' + timestamp + ',' + properties
         words = re.findall(r"[\w\.]+", properties )
         # print 'words=' + str( words )
         keyComp = ''
         for i  in range( 0, len( words ), 2 ):
            key = words[ i ] 
            value = words[ i + 1 ] 
            if key in keyAggr:
                if len( keyComp ) > 0:
                    keyComp += '.'
                keyComp += value
            else:
                # print 'keyComp,value=' + keyComp + '.' + key + '=' + value
                keyCurr = keyComp + '.' + key
                if keyCurr in values:
                    currValue = values[ keyCurr ]
                    currValue.append( value )
                    values[ keyCurr ] = currValue
                else:
                    values[ keyCurr ] = [ value ] 
  input_file.close()  # Not strictly required, but good form.
  return values

# Given two timestamps, makes wild cards of dissimilar fields
# For example, 2015-03-15 10:31:22 and 2015-03-15 10:32:05 yields 2015-03-15 10:xx:xx 
def timeStampWild(ts1,ts2,replaceChar='X'):
    delimiters = [ '-', ':', '/' ]
    ts = ''
    for t1,t2 in zip(ts1,ts2):
        if t1 in delimiters:
            ts += t1
        elif (t1 == t2):
            ts += t1 
        else:
            ts += replaceChar 
    return ts
 
# Basic command line argument parsing code
# For example ./fileParser.py ../data/scripts/data.json
def main():
  if len(sys.argv) != 3:
    print 'usage: ./fileParser.py {--option1 | --option2} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--option1':
    print 'values=' + str( parseFile(filename) )
  elif option == '--option1':
    print 'values=' + str( parseFile(filename) )
  else:
    print 'unknown option: ' + option
    sys.exit(1)
  print timeStampWild( '2015-03-15 10:31:04', '2015/03/15 10:32:44')

if __name__ == '__main__':
  main()