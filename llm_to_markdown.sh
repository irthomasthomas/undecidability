#!/bin/bash

# Read the JSON and prettify it using jq
IFS= read -r -d '' json

# Parse the JSON object with escaped control characters
id=$(jq -r '.[0].id' <<< "$json")
echo "$id"
#
# id=$(jq -r --raw-input '.[0].id' <<< "$json")
# prompt=$(jq -r --raw-input '.[0].prompt' <<< "$json")
# content=$(jq -r --raw-input '.[0].response_json.content' <<< "$json")
# role=$(jq -r --raw-input '.[0].response_json.role' <<< "$json")
# model=$(jq -r --raw-input '.[0].response_json.model' <<< "$json")
# created=$(jq -r --raw-input '.[0].response_json.created' <<< "$json")
# datetime_utc=$(jq -r --raw-input '.[0].datetime_utc' <<< "$json")
# conversation_name=$(jq -r --raw-input '.[0].conversation_name' <<< "$json")

# Generate the GitHub Markdown issue
# issue_text="**Prompt:** $prompt
# **Content:** $content
# **Role:** $role
# **Model:** $model
# **Created:** $created
# **Datetime UTC:** $datetime_utc
# **Conversation Name:** $conversation_name"
#
# # Print the Markdown issue
# echo "$issue_text"


# Example usage
