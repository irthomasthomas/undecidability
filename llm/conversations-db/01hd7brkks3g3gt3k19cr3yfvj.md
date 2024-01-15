**Prompt:**
Rewrite this in bash. Do a professional job, please. Read parameters: title, url, selection from one or more named pipes. In the nyxt lisp send those values to the named pipe(s). Think carefully about the design and the algorithm. The plan is to send the title/url/selection to a new github issue for it to be picked up by github actions for further processing.

**Response:**
Here's a bash script that reads parameters from named pipes and sends them to a new GitHub issue:

```bash
#!/bin/bash

# Named pipes
TITLE_PIPE="/tmp/title_pipe"
URL_PIPE="/tmp/url_pipe"
SELECTION_PIPE="/tmp/selection_pipe"

# Check if pipes exist, if not create them
[ ! -p $TITLE_PIPE ] && mkfifo $TITLE_PIPE
[ ! -p $URL_PIPE ] && mkfifo $URL_PIPE
[ ! -p $SELECTION_PIPE ] && mkfifo $SELECTION_PIPE

# Read from pipes
read -r title < $TITLE_PIPE
read -r url < $URL_PIPE
read -r selection < $SELECTION_PIPE

# Prepare data for GitHub issue
issue_data='{
  "title": "'"$title"'",
  "body": "URL: '"$url"'\nSelection: '"$selection"'"
}'

# GitHub API URL
github_api_url="https://api.github.com/repos/<owner>/<repo>/issues?access_token=<token>"

# Send data to GitHub API
curl -X POST -H "Content-Type: application/json" -d "$issue_data" $github_api_url

# Close pipes
exec 3>&-
```

Please replace `<owner>`, `<repo>`, and `<token>` with your GitHub username, repository name, and personal access token respectively.

This script creates named pipes if they don't exist, then reads from them. It then prepares a JSON object to send to the GitHub API to create a new issue. The issue's title is the title read from the pipe, and the body contains the URL and selection. The script then sends a POST request to the GitHub API to create the issue.

Please note that you need to have curl installed to send the POST request. Also, this script doesn't handle errors, such as failing to create a pipe or failing to send the POST request. You might want to add error handling depending on your needs.

<details><summary>Metadata</summary>

- Duration: 31315 ms
- Datetime: 2023-10-20T20:16:54.309348
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

