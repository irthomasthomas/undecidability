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
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash
# A bash script to create a hash function for activity_id and activity_name.

# Function to get the activity name given an activity id.
get_activity_name() {
    local activity_id="$1"
    local activity_name=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$activity_id")
    echo "$activity_name"
}

# Function to get the current activity id and name.
get_current_activity() {
    local active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
    local active_activity_name=$(get_activity_name "$active_activity_id")
    echo "$active_activity_id : $active_activity_name"
}

# A hash function for activity_id and activity_name.
make_activity_hash() {
    declare -A activity_hash
    local active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
    local active_activity_name=$(get_activity_name "$active_activity_id")

    activity_hash["$active_activity_id"]="$active_activity_name"
    for id in "${!activity_hash[@]}" 
    do 
        echo "id:   $id"
        echo "name: ${activity_hash[$id]}"
    done
}

# Call the function
make_activity_hash
```

<details><summary>Metadata</summary>

- Duration: 22210 ms
- Datetime: 2023-07-19T17:13:26.945681
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

