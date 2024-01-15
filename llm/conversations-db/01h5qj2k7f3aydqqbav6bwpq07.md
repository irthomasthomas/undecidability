**Prompt:**
Think carefully. Write a complete, fully functional bash script to Make a hash function for activity_id and activity_name. Use the following functions for inspiration. 
get_current_activity() {
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  active_activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
  echo $active_activity_id
}

get_current_activity_name() {
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  active_activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
  echo $active_activity_name
}

get_activity_name() {
  activity_id="$1"
  activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$activity_id")
  echo $activity_name
} ?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block.
SAY NOTHING ELSE!


**Response:**
#!/bin/bash

# Hash function to map activity_id to activity_name
declare -A ActivityHash

# Function to get activity_name using activity_id from DBus interface
get_activity_name() {
  activity_id="$1"
  activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$activity_id")
  echo $activity_name
}

# Function to add activity_id and activity_name to Hash
add_activity_to_hash() {
  activity_id="$1"
  activity_name="$2"
  
  # Only add if not already exists in the hash
  if [[ -z "${ActivityHash[$activity_id]+exists}" ]]; then
    ActivityHash["$activity_id"]=$activity_name
  fi
}

# Main function to run the whole process
main() {
  # Fetch Current Activity ID
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)

  # Fetch Activity Name for the Active Activity ID
  active_activity_name=$(get_activity_name $active_activity_id)

  # Add Active activity_id and activity_name to Hash
  add_activity_to_hash "$active_activity_id" "$active_activity_name"

  # Print the entire hash map
  for key in "${!ActivityHash[@]}"; do
    echo "Activity ID: $key , Activity Name: ${ActivityHash[$key]}"
  done
}

# Call the main function
main


<details><summary>Metadata</summary>

- Duration: 21219 ms
- Datetime: 2023-07-19T17:09:39.466900
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

