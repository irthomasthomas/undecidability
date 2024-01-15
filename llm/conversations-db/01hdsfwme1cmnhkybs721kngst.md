**Prompt:**
Is there a more elegant way to write the mark_task_complete function?



# Function to parse the text for markdown task lists
parse_task_lists() {
    issue_text=$1
    tasks=$(echo "$issue_text" | grep '- \[ \]' | sed 's/- \[ \] //')
    echo "$tasks"
}

# Function to display the list of tasks to do
display_tasks_to_do() {
    tasks=$1
    echo "Tasks to do:"
    echo "$tasks"
}

# Function to mark a task as complete and update the GitHub issue
mark_task_complete() {
    issue_url=$1
    task_index=$2
    issue_text=$(read_github_issue $issue_url)
    updated_issue_text=$(echo "$issue_text" | awk -v idx=$task_index 'BEGIN{FS="\n"; RS=""} {gsub("- \[ \]", "- \[x\]", $idx); print}')
    curl -X PATCH -d "{\"body\":\"$updated_issue_text\"}" $issue_url
}

**Response:**
Yes, there is a more elegant way to write the `mark_task_complete` function. Here is a refactored version of the function:

```bash
# Function to mark a task as complete and update the GitHub issue
mark_task_complete() {
    issue_url=$1
    task_index=$2
    issue_text=$(read_github_issue $issue_url)
    tasks=$(parse_task_lists "$issue_text")
    tasks_array=($tasks)
    tasks_array[$task_index]="- [x] ${tasks_array[$task_index]}"
    updated_issue_text="${issue_text//- [ ] ${tasks[$task_index]}/${tasks_array[$task_index]}}"
    curl -X PATCH -d "{\"body\":\"$updated_issue_text\"}" $issue_url
}
```

In this refactored version, the `mark_task_complete` function uses the `parse_task_lists` function to get the list of tasks from the issue text. It then converts the tasks into an array and marks the task at the specified index as complete. Finally, it replaces the original task in the issue text with the marked task and updates the GitHub issue.

This version is more elegant because it reuses the `parse_task_lists` function to parse the tasks and uses array manipulation to mark a task as complete, which is more straightforward and easier to understand than the original version.

<details><summary>Metadata</summary>

- Duration: 20379 ms
- Datetime: 2023-10-27T21:15:31.237790
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

