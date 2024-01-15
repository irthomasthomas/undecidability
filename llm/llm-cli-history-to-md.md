To save every conversation to a markdown file, here are the steps you would need to take using SQL queries and scripting (e.g., Python/bash scripting):

1. Extract conversations.
2. Construct markdown documents.
3. Save markdown documents.

Assuming we're using a scripting language like Python with a library for SQLite manipulation (e.g., `sqlite3`):

```python
import sqlite3
import json

# Connect to the database
conn = sqlite3.connect('logs.db')

# 1. Extract conversations:
# Query to get all related responses for each conversation, ordered by datetime.
query = '''
    SELECT r.prompt, r.response, r.options_json, r.duration_ms, r.datetime_utc, r.response_json, c.id
    FROM responses r
    JOIN conversations c ON r.conversation_id = c.id
    ORDER BY r.datetime_utc ASC
'''
cursor = conn.execute(query)

# 2. Construct markdown documents:
current_conversation_id = None
markdown_content = ""

for row in cursor:
    prompt, response, options_json, duration_ms, datetime_utc, response_json, conversation_id = row
    if conversation_id != current_conversation_id:
        if current_conversation_id is not None:
            # Save previous conversation to its markdown file
            with open(f"{current_conversation_id}.md", 'w') as file:
                file.write(markdown_content)
            markdown_content = ""  # Reset for new conversation
        current_conversation_id = conversation_id

    # JSON loading for extracting model
    response_json_data = json.loads(response_json)
    model = response_json_data.get('model', 'Unknown')

    # Construct markdown content for the current row
    markdown_content += f"**Prompt:**\n{prompt}\n\n**Response:**\n{response}\n\n<details><summary>Metadata</summary>\n\n- Duration: {duration_ms} ms\n- Datetime: {datetime_utc}\n- Model: {model}\n\n</details>\n\n**Options:**\n```json\n{options_json}\n```\n\n"

# 3. Save last markdown document:
if current_conversation_id is not None:
    # Don't forget to save the last conversation if there were any
    with open(f"{current_conversation_id}.md", 'w') as file:
        file.write(markdown_content)

# Close the connection to the database
conn.close()
```

This script iterates over rows of related responses, joining the data on `conversation_id`. For each new conversation, the previous one is saved to a markdown file named with the `conversation_id`. Each prompt/response pair, along with their metadata and options, are formatted in Markdown collapsible details tags. The script concludes by closing the database connection. This assumes that conversation IDs are unique and valid for use as filenames. If not, some sanitization might be necessary.

Remember to adapt the file paths and database connection as needed for your environment.
