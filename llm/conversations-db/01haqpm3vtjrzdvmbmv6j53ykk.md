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
Certainly! Here's a shell script using jq to prettify the JSON and convert it into GitHub Markdown for an issue:

```shell
#!/bin/bash

# Assuming the JSON is stored in a file named "input.json"
input_file="input.json"

# Read the JSON and prettify it using jq
json=$(jq '.' $input_file)

# Extract the required fields from the JSON
id=$(echo $json | jq -r '.id')
prompt=$(echo $json | jq -r '.prompt')
content=$(echo $json | jq -r '.response_json.content')
role=$(echo $json | jq -r '.response_json.role')
finish_reason=$(echo $json | jq -r '.response_json.finish_reason')
model=$(echo $json | jq -r '.response_json.model')
created=$(echo $json | jq -r '.response_json.created')
datetime_utc=$(echo $json | jq -r '.datetime_utc')
conversation_name=$(echo $json | jq -r '.conversation_name')

# Generate the GitHub Markdown issue
issue_text="**ID:** $id
**Prompt:** $prompt
**Content:** $content
**Role:** $role
**Finish Reason:** $finish_reason
**Model:** $model
**Created:** $created
**Datetime UTC:** $datetime_utc
**Conversation Name:** $conversation_name"

# Print the Markdown issue
echo "$issue_text"
```

Save this script to a file, e.g., `json_to_github_issue.sh`, and make it executable (`chmod +x json_to_github_issue.sh`). Then, you can run the script by executing `./json_to_github_issue.sh`, and it will print the generated GitHub Markdown issue.

Please note that you may need to install `jq` before running the script. You can usually install it using your system's package manager (`apt`, `yum`, `brew`, etc.).

<details><summary>Metadata</summary>

- Duration: 14793 ms
- Datetime: 2023-09-19T21:47:43.408381
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

