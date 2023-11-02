#!/bin/bash

add_eval() {
  # Check for correct number of arguments
  if [ $# -ne 2 ]; then
    echo "Error: Invalid number of arguments. Expecting 4, but got $#."
    echo "Usage: add_eval '<response_id>' '<evaluation_grade>' '<evaluation_comment>' '<evaluation_date>'"
    return 1
  fi

  local evaluation_grade="$1"
  local evaluation_comment="$2"

  evaluation_date="$(llm logs list -n 1 --json | jq -r '.[] | .datetime_utc')"
  echo "evaluation_date $evaluation_date"
  # Getting the database path
  local db_path=$(llm logs path)
  echo "db_path: $db_path"
  # validate if 'llm logs path' exists and can give database path.
  if [ -z "$db_path" ]; then
    echo "Error: Could not retrieve database path. Please check 'llm logs path' command."
    return 1
  fi

  # Get the response_id from 'llm logs list' command.
  local response_id=$(llm logs list -n 1 --json | jq -r '.[] | .id')
  echo "response_id $response_id"
  if [ -z "$response_id" ]; then
    echo "Error: Could not retrieve conversation id. Please check 'llm logs list -n 1 --json' command."
    return 1
  fi

  # SQL Command
  local sql_command="INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment, evaluation_date)
                     VALUES ('$response_id', '$evaluation_grade', '$evaluation_comment', '$evaluation_date');
                     SELECT changes();"
  echo "sql_command: $sql_command"

  # Executing SQL command and capturing result
  local result=$(echo $sql_command | sqlite3 $db_path)
  echo "result: $result"

  # Checking if command execution is successful
  if [ "$result" -eq "0" ]; then
    echo 'Error: Failed to add evaluation.'
    return 1
  else
    echo 'Success: Evaluation added in the database.'
  fi
}


add_eval "$1" "$2"
