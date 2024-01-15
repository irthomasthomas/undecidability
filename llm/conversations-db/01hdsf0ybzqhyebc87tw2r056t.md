**Prompt:**
Write a script that reads a github issue and parses the text for a markdown task list, then populate a list of tasks to do with unchecked tasks. Also a write a function that can update the issue to mark a task complete.


Think carefully. Start with a brief algorithm.

**Response:**
Algorithm:

1. Read the GitHub issue text.
2. Parse the text to find any markdown task lists.
3. For each task list found, iterate through the tasks.
4. If a task is unchecked, add it to the list of tasks to do.
5. Display the list of tasks to do.
6. Provide an option to mark a task as complete.
7. If a task is marked as complete, update the GitHub issue text to reflect the change.

Script:

```python
import requests

# Function to read the GitHub issue text
def read_github_issue(issue_url):
    response = requests.get(issue_url)
    issue_text = response.json()['body']
    return issue_text

# Function to parse the text for markdown task lists
def parse_task_lists(issue_text):
    tasks = []
    lines = issue_text.split('\n')
    for line in lines:
        if '- [ ]' in line:
            task = line.replace('- [ ]', '').strip()
            tasks.append(task)
    return tasks

# Function to display the list of tasks to do
def display_tasks_to_do(tasks):
    print("Tasks to do:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Function to mark a task as complete and update the GitHub issue
def mark_task_complete(issue_url, task_index):
    response = requests.get(issue_url)
    issue_text = response.json()['body']
    lines = issue_text.split('\n')
    updated_lines = []
    for i, line in enumerate(lines):
        if '- [ ]' in line:
            if i + 1 == task_index:
                updated_lines.append(line.replace('- [ ]', '- [x]'))
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    updated_issue_text = '\n'.join(updated_lines)
    response = requests.patch(issue_url, json={'body': updated_issue_text})
    if response.status_code == 200:
        print("Task marked as complete successfully.")
    else:
        print("Failed to mark task as complete.")

# Main script
if __name__ == "__main__":
    issue_url = "https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    issue_text = read_github_issue(issue_url)
    tasks = parse_task_lists(issue_text)
    display_tasks_to_do(tasks)

    task_index = int(input("Enter the task number to mark as complete (0 to exit): "))
    while task_index != 0:
        mark_task_complete(issue_url, task_index)
        task_index = int(input("Enter the task number to mark as complete (0 to exit): "))
```

Note: Replace `{owner}`, `{repo}`, and `{issue_number}` in the `issue_url` with the appropriate values for the GitHub repository and issue you want to work with.

<details><summary>Metadata</summary>

- Duration: 55511 ms
- Datetime: 2023-10-27T20:59:48.775455
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

**Prompt:**
Write the same program in bash. Fixing any bugs along the way.

**Response:**
Writing this in bash is a bit more complex due to the lack of built-in JSON parsing and HTTP request libraries. However, we can use `curl` for HTTP requests and `jq` for JSON parsing. Here's a bash script that accomplishes the same task:

```bash
#!/bin/bash

# Function to read the GitHub issue text
read_github_issue() {
    issue_url=$1
    issue_text=$(curl -s $issue_url | jq -r '.body')
    echo "$issue_text"
}

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

# Main script
issue_url="https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
issue_text=$(read_github_issue $issue_url)
tasks=$(parse_task_lists "$issue_text")
display_tasks_to_do "$tasks"

echo "Enter the task number to mark as complete (0 to exit): "
read task_index
while [ $task_index -ne 0 ]
do
    mark_task_complete $issue_url $task_index
    echo "Enter the task number to mark as complete (0 to exit): "
    read task_index
done
```

Note: Replace `{owner}`, `{repo}`, and `{issue_number}` in the `issue_url` with the appropriate values for the GitHub repository and issue you want to work with. Also, you need to set up authentication for the `curl` command to be able to update the issue.

<details><summary>Metadata</summary>

- Duration: 34977 ms
- Datetime: 2023-10-27T21:01:31.383609
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

