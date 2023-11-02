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
