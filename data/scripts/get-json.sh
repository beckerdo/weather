# GET a JSON entity from the host. 
#    $1 is resource endpoint - example http://localhost:8080/rest/messages
#    $2 is the resource id - example abc123
# Author: Dan Becker
curl -sv -X GET $1/$2  --header "Accept: application/json" --insecure
