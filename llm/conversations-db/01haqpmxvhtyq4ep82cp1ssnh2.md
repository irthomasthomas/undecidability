**Prompt:**
Think carefully. As the resident shell script and github expert, can you reccomend a script to turn this json into a pretty github markdown issue? \n\n  {
    "id": "01h9d9qgd0t18dhyd3fst30pbk",
    "prompt": "Goal Oriented Userinterface",
    "system": null,
    "options_json": {},
    "response_json": {
      "content": "A goal-oriented user interface is a user interface design approach ...",
      "role": "assistant",
      "finish_reason": "stop",
      "id": "chatcmpl-7ueiIBtnRymZfKlsd8XR6xXfIHwM4",
      "object": "chat.completion.chunk",
      "model": "gpt-3.5-turbo-0613",
      "created": 1693737226
    },
    "conversation_id": "01h9d9qgcb97rf0ddkfpz19bge",
    "duration_ms": 13225,
    "datetime_utc": "2023-09-03T10:34:18.465893",
    "conversation_name": "Goal Oriented Userinterface"
  }

**Response:**
Certainly! Here's a shell script that turns the provided JSON into a pretty GitHub markdown issue:

```bash
#!/bin/bash

# Set the JSON input as a variable
JSON='{
    "id": "01h9d9qgd0t18dhyd3fst30pbk",
    "prompt": "Goal Oriented Userinterface",
    "system": null,
    "options_json": {},
    "response_json": {
      "content": "A goal-oriented user interface is a user interface design approach ...",
      "role": "assistant",
      "finish_reason": "stop",
      "id": "chatcmpl-7ueiIBtnRymZfKlsd8XR6xXfIHwM4",
      "object": "chat.completion.chunk",
      "model": "gpt-3.5-turbo-0613",
      "created": 1693737226
    },
    "conversation_id": "01h9d9qgcb97rf0ddkfpz19bge",
    "duration_ms": 13225,
    "datetime_utc": "2023-09-03T10:34:18.465893",
    "conversation_name": "Goal Oriented Userinterface"
}'

# Parse the JSON to extract necessary data
id=$(echo $JSON | jq -r '.id')
prompt=$(echo $JSON | jq -r '.prompt')
content=$(echo $JSON | jq -r '.response_json.content')
role=$(echo $JSON | jq -r '.response_json.role')
finish_reason=$(echo $JSON | jq -r '.response_json.finish_reason')
model=$(echo $JSON | jq -r '.response_json.model')
datetime_utc=$(echo $JSON | jq -r '.datetime_utc')

# Generate the GitHub markdown issue
echo "## Issue: $id"
echo ""
echo "**Prompt:** $prompt"
echo ""
echo "**Content:**"
echo "$content"
echo ""
echo "**Role:** $role"
echo ""
echo "**Finish Reason:** $finish_reason"
echo ""
echo "**Model:** $model"
echo ""
echo "**Datetime UTC:** $datetime_utc"
echo ""
```

To use this script, you'll need to have `jq` installed, which is a command-line JSON processor. You can install it on macOS using Homebrew (`brew install jq`), on Ubuntu using apt (`sudo apt-get install jq`), or on other systems by following the official installation instructions available at https://stedolan.github.io/jq/download/.

Save the script in a file (e.g., `json_to_github_issue.sh`), make it executable (`chmod +x json_to_github_issue.sh`), and then run it (`./json_to_github_issue.sh`). It will output the GitHub markdown issue in the console, which you can copy and paste into a GitHub issue.

Please note that this script assumes the provided JSON structure remains consistent. If the structure changes, adjustments may be necessary.

<details><summary>Metadata</summary>

- Duration: 25088 ms
- Datetime: 2023-09-19T21:47:59.727956
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

