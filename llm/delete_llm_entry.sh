#!/bin/bash

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

  if [ "$2" == "-y" ]; then
    confirm="y"
  else
    read -p "Are you sure you want to delete these records? (y/n): " confirm
  fi

  if [ "$confirm" != "y" ]; then
    echo "Deletion cancelled for conversation ID $conversation_id."
    return
  fi

  sqlite3 $(llm logs path) "DELETE FROM responses WHERE conversation_id = '$conversation_id'"
  sqlite3 $(llm logs path) "DELETE FROM conversations WHERE id = '$conversation_id'"

  echo "Log entry with ID $conversation_id and all associated entries have been deleted successfully."
  echo ""
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
