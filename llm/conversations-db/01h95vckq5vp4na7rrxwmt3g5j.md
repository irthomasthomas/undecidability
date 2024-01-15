**Prompt:**
propose an github issues label scheme for the following workflow: When a new issue is detected, it will be one of title:url where the issue title is the subject of the url target, and the body contains only a url. In that case, github actions should run a get_new_url and add a reply with the output. Then remove the label.

**Response:**
I would propose the following GitHub issues label scheme for the mentioned workflow:

1. **NewIssue**: This label would be added automatically when a new issue is detected. It indicates that the issue follows the required format of having the issue title as the subject of the URL target, and the body containing only a URL. 

2. **ActionRequired**: This label would be added by a GitHub action called "get_new_url". It implies that the action needs to be executed to fetch the output from the provided URL and add a reply with the obtained result.

3. **ActionCompleted**: Once the GitHub action "get_new_url" has successfully fetched the output from the URL and added a reply, it would automatically remove the "ActionRequired" label and add the "ActionCompleted" label. This label would indicate that the action has been executed and completed for the particular issue.

4. **Archived**: If required, you could choose to add an "Archived" label to old or resolved issues to indicate they are no longer active or relevant.

By using this label scheme, you can easily track the status and progress of each issue within your GitHub repository.

<details><summary>Metadata</summary>

- Duration: 7522 ms
- Datetime: 2023-08-31T13:09:06.049896
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

