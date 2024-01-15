**Prompt:**
A BASH SCRIPT USING STANDARD LINUX TOOLS TO CONSUME A REST SERVICE. I should be able to pass in some arbitrary text content that will be sent to the REST service. The service should save the request in a local SQLite database, and send the auto increment ID to the REST service along with a response URL which can, for now, be localhost:8080/restreply/

Check if any non-standard commands are installed and install them if required, including sqlite, and create the sqlite db if it does not already exist.

#!/bin/bash


**Response:**
#
if ! [ -x "$(command -v curl)" ]; then
  echo 'Error: curl is not installed.' >&2
  exit 1
fi


echo "Creating SQLite database..."
sqlite3 rest_api.db < create-table.sql

read -p "Enter text to send to the REST service (default=Hello World):" message
if [ "$message" == "" ]; then
    message="Hello World!"
fi;

# get_id=$(echo $RANDOM)

 echo "Sending request..."
  curl --silent \
  	-H 'Content-Type: application/json' -d '{"text":"'"$message"'"}' http://localhost:8080/restapi | jq . > restreply.txt

  read -p "Enter the response URL (default=http://localhost:8080/restreply):" url
  if [ "$url" == "" ]; then
    url="http://localhost:8080/restreply/"$get_id".json"
fi;

 echo "Sending reply..."
   curl --silent \
     -H 'Content-Type: application/json'  http://localhost:8080/restapi | jq . > restreply.txt

  sqlite3 rest_api.db < insert-into-table.sql
  sqlite3 rest_api.db "UPDATE requests SET responseurl = '$url', textsent=''"$message"'' WHERE id=$get_id;"


<details><summary>Metadata</summary>

- Duration: 77631 ms
- Datetime: 2023-11-02T21:07:54.228804
- Model: Unknown

</details>

**Options:**
```json
{}
```

