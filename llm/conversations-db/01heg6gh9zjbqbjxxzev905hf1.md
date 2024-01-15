**Prompt:**
 llm logs list -n 1 --json | jq -r '.[] | "**ID:** \n\n" + .id + "\n\n#### Model\n\n" + .response_json.model + "\n\n#### Prompt\n\n" + .prompt + "\n\n#### System\n\n" + .system + "\n\n#### Response\n\n" + .response + "\n\n#### Options\n\n" + (.options_json | tojson) + "\n\n#### Duration\n\n" + .duration_ms + "\n\n#### Datetime_utc\n\n" + .datetime_utc + "\n\n#### Conversation ID\n\n" + .conversation_id'
jq: error (at <stdin>:34): string ("**ID:** \n...) and number (12646) cannot be added

**Response:**
The error message is indicating that you're trying to concatenate a string with a number, which isn't allowed in `jq`. 

You need to convert the number to a string before concatenating. You can do this using the `tostring` function in `jq`. Here's how you can modify your command:

```bash
llm logs list -n 1 --json | jq -r '.[] | "**ID:** \n\n" + .id + "\n\n#### Model\n\n" + .response_json.model + "\n\n#### Prompt\n\n" + .prompt + "\n\n#### System\n\n" + .system + "\n\n#### Response\n\n" + .response + "\n\n#### Options\n\n" + (.options_json | tojson) + "\n\n#### Duration\n\n" + (.duration_ms | tostring) + "\n\n#### Datetime_utc\n\n" + .datetime_utc + "\n\n#### Conversation ID\n\n" + .conversation_id'
```

This will convert the `duration_ms` value to a string before concatenating it with the rest of the string.

<details><summary>Metadata</summary>

- Duration: 16141 ms
- Datetime: 2023-11-05T16:54:13.809176
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

