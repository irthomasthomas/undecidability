#!/bin/bash

# Set the necessary variables
GITHUB_USERNAME="irthomasthomas"
GITHUB_REPO="undecidability"
GITHUB_TOKEN=$(cat $HOME/GITHUB_TOKEN)
FILE_PATH="exec_test_output.md"
COMMIT_MESSAGE="Auto commit of exec test output file"

# Base64 encode the file content
FILE_CONTENT=$(cat "$FILE_PATH" | base64 -w 0)

# Set the necessary headers
HEADERS="Authorization: token $GITHUB_TOKEN"
HEADERS+=$'\nAccept: application/vnd.github.v3+json'

# Set the API endpoint
API_ENDPOINT="https://api.github.com/repos/$GITHUB_USERNAME/$GITHUB_REPO/contents/$FILE_PATH"

# Prepare the data payload
DATA="{\"message\":\"$COMMIT_MESSAGE\",\"content\":\"$FILE_CONTENT\"}"

# Make the API request using curl
RESPONSE=$(curl -X PUT -H "$HEADERS" -d "$DATA" "$API_ENDPOINT")

# Check the response status code
STATUS_CODE=$(echo "$RESPONSE" | grep -o '"status":[0-9]\+' | grep -o '[0-9]\+')

if [ "$STATUS_CODE" == "201" ]; then
    echo "File committed successfully."
else
    echo "Failed to commit file. Status code: $STATUS_CODE"
    echo "$RESPONSE"
fi