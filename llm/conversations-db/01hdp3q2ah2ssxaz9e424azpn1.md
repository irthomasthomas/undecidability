**Prompt:**
Using this command as inspiration, add a bulk search and delete function to the script. llm logs list -q "search query" -n 0  --json | jq -r '.[] | [.conversation_id, .conversation_name] | @tsv'



#!/bin/bash

# Step 1: Read the log entry id from user input
conversation_id="$1"
responses_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM responses WHERE conversation_id = '$conversation_id'")
if [ "$responses_count" -eq 0 ]; then
  echo "Log entry with id $conversation_id does not exist."
  exit 1
fi

conversations_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM conversations WHERE id = '$conversation_id'" )

# Step 5: Show the count of records that will be deleted for each table
echo "The following records will be deleted:"
echo "Evaluations: $evaluations_count"
echo "Responses: $responses_count"
echo "conversations_table Records: $conversations_count"

# Step 6: Ask the user to confirm before proceeding with deletion
read -p "Are you sure you want to delete these records? (y/n): " confirm

if [ "$confirm" != "y" ]; then
  echo "Deletion cancelled."
  exit 1
fi

sqlite3 $(llm logs path) "DELETE FROM responses WHERE conversation_id = '$conversation_id'"
sqlite3 $(llm logs path) "DELETE FROM conversations WHERE id = '$conversation_id'"

echo "Log entry with id $conversation_id and all associated entries have been deleted successfully."

**Response:**
To add a bulk search and delete function to the script, you can modify it as follows:

```bash
#!/bin/bash

# Step 1: Read the search query from user input
search_query="$1"

# Step 2: Perform the search and retrieve the conversation IDs
conversation_ids=$(llm logs list -q "$search_query" -n 0 --json | jq -r '.[].conversation_id')

# Step 3: Check if any conversations match the search query
if [ -z "$conversation_ids" ]; then
  echo "No log entries found matching the search query."
  exit 1
fi

# Step 4: Iterate over the conversation IDs and delete the associated entries
for conversation_id in $conversation_ids; do
  responses_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM responses WHERE conversation_id = '$conversation_id'")
  conversations_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM conversations WHERE id = '$conversation_id'")

  # Step 5: Show the count of records that will be deleted for each table
  echo "The following records will be deleted for conversation ID $conversation_id:"
  echo "Responses: $responses_count"
  echo "Conversations: $conversations_count"

  # Step 6: Ask the user to confirm before proceeding with deletion
  read -p "Are you sure you want to delete these records? (y/n): " confirm

  if [ "$confirm" != "y" ]; then
    echo "Deletion cancelled for conversation ID $conversation_id."
    continue
  fi

  # Step 7: Delete the records for the conversation ID
  sqlite3 $(llm logs path) "DELETE FROM responses WHERE conversation_id = '$conversation_id'"
  sqlite3 $(llm logs path) "DELETE FROM conversations WHERE id = '$conversation_id'"

  echo "Log entry with ID $conversation_id and all associated entries have been deleted successfully."
done
```

With this modified script, you can now provide a search query as an argument, and it will search for log entries matching the query. For each matching log entry, it will display the count of associated records that will be deleted and ask for confirmation before proceeding with deletion.

<details><summary>Metadata</summary>

- Duration: 37269 ms
- Datetime: 2023-10-26T13:44:45.755861
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

**Prompt:**
Make it an optional function alongside the delete_by_id functionality

**Response:**
To make the bulk search and delete function optional alongside the delete_by_id functionality, you can modify the script as follows:

```bash
#!/bin/bash

# Function for deleting log entries by ID
delete_by_id() {
  conversation_id="$1"
  responses_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM responses WHERE conversation_id = '$conversation_id'")
  if [ "$responses_count" -eq 0 ]; then
    echo "Log entry with ID $conversation_id does not exist."
    return
  fi

  conversations_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM conversations WHERE id = '$conversation_id'")

  echo "The following records will be deleted for conversation ID $conversation_id:"
  echo "Responses: $responses_count"
  echo "Conversations: $conversations_count"

  read -p "Are you sure you want to delete these records? (y/n): " confirm

  if [ "$confirm" != "y" ]; then
    echo "Deletion cancelled for conversation ID $conversation_id."
    return
  fi

  sqlite3 $(llm logs path) "DELETE FROM responses WHERE conversation_id = '$conversation_id'"
  sqlite3 $(llm logs path) "DELETE FROM conversations WHERE id = '$conversation_id'"

  echo "Log entry with ID $conversation_id and all associated entries have been deleted successfully."
}

# Function for bulk search and delete
bulk_search_delete() {
  search_query="$1"
  conversation_ids=$(llm logs list -q "$search_query" -n 0 --json | jq -r '.[].conversation_id')

  if [ -z "$conversation_ids" ]; then
    echo "No log entries found matching the search query."
    return
  fi

  for conversation_id in $conversation_ids; do
    delete_by_id "$conversation_id"
  done
}

# Check if delete_by_id or bulk_search_delete should be executed based on arguments
if [ "$1" == "delete_by_id" ]; then
  delete_by_id "$2"
elif [ "$1" == "bulk_search_delete" ]; then
  bulk_search_delete "$2"
else
  echo "Invalid command. Supported commands are 'delete_by_id' and 'bulk_search_delete'."
fi
```

Now, you can run the script with the following commands:

```bash
# Delete log entry by ID
./script.sh delete_by_id <conversation_id>

# Bulk search and delete by query
./script.sh bulk_search_delete <search_query>
```

The script checks the first argument provided. If it is `delete_by_id`, the script will call the `delete_by_id` function and pass the conversation ID as the second argument. If it is `bulk_search_delete`, the script will call the `bulk_search_delete` function and pass the search query as the second argument. If the first argument does not match any supported commands, an error message will be displayed.

<details><summary>Metadata</summary>

- Duration: 45554 ms
- Datetime: 2023-10-26T13:46:21.152634
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

