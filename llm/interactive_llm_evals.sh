#!/bin/bash

DB_PATH="$HOME/logs.db"

# Function to execute a SQL query and return results
query_db() {
  sqlite3 "$DB_PATH" "$1"
}

# Function to interactively search prompts or responses using fzf
  search_entries() {
    echo "search_entries"
    local search_column="$1"
    echo "search_column: $search_column"
    local search_term=${2:-$(read -p "Enter search term: " search_term)}
    echo "search_term: $search_term"
  
    # Add '%' wildcard for partial matching 
    IFS=$'|'
    query_db "SELECT id, model, prompt, response FROM responses WHERE $search_column LIKE '%${search_term}%' ORDER BY datetime_utc DESC;" | while read -r id model prompt response
    do
      short_prompt=${prompt:0:40}
      short_response=${response:0:40}
      echo "$id|$short_prompt|$short_response" | fzf --delimiter='|' --with-nth=1,2
    done
  }

# Function to copy to clipboard
copy_to_clipboard() {
  local response="$1"
  echo "$response" | xclip -selection clipboard
  echo "Response copied to clipboard."
}

# Function to open in a new terminal
open_in_terminal() {
  local response="$1"
  local tempfile=$(mktemp)
  echo "$response" > "$tempfile"
  x-terminal-emulator -e bash -c "cat $tempfile; exec bash"
  echo "Response opened in new terminal."
}

# Function to score a response
score_response() {
  local response_id="$1"
  echo "Scoring for response ID: $response_id"
  local score=$(printf "-2\n-1\n0\n1\n2" | fzf --header="Choose a score (-2 to +2):")
#  local comment=$(printf "Good\nAverage\nPoor" | fzf --header="Choose a comment:")
   local comment=""

  # Insert the score and comment into the database
  query_db "INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment) VALUES ('$response_id', '$score', '$comment');"
  echo "Response scored successfully."
}

# Function to evaluate a response
evaluate_response() {
  echo "evaluate_response"
  local chosen_entry=$(search_entries "prompt")
  echo "chosen_entry: $chosen_entry"
  local response_id=$(echo $chosen_entry | cut -d '|' -f 1)
  echo "response_id: $response_id"
  # Display options for what to do next with the response
  local action=$(printf "Copy to Clipboard\nOpen in Terminal\nScore Response" | fzf --header="Choose action:")
  case $action in
    "Copy to Clipboard")
      local response=$(echo $chosen_entry | cut -d '|' -f 4)
      copy_to_clipboard "$response"
      ;;
    "Open in Terminal")
      local response=$(echo $chosen_entry | cut -d '|' -f 4)
      open_in_terminal "$response"
      ;;
    "Score Response")
      score_response "$response_id"
      ;;
    *)
      echo "No valid action selected."
      ;;
  esac
}

# Text-based main menu function
main_menu() {
  while true; do
    echo "Menu Options:"
    echo "1) Search prompts"
    echo "2) Search responses"
    echo "3) Evaluate response"
    echo "4) Exit"
    echo "Please choose an option: "
    read -r action

    case "$action" in
      1)
        search_entries "prompt"
        ;;
      2)
        search_entries "response"
        ;;
      3)
        evaluate_response
        ;;
      4)
        echo "Exiting..."
        break
        ;;
      *)
        echo "Invalid option, please try again."
        ;;
    esac
  done
}

# Run the main menu
main_menu
