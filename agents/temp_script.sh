#!/bin/bash

echo "# LLM Conversation Log"

# Iterate over each provided conversation ID
for cid in "$@"; do
  # Fetch and format the conversation details
  conversation_details=$(llm logs list --cid "$cid" --json | jq -r '
    .[] |
    "## Conversation ID: \(.conversation_id)\n\n" +
    "### Response Details\n\n" +
    "* **Model:** \(.model)\n" +
    "* **Token Count:** \(.response | split("\n") | .[0] | split(" ") | length)\n" +
    "* **Token Rate:** \((.response | split("\n") | .[0] | split(" ") | length) / (.duration_ms / 1000) ) tokens/s\n" +
    "* **Duration:** \(.duration_ms) ms\n" +
    "* **Datetime (UTC):** \(.datetime_utc)\n\n" +

    "### View Details\n\n" +
    "<details>\n" + 
    "<summary>Click to expand</summary>\n\n" +
    
    "<details>\n" +
    "<summary><b>Prompt</b></summary>\n" +
    "```\n" + .prompt + "\n```\n\n" +
    "```\n" + (.system // "N/A") + "\n```\n\n" +
    "</details>\n\n" +
    
    "<details>\n" +
    "<summary><b>Response</b></summary>\n" +
    "```\n" + .response + "\n```\n\n" +
    "```\n" + ((.options_json | tostring) // "N/A") + "\n```\n\n" +
    "</details>\n" +
    "</details>\n"
  ')

  # Output the formatted conversation details
  echo "$conversation_details"
done
