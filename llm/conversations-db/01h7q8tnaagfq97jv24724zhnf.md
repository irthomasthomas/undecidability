**Prompt:**
What is the exact zsh or bash command to: create a new github issue?

**Response:**
There is no built-in command in zsh or bash to create a new GitHub issue. However, you can use the GitHub API to achieve this. Here is an example of a curl command that creates a new GitHub issue:

```shell
curl --request POST \
  --url 'https://api.github.com/repos/{owner}/{repo}/issues' \
  --header 'Authorization: Bearer {access_token}' \
  --header 'Content-Type: application/json' \
  --data '{
    "title": "New Issue",
    "body": "This is a new issue"
  }'
```

Replace `{owner}` with the owner of the repository, `{repo}` with the repository name, and `{access_token}` with a valid GitHub access token that has the necessary permissions to create issues in the repository.

<details><summary>Metadata</summary>

- Duration: 5358 ms
- Datetime: 2023-08-13T10:59:41.786835
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

