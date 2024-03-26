#!/bin/bash

echo "# LLM Conversation Log"

# Iterate over the list of cids
for cid in "$@"; do
    conversation_details=$(llm logs list --cid "$cid" --json | jq -r '
        .[] | 
        "## Conversation ID: " + .conversation_id + "\n" +
        "### Response ID: " + .id + "\n" +
        "**Model:** " + .model + "\n" +
        ( "Token Count: " + ( .response | split("\n\"") | .[0] | split(" ") | length | tostring ) + "\n" ) +
        ( "Token Rate: " + ( ( .response | split("\n\"") | .[0] | split(" ") | length ) / ( .duration_ms / 1000 ) | tostring ) + " tokens/s\n" )  +
        "<details>\n<summary><strong>Prompt</strong></summary>\n" + .prompt + "\n</details>\n" +
        "<details>\n<summary><strong>System</strong></summary>\n" + (.system // "") + "\n</details>\n" +
        "<details>\n<summary><strong>Response</strong></summary>\n" + .response + "\n</details>\n" +
        "<details>\n<summary><strong>Options</strong></summary>\n" + ((.options_json | tostring) // "") + "\n</details>\n" +
        "**Duration:** " + (.duration_ms | tostring) + " ms\n" +
        "**Datetime (UTC):** " + .datetime_utc'
    )

    echo -e "$conversation_details"
done