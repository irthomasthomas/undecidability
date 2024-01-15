**Prompt:**
Update that to call LogFailedInstruction to log the failure with the input prompt, the note string, the output, and the failure type.

**Response:**
```bash
# Function to sanitize the classification result and log errors
SanitizeResult() {
    [[ -z "$1" || -z "$2" ]] && { echo "You did not provide any input"; return 1; } # Check input
    classification=$(grep -Eo 'true|false' <<< "$1")
    if [[ $(grep -E 'true|false' <<< "$1" | wc -l) -ne 1 ]]; then
        LogFailedInstruction "$2" "$1" "Invalid classification result"
        return 1
    fi
    echo "$classification"
}

# Function to log failures
LogFailedInstruction() {
    note="$1"
    output="$2"
    failureType="$3"
    echo -e "Prompt: $note\nOutput: $output\nError: $failureType" >> fail_log.txt
}
```

<details><summary>Metadata</summary>

- Duration: 16923 ms
- Datetime: 2023-08-23T16:39:12.379213
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
Output the completed script.

**Response:**
```bash
#!/bin/bash

# Function to create a diff file and delete the original
MakeDiff() {
    [[ -z "$1" || -z "$2" ]] && { echo "You did not provide any input"; return 1; } # Check input
    diff -u "$1" "$2" > "$1".diff && rm "$1" # Create diff file and delete original file
}

# Function to apply changes and revert to an old version
RebuildFromDiff() {
    [[ -z "$1" || -z "$2" ]] && { echo "You did not provide any input"; return 1; } # Check input
    patch "$1" "$2" # Apply changes 
}

# Function to detect notes
DetectNotes() {
    [[ -z "$1" ]] && { echo "You did not provide any input"; return 1; } # Check input
    grep -r '^#.*Note:' "$1" > queue.txt # Find notes and push them to queue.txt
}

# Function to classify notes
NoteClassifier-GPT3() {
    while IFS= read -r line
    do
        NoteString=$(echo "$line" | awk -F':' '{print $2}') # Get the note text
        isActionable=$(LLM -template "ClassifyNoteActions $NoteString") # Classify the note
        echo "$line is actionable: $isActionable" >> classified_notes.txt # Write result to a file
    done < queue.txt
}

# Required prompt for classifying notes using GPT3
ClassifyNoteActions() {
    NoteString="$1"
    # Define the prompt 
    Prompt="I have a note from an engineer. Here it is: '${NoteString}'. Is this note actionable? An actionable note will contain something that needs to be researched, like a problem, or new feature idea. Or some code or function than needs to be fixed, refactored or expanded. If the Note text is a typical code note, reminder, or explanation then it is not actionable. Please classify as 'true' for actionable or 'false' for non-actionable."
    # Use your CLI tool to send the request body to GPT3 API for classification
    Response=$(cli-tool-to-gpt3-api "$Prompt")
    echo "$Response"
}

# Function to sanitize the classification result and log errors
SanitizeResult() {
    [[ -z "$1" || -z "$2" ]] && { echo "You did not provide any input"; return 1; } # Check input
    classification=$(grep -Eo 'true|false' <<< "$1")
    if [[ $(grep -E 'true|false' <<< "$1" | wc -l) -ne 1 ]]; then
        LogFailedInstruction "$2" "$1" "Invalid classification result"
        return 1
    fi
    echo "$classification"
}

# Function to log failures
LogFailedInstruction() {
    note="$1"
    output="$2"
    failureType="$3"
    echo -e "Prompt: $note\nOutput: $output\nError: $failureType" >> fail_log.txt
}

# Usage Examples
# MakeDiff original.txt new.txt
# RebuildFromDiff current.txt diff.txt
# DetectNotes directory/
# NoteClassifier-GPT3
# SanitizeResult result "$NoteString"
# LogFailedInstruction "$NoteString" "$Response" "Invalid classification result"

```

<details><summary>Metadata</summary>

- Duration: 37593 ms
- Datetime: 2023-08-23T16:45:35.389477
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{}
```

