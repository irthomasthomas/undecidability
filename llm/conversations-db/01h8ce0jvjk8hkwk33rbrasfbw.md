**Prompt:**
Think about this quietly. Generate a descriptive and simple filename, in the form of file-name.ext (e.g. ink-check.py) for this script: \n\n #!/bin/zsh

# Ask the user if they want to record history
read -p "Do you want to record the session history? [y/n]: " answer

if [[ $answer == "y" || $answer == "Y" ]]; then
    # Get the current date and time
    timestamp=$(date +"%Y%m%d%H%M%S")

    # Set the activity variable
    activity="your_activity_name"

    # Define the output file name with activity
    output_file="${activity}_session_${timestamp}.log"

    # Start recording the session using the script command
    script -a -f -q "$output_file"

    # Create the symlink to the log file in the Activities directory
    ln -s "$output_file" "$HOME/Activities/$output_file"
else
    echo "Session history will not be recorded."
fi.

**Response:**
session-recorder.sh

<details><summary>Metadata</summary>

- Duration: 485 ms
- Datetime: 2023-08-21T16:14:26.700516
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

