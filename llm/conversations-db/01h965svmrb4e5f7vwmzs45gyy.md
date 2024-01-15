**Prompt:**
Heredoc to markdown to gh issue

**Response:**
To convert a heredoc text into Markdown and then use it in a GitHub issue, you can follow these steps:

Step 1: Convert Heredoc to Markdown
If you have the heredoc text as a variable in a programming language, you can convert it to Markdown. Assuming you have the heredoc stored in a variable called `heredoc_text`, you can use a Markdown library or module to convert it to Markdown format. For example, in Python, you can use the `markdown` library:

```python
import markdown

markdown_text = markdown.markdown(heredoc_text)
```

Step 2: Create a GitHub Issue
To create a GitHub issue with the converted Markdown text, you can use GitHub's REST API or a library/module specific to your programming language. Assuming you are using Python, you can use the `requests` library to create the issue:

```python
import requests

# Specify the necessary details for creating the issue
repo_owner = "your_username"
repo_name = "your_repo"
access_token = "your_access_token"
issue_title = "Your Issue Title"
issue_body = markdown_text

# Create the issue using GitHub's REST API
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
headers = {"Authorization": f"token {access_token}"}
data = {
    "title": issue_title,
    "body": issue_body
}
response = requests.post(url, headers=headers, json=data)

# Check if the issue was created successfully
if response.status_code == 201:
    print("Issue created successfully!")
else:
    print(f"Failed to create issue. Response status code: {response.status_code}")
```

Make sure to replace `"your_username"`, `"your_repo"`, `"your_access_token"`, `"Your Issue Title"`, and other necessary values with your own information.

Running this code will convert the heredoc text to Markdown and create a new GitHub issue with the converted text as the issue body.

<details><summary>Metadata</summary>

- Duration: 12637 ms
- Datetime: 2023-08-31T16:11:00.794365
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

