**Prompt:**
logs list -q "Experiment User msg" --json | jq
[
  {
    "id": "01h9tcvvqxgfvnwdx12143g659",
    "model": "gpt-3.5-turbo",
    "prompt": "Experiment User msg",
    "system": "Experiment System msg",
    "prompt_json": {
      "messages": [
        {
          "role": "system",
          "content": "Experiment System msg"
        },
        {
          "role": "user",
          "content": "Experiment User msg"
        }
      ]
    },
    "options_json": {},
    "response": "Experiment Assistant msg",
    "response_json": {
      "content": "Experiment Assistant msg",
      "role": "assistant",
      "finish_reason": "stop",
      "id": "chatcmpl-7wV371107O34mOyJhn2NgiGIgihWd",
      "object": "chat.completion.chunk",
      "model": "gpt-3.5-turbo-0613",
      "created": 1694176733
    },
    "conversation_id": "01h9tcvvq3p58g7fsxgfdv9vqr",
    "duration_ms": 556,
    "datetime_utc": "2023-09-08T12:39:27.158398",
    "conversation_name": "Experiment User msg",
    "conversation_model": "gpt-3.5-turbo"
  }
]

**Response:**
You can use the following jq query to extract the desired fields from the JSON object:

```bash
jq '[.[] | {id, prompt, system, options_json, response_json, conversation_id, duration_ms, datetime_utc, conversation_name}]'
```

This will return a new JSON object with the specified fields:

```json
[
  {
    "id": "01h9tcvvqxgfvnwdx12143g659",
    "prompt": "Experiment User msg",
    "system": "Experiment System msg",
    "options_json": {},
    "response_json": {
      "content": "Experiment Assistant msg",
      "role": "assistant",
      "finish_reason": "stop",
      "id": "chatcmpl-7wV371107O34mOyJhn2NgiGIgihWd",
      "object": "chat.completion.chunk",
      "model": "gpt-3.5-turbo-0613",
      "created": 1694176733
    },
    "conversation_id": "01h9tcvvq3p58g7fsxgfdv9vqr",
    "duration_ms": 556,
    "datetime_utc": "2023-09-08T12:39:27.158398",
    "conversation_name": "Experiment User msg"
  }
]
```

<details><summary>Metadata</summary>

- Duration: 9508 ms
- Datetime: 2023-09-08T12:55:38.103587
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

