import sqlite3
import json

# Connect to the database
conn = sqlite3.connect("/home/thomas/.config/io.datasette.llm/logs.db")
print(f"Connected to database: {conn}")

# 1. Extract conversations:
# Query to get all related responses for each conversation, ordered by datetime.
query = '''
    SELECT r.model, r.prompt, r.response, r.options_json, r.duration_ms, r.datetime_utc, r.response_json, c.id
    FROM responses r
    JOIN conversations c ON r.conversation_id = c.id
    ORDER BY r.datetime_utc ASC
'''
cursor = conn.execute(query)

# 2. Construct markdown documents:
current_conversation_id = None
markdown_content = ""

for row in cursor:
    model, prompt, response, options_json, duration_ms, datetime_utc, response_json, conversation_id = row
    if conversation_id != current_conversation_id:
        if current_conversation_id is not None:
            # Save previous conversation to its markdown file
            with open(f"{current_conversation_id}.md", 'w') as file:
                file.write(markdown_content)
            markdown_content = ""  # Reset for new conversation
        current_conversation_id = conversation_id

    # JSON loading for extracting model
    if response_json:
        try:
            response_json_data = json.loads(response_json)
            model = response_json_data.get('model', 'Unknown')
        except json.decoder.JSONDecodeError:
            print(f"Could not decode JSON: {response_json}")
    # Construct markdown content for the current row
    markdown_content += f"**Prompt:**\n{prompt}\n\n**Response:**\n{response}\n\n<details><summary>Metadata</summary>\n\n- Duration: {duration_ms} ms\n- Datetime: {datetime_utc}\n- Model: {model}\n\n</details>\n\n**Options:**\n```json\n{options_json}\n```\n\n"

# 3. Save last markdown document:
if current_conversation_id is not None:
    # Don't forget to save the last conversation if there were any
    with open(f"{current_conversation_id}.md", 'w') as file:
        file.write(markdown_content)

# Close the connection to the database
conn.close()