#!/bin/bash

# Read the JSON and prettify it using jq
json=$(jq '.')

# Extract the required fields from the JSON
id=$(echo $json | jq -r '.id')
prompt=$(echo $json | jq -r '.prompt')
content=$(echo $json | jq -r '.response_json.content')
role=$(echo $json | jq -r '.response_json.role')
model=$(echo $json | jq -r '.response_json.model')
created=$(echo $json | jq -r '.response_json.created')
datetime_utc=$(echo $json | jq -r '.datetime_utc')
conversation_name=$(echo $json | jq -r '.conversation_name')

# Generate the GitHub Markdown issue
issue_text="**Prompt:** $prompt\n**Content:** $content\n**Role:** $role\n**Model:** $model\n**Created:** $created\n**Datetime UTC:** $datetime_utc\n**Conversation Name:** $conversation_name"

# Print the Markdown issue
echo "$issue_text"



#!/bin/bash
#
# while read line; do
#     input+=$line
# done
#
# # Read the JSON and prettify it using jq
# json=$(echo "$input" | jq '.')
#
# # Extract the required fields from the JSON
# id=$(echo $json | jq -r '.id')
# prompt=$(echo $json | jq -r '.prompt')
# content=$(echo $json | jq -r '.response_json.content')
# role=$(echo $json | jq -r '.response_json.role')
# model=$(echo $json | jq -r '.response_json.model')
# created=$(echo $json | jq -r '.response_json.created')
# datetime_utc=$(echo $json | jq -r '.datetime_utc')
# conversation_name=$(echo $json | jq -r '.conversation_name')
#
# # Generate the GitHub Markdown issue
# issue_text="**Prompt:** $prompt
# **Content:** $content
# **Role:** $role
# **Model:** $model
# **Datetime UTC:** $datetime_utc
# **Conversation Name:** $conversation_name"
#
# # Print the Markdown issue
# echo "$issue_text"
