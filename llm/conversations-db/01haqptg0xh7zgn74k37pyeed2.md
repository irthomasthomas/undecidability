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
To convert the given JSON into a pretty GitHub Markdown issue, you can use the following script:

```python
import json

def generate_github_issue(json_data):
    issue_template = """
### {prompt}

**Conversation ID:** {conversation_id}
**Duration:** {duration_ms} ms
**Created Date:** {datetime_utc}
**Conversation Name:** {conversation_name}

#### Response
{content}

#### Meta Data
- **Role:** {role}
- **Finish Reason:** {finish_reason}
- **ID:** {id}
- **Object:** {object}
- **Model:** {model}
- **Created:** {created}
"""

    data = json.loads(json_data)

    issue_markdown = issue_template.format(
        prompt=data['prompt'],
        conversation_id=data['conversation_id'],
        duration_ms=data['duration_ms'],
        datetime_utc=data['datetime_utc'],
        conversation_name=data['conversation_name'],
        content=data['response_json']['content'],
        role=data['response_json']['role'],
        finish_reason=data['response_json']['finish_reason'],
        id=data['response_json']['id'],
        object=data['response_json']['object'],
        model=data['response_json']['model'],
        created=data['response_json']['created']
    )

    return issue_markdown

# Example usage
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

This script defines the `generate_github_issue` function, which takes the JSON data as input and uses it to fill in the template for the GitHub issue. The resulting issue is returned as a string.

You can adjust the template as per your requirements, and modify the script to handle the JSON data from your desired source.

<details><summary>Metadata</summary>

- Duration: 22612 ms
- Datetime: 2023-09-19T21:51:04.648123
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

