**Prompt:**
Turn this into a click cli app: import sqlite3
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

**Response:**
Install `click` if you haven't already:

```shell
pip install click
```

Refactor the code with `click`:

```python
import click
import sqlite3
import json
import os

@click.command()
@click.option('--db_path', required=True, type=click.Path(exists=True), help='Path to the SQLite database file.')
@click.option('--output_dir', default='conversations_markdown', type=click.Path(), help='Output directory for markdown files.')

def main(db_path, output_dir):
    responses = query_database(db_path)
    conversations = group_conversations(responses)
    save_to_markdown(conversations, output_dir)

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
    main()
```

You can run the app using:

```shell
python3 app.py --db_path path_to_logs.db
```

Replace `app.py` with the actual file name. Add any additional options as needed.

<details><summary>Metadata</summary>

- Duration: 25536 ms
- Datetime: 2024-01-14T14:47:59.984535
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

