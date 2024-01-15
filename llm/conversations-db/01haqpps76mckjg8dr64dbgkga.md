**Prompt:**
Think carefully. As the resident github expert, can you reccomend a script to turn this json into a pretty github markdown issue? \n\n  {
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
To turn the given JSON into a pretty GitHub markdown issue, you can use the following script:

```python
import json

def format_json(json_data):
    return json.dumps(json_data, indent=4)

def create_github_issue(json_data):
    issue = f"# {json_data['prompt']}\n\n"
    issue += f"**Conversation ID**: {json_data['conversation_id']}\n\n"
    issue += f"**Duration**: {json_data['duration_ms']}ms\n\n"
    issue += f"**Datetime UTC**: {json_data['datetime_utc']}\n\n"
    issue += f"**Conversation Name**: {json_data['conversation_name']}\n\n"
    issue += "## Response JSON\n\n"
    issue += "```\n"
    issue += format_json(json_data['response_json'])
    issue += "\n```\n"
    return issue

# JSON data
json_data = {
    "id": "01h9d9qgd0t18dhyd3fst30pbk",
    "prompt": "Goal Oriented Userinterface",
    "system": None,
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

# Generate GitHub issue markdown
github_issue = create_github_issue(json_data)

print(github_issue)
```

This script defines two helper functions: `format_json` to format the JSON as a string with indentation, and `create_github_issue` to generate the GitHub issue markdown using the provided JSON data.

The output will be the GitHub issue markdown, which you can then copy and paste into a GitHub issue to render it in a readable format.

<details><summary>Metadata</summary>

- Duration: 19912 ms
- Datetime: 2023-09-19T21:49:05.693098
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

