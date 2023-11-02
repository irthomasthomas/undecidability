#!/bin/bash

# Function to display issues
display_issues() {
  echo "Displaying issues labeled as overseer-inbox:"
  gh issue list -L 30 --label overseer-inbox
}

# Function to add new issues
add_issue() {
  echo "Enter the description for new issue:"
  read issue_desc
  gh issue create --title "$issue_desc" --label inbox-url
}

# Function to reply to queries
reply_query() {
  echo "Please choose one of the issue to reply:"
  reply_issue=$(gh issue list -L 5 --state all | fzf -1 -0 | awk '{print $1}')
  echo "Enter your reply:"
  read reply
  gh issue comment "$reply_issue" -b "$reply"
}

# Main menu
while true
do
  echo "1. Display issues"
  echo "2. Add new issue"
  echo "3. Reply to query"
  echo "4. Exit"
  read -p "Enter your choice: " choice

  case $choice in
    1)
      display_issues
      ;;
    2)
      add_issue
      ;;
    3)
      reply_query
      ;;
    4)
      break
      ;;
    *)
      echo "Invalid choice, please try again."
      ;;
  esac
done
