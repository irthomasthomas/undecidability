**Prompt:**
my logs.db has a table called responses that contains logs of my interactions with the gpt api. 
**responses .schema**:
CREATE TABLE [responses] (
   [id] TEXT PRIMARY KEY,
   [model] TEXT,
   [prompt] TEXT,
   [system] TEXT,
   [prompt_json] TEXT,
   [options_json] TEXT,
   [response] TEXT,
   [response_json] TEXT,
   [conversation_id] TEXT REFERENCES [conversations]([id]),
   [duration_ms] INTEGER,
   [datetime_utc] TEXT
);
CREATE TRIGGER [responses_ai] AFTER INSERT ON [responses] BEGIN
  INSERT INTO [responses_fts] (rowid, [prompt], [response]) VALUES (new.rowid, new.[prompt], new.[response]);
END;
CREATE TRIGGER [responses_ad] AFTER DELETE ON [responses] BEGIN
  INSERT INTO [responses_fts] ([responses_fts], rowid, [prompt], [response]) VALUES('delete', old.rowid, old.[prompt], old.[response]);
END;
CREATE TRIGGER [responses_au] AFTER UPDATE ON [responses] BEGIN
  INSERT INTO [responses_fts] ([responses_fts], rowid, [prompt], [response]) VALUES('delete', old.rowid, old.[prompt], old.[response]);
  INSERT INTO [responses_fts] (rowid, [prompt], [response]) VALUES (new.rowid, new.[prompt], new.[response]);
END;
**conversations .schema**:
CREATE TABLE [conversations] (
   [id] TEXT PRIMARY KEY,
   [name] TEXT,
   [model] TEXT
);

I need to save every conversation to a markdown file. 
Some conversations are contained in a single response row.
Other conversations consist of MULTIPLE response rows and should be cated by conversation_id

The markdown document should consist of:
prompt
response
options_json
prompt
response
options_json
... until all parts of the conversation are included.

Each prompt/response pair should include a colapsible md field to record:
duration_ms
datetime_utc
response_json.model 
response_json contains, e.g. {"content": " No", "role": null, "finish_reason": null, "logprobs": [{"text": " No", "top_logprobs": [{" No": -1.2232164, " no": -1.5087332}]}, {"text": "", "top_logprobs": []}], "id": "cmpl-8Lb2al4kbNvcfYhfOzqkmgHIhTe50", "object": "text_completion", "model": "gpt-3.5-turbo-instruct", "created": 1700157964}




**Response:**
Create a Python script to fetch, organize, and save the data from `responses` and `conversations` tables into Markdown files.

1. Connect to the SQLite database and fetch necessary data.
2. Organize the conversation blocks.
3. Generate Markdown content with collapsible sections.
4. Save to Markdown files.

Code overview:

```python
import sqlite3
import json
import os

def query_database(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, prompt, response, options_json, duration_ms, datetime_utc, response_json, conversation_id FROM responses ORDER BY datetime_utc")
        return cursor.fetchall()

def group_conversations(responses):
    conversations = {}
    for row in responses:
        conv_id = row[7]
        if conv_id in conversations:
            conversations[conv_id].append(row)
        else:
            conversations[conv_id] = [row]
    return conversations

def markdown_collapsible(prompt, response, options_json, duration_ms, datetime_utc, response_json):
    model = json.loads(response_json).get("model", "N/A")
    return f"""
<details>
<summary>Prompt\n\n{prompt}\n\nResponse\n\n{response}\n\nOptions JSON\n\n{options_json}</summary>
Duration (ms): {duration_ms}
Datetime (UTC): {datetime_utc}
Model: {model}
</details>
"""

def save_to_markdown(conversations, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for conv_id, messages in conversations.items():
        markdown_content = ""
        for msg in messages:
            markdown_content += markdown_collapsible(*msg[1:6])
        with open(os.path.join(output_dir, f"{conv_id}.md"), 'w') as md_file:
            md_file.write(markdown_content)

if __name__ == "__main__":
    db_path = "path_to_logs.db"  # Update with the actual database path.
    output_dir = "conversations_markdown"  # Update with the desired output directory.
    
    responses = query_database(db_path)
    conversations = group_conversations(responses)
    save_to_markdown(conversations, output_dir)
```

Explanation:
- Connect to `logs.db` using `sqlite3.connect`.
- Retrieve data from the `responses` table, ordered by `datetime_utc` to maintain conversation flow.
- Group rows by `conversation_id` to handle multi-row conversations.
- Convert each prompt/response/options JSON to Markdown with a collapsible section for metadata that includes `duration_ms`, `datetime_utc`, and `model` extracted from the `response_json`.
- Write the collected conversation Markdown text to separate files, one per conversation ID, in the specified output directory.

<details><summary>Metadata</summary>

- Duration: 33445 ms
- Datetime: 2024-01-14T14:40:28.158199
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

