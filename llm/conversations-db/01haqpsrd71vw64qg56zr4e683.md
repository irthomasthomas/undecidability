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
Here is a script written in Python that takes the provided JSON and generates a pretty GitHub Markdown issue:

```python
import json

def generate_github_issue(json_data):
    issue_template = """
**Prompt:** {prompt}

**Response:**
{content}

**Model Used:** {model}

**Conversation ID:** {conversation_id}

**Duration:** {duration_ms}ms

**Timestamp:** {datetime_utc}
"""

    data = json.loads(json_data)
    issue = issue_template.format(
        prompt=data["prompt"],
        content=data["response_json"]["content"],
        model=data["response_json"]["model"],
        conversation_id=data["conversation_id"],
        duration_ms=data["duration_ms"],
        datetime_utc=data["datetime_utc"]
    )

    return issue

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

issue = generate_github_issue(json_data)
print(issue)
```

Make sure you have the `json` module available in your Python environment in order to run this script. You can customize the issue template as per your requirements.

<details><summary>Metadata</summary>

- Duration: 16901 ms
- Datetime: 2023-09-19T21:50:46.176956
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

