**Prompt:**
diff --git a/llm/delete_llm_entry.sh b/llm/delete_llm_entry.sh
new file mode 100644
index 0000000..3297b29
--- /dev/null
+++ b/llm/delete_llm_entry.sh
@@ -0,0 +1,57 @@
+#!/bin/bash
+
+delete_by_id() {
+  conversation_id="$1"
+  responses_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM responses WHERE conversation_id = '$conversation_id'")
+  if [ "$responses_count" -eq 0 ]; then
+    echo "Log entry with ID $conversation_id does not exist."
+    return
+  fi
+
+  conversations_count=$(sqlite3 $(llm logs path) "SELECT COUNT(*) FROM conversations WHERE id = '$conversation_id'")
+
+  echo "The following records will be deleted for conversation ID $conversation_id:"
+  echo "Responses: $responses_count"
+  echo "Conversations: $conversations_count"
+
+  if [ "$2" == "-y" ]; then
+    confirm="y"
+  else
+    read -p "Are you sure you want to delete these records? (y/n): " confirm
+  fi
+
+  if [ "$confirm" != "y" ]; then
+    echo "Deletion cancelled for conversation ID $conversation_id."
+    return
+  fi
+
+  sqlite3 $(llm logs path) "DELETE FROM responses WHERE conversation_id = '$conversation_id'"
+  sqlite3 $(llm logs path) "DELETE FROM conversations WHERE id = '$conversation_id'"
+
+  echo "Log entry with ID $conversation_id and all associated entries have been deleted successfully."
+  echo ""
+}
+
+# Function for bulk search and delete
+bulk_search_delete() {
+  search_query="$1"
+  conversation_ids=$(llm logs list -q "$search_query" -n 0 --json | jq -r '.[].conversation_id')
+
+  if [ -z "$conversation_ids" ]; then
+    echo "No log entries found matching the search query."
+    return
+  fi
+
+  for conversation_id in $conversation_ids; do
+    delete_by_id "$conversation_id"
+  done
+}
+
+# Check if delete_by_id or bulk_search_delete should be executed based on arguments
+if [ "$1" == "delete_by_id" ]; then
+  delete_by_id "$2"
+elif [ "$1" == "bulk_search_delete" ]; then
+  bulk_search_delete "$2"
+else
+  echo "Invalid command. Supported commands are 'delete_by_id' and 'bulk_search_delete'."
+fi
diff --git a/llm/evals_table_maker.sh b/llm/evals_table_maker.sh
new file mode 100644
index 0000000..3591a3d
--- /dev/null
+++ b/llm/evals_table_maker.sh
@@ -0,0 +1,23 @@
+#!/bin/bash
+
+# Get the path to the llm logs
+DB_PATH=$(llm logs path)
+
+# Create a backup of the db
+cp $DB_PATH ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)
+
+# Apply the sql schema changes
+# Store the sql command in a variable
+SQL_COMMAND="CREATE TABLE [evaluations] (
+[id] INTEGER PRIMARY KEY,
+[response_id] TEXT REFERENCES [responses]([id]),
+[evaluation_grade] INTEGER,
+[evaluation_comment] TEXT,
+[evaluation_date] TEXT
+);"
+
+# Run the sql command
+echo $SQL_COMMAND | sqlite3 $DB_PATH
+
+# Print a success message
+echo "Database schema updated successfully. A backup of the original database was created at path: ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)"
diff --git a/llm/llm_evaluations.sh b/llm/llm_evaluations.sh
new file mode 100644
index 0000000..ab5320f
--- /dev/null
+++ b/llm/llm_evaluations.sh
@@ -0,0 +1,53 @@
+#!/bin/bash
+
+add_eval() {
+  # Check for correct number of arguments
+  if [ $# -ne 2 ]; then
+    echo "Error: Invalid number of arguments. Expecting 4, but got $#."
+    echo "Usage: add_eval '<response_id>' '<evaluation_grade>' '<evaluation_comment>' '<evaluation_date>'"
+    return 1
+  fi
+
+  local evaluation_grade="$1"
+  local evaluation_comment="$2"
+
+  evaluation_date="$(llm logs list -n 1 --json | jq -r '.[] | .datetime_utc')"
+  echo "evaluation_date $evaluation_date"
+  # Getting the database path
+  local db_path=$(llm logs path)
+  echo "db_path: $db_path"
+  # validate if 'llm logs path' exists and can give database path.
+  if [ -z "$db_path" ]; then
+    echo "Error: Could not retrieve database path. Please check 'llm logs path' command."
+    return 1
+  fi
+
+  # Get the response_id from 'llm logs list' command.
+  local response_id=$(llm logs list -n 1 --json | jq -r '.[] | .id')
+  echo "response_id $response_id"
+  if [ -z "$response_id" ]; then
+    echo "Error: Could not retrieve conversation id. Please check 'llm logs list -n 1 --json' command."
+    return 1
+  fi
+
+  # SQL Command
+  local sql_command="INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment, evaluation_date)
+                     VALUES ('$response_id', '$evaluation_grade', '$evaluation_comment', '$evaluation_date');
+                     SELECT changes();"
+  echo "sql_command: $sql_command"
+
+  # Executing SQL command and capturing result
+  local result=$(echo $sql_command | sqlite3 $db_path)
+  echo "result: $result"
+
+  # Checking if command execution is successful
+  if [ "$result" -eq "0" ]; then
+    echo 'Error: Failed to add evaluation.'
+    return 1
+  else
+    echo 'Success: Evaluation added in the database.'
+  fi
+}
+
+
+add_eval "$1" "$2"


**Response:**
Add script for adding evaluations to the database

<details><summary>Metadata</summary>

- Duration: 1581 ms
- Datetime: 2023-11-02T14:24:15.931102
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

