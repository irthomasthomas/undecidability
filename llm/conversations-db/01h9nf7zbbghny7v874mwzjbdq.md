**Prompt:**
What is the best terminal command, small function, or script to run in order to: Monitor github repo for new issue comments using gh cli?


**Response:**
You can use the GitHub CLI tool `gh` to monitor a GitHub repository for new issue comments. However, `gh` does not have a built-in feature to monitor in real-time. You would need to periodically run the command to fetch the latest comments.

Here is a simple bash script that you can use:

```bash
#!/bin/bash

REPO=<Your-Repo-Name>
OWNER=<Your-Github-Username>

while true; do
    gh issue list -R $OWNER/$REPO --comments
    sleep 60
done
```

Replace `<Your-Repo-Name>` and `<Your-Github-Username>` with your repository name and GitHub username respectively. This script will fetch the list of issues with their comments every 60 seconds.

Please note that this will only fetch the number of comments, not the actual comments themselves. The GitHub CLI currently does not support fetching comments directly. You might need to use the GitHub API for more detailed information.

<details><summary>Metadata</summary>

- Duration: 28152 ms
- Datetime: 2023-09-06T14:44:21.490946
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

