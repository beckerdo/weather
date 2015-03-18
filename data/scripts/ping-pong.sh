#!/bin/bash
# Ping pong a post between two instance of a host. 
#    $1 is the repetition counter (default=4)
#    $2 is the delay between posts (seconds) (default=0)
# Author: Dan Becker
COUNTER=${1:-4}
DELAY=${2:-0}
echo "Ping pong repetition counter=$COUNTER"
until [  $COUNTER -lt 1 ]; do
   # echo "PING pong"
   ./post-json.sh https://standindecision-3075.lvs01.dev.ebayc3.com:8443/v1/standindecision/decision/ trans.json m123 1 fi123
   sleep $DELAY
   ./post-json.sh https://standindecision-7097.lvs01.dev.ebayc3.com:8443/v1/standindecision/decision/ trans.json m123 1 fi123
   sleep $DELAY
   let COUNTER-=1
done