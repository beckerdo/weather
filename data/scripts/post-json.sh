#!/bin/bash
# POST a JSON format entity to the host. 
#    $1 is the resource URL - example http://localhost:8080/rest/messages/
#    $2 is the file name containing message body - example submitdata.json. Do not escape " in the data file.
#    $3 is the merchant ID (default=m123)
#    $4 is the transaction amount cents (default=1)
#    $5 is the financial instrument ID (default=fi123)
# Author: Dan Becker
RESOURCE_URL=$1
FILE_TEMPLATE=$2
MID=${3:-m123}
AMT=${4:-1}
FID=${5:-fi123}
echo "POSTing to URL $RESOURCE_URL"
echo "Template file $FILE_TEMPLATE with substitution values $MID, $AMT, $FID"
# Grab template, replace values in template file.
CONTENTS=`cat $FILE_TEMPLATE | sed -e "s/{mID}/\$MID/" -e "s/{amt}/\$AMT/"  -e "s/{fiID}/\$FID/"`
echo "body=$CONTENTS"
curl -s -X POST --data "$CONTENTS" --header "Content-Type: application/json" --insecure $RESOURCE_URL
echo ""
