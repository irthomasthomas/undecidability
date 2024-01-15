**Prompt:**
Here is a new table schema for the evals function. Write the corresponding bash function so I can add my eval from the console
#!/bin/bash

# Get the path to the llm logs
DB_PATH=$(llm logs path)

# Create a backup of the db
cp $DB_PATH ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)

# Apply the sql schema changes
# Store the sql command in a variable
SQL_COMMAND="CREATE TABLE [evaluations] (
[id] INTEGER PRIMARY KEY,
[response_id] TEXT REFERENCES [responses]([id]),
[evaluation_grade] INTEGER,
[evaluation_comment] TEXT,
[evaluation_date] TEXT
);"

# Run the sql command
echo $SQL_COMMAND | sqlite3 $DB_PATH

# Print a success message
echo "Database schema updated successfully. A backup of the original database was created at path: ${DB_PATH}_bak_$(date +%Y%m%d%H%M%S)"

**Response:**
Here is a bash function to add your eval from the console. You can use the SQLite INSERT INTO statement to add a new record to the evaluations table in your SQLite database:

```bash
function add_eval() {
  # Get the path to the llm logs
  DB_PATH=$(llm logs path)
  
  # Store the insert statement in a variable
  SQL_COMMAND="INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment, evaluation_date) 
               VALUES ('$1', '$2', '$3', '$4');"
  
  # Run the sql command
  echo $SQL_COMMAND | sqlite3 $DB_PATH
  
  # Print a success message
  echo "Evaluation added successfully to the database."
}
```

You can run it in the console as follows (replace placeholders with actual values):

```',
add_eval 'response_id_value' 'evaluation_grade_value' 'evaluation_comment_value' 'evaluation_date_value'
```

<details><summary>Metadata</summary>

- Duration: 19962 ms
- Datetime: 2023-10-19T14:22:36.236475
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

