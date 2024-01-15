**Prompt:**
Include the name in a query like this: llm logs list --cid "01h9g07styj0gjjvdtaf9xs7ah" --json | jq '.[] | [.datetime_utc, .conversation_id, .model, .prompt, .response ]'

**Response:**
The query with the included name would look like this:

llm logs list --cid "01h9g07styj0gjjvdtaf9xs7ah" --json | jq '.[] | [.datetime_utc, .name, .conversation_id, .model, .prompt, .response ]'

<details><summary>Metadata</summary>

- Duration: 6688 ms
- Datetime: 2023-09-06T14:14:44.226709
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

