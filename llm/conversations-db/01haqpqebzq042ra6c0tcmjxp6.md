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
To convert this JSON into a pretty Github Markdown issue, you can use the following script:

```python
import json

# Load the JSON data
json_data = '''
{
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
'''

# Parse the JSON data
data = json.loads(json_data)

# Format the data as a Github Markdown issue
issue_content = f'''
#### Issue Details

- ID: {data["id"]}
- Prompt: {data["prompt"]}
- System: {data["system"]}
- Options JSON: {data["options_json"]}

#### Response Details

- Content: {data["response_json"]["content"]}
- Role: {data["response_json"]["role"]}
- Finish Reason: {data["response_json"]["finish_reason"]}
- ID: {data["response_json"]["id"]}
- Object: {data["response_json"]["object"]}
- Model: {data["response_json"]["model"]}
- Created: {data["response_json"]["created"]}

#### Conversation Details

- Conversation ID: {data["conversation_id"]}
- Duration (ms): {data["duration_ms"]}
- Datetime UTC: {data["datetime_utc"]}
- Conversation Name: {data["conversation_name"]}
'''

# Print or save the formatted issue content
print(issue_content)
```

This script will load the JSON data, parse it, and format it as a Github Markdown issue. You can then print or save the formatted issue content as needed.

<details><summary>Metadata</summary>

- Duration: 20080 ms
- Datetime: 2023-09-19T21:49:27.182107
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

