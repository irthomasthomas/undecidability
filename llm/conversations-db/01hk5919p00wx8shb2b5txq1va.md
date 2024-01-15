**Prompt:**
Show me some example commands for gh labels with formatting for repo:irthomasthomas/undecidability


**Response:**
Sure! Here are some example commands for the `gh labels` command with formatting for the repository "irthomasthomas/undecidability":

1. List all labels in the repository:
   ```
   gh pr list -R irthomasthomas/undecidability --json name,color,description --jq '.[] | {name, color, description}' 
   ```

2. Create a new label in the repository:
   ```
   gh label create -R irthomasthomas/undecidability "bug" --color F00 --description "For reporting bugs"
   ```

3. Delete a label from the repository:
   ```
   gh label delete -R irthomasthomas/undecidability "bug"
   ```

4. Update a label in the repository:
   ```
   gh label edit -R irthomasthomas/undecidability "bug" --new-name "issue" --new-color F00 --new-description "For reporting issues"
   ```

5. Get information about a specific label in the repository:
   ```
   gh label view -R irthomasthomas/undecidability "bug" --json name,color,description --jq '{name, color, description}'
   ```

Note: Replace "irthomasthomas/undecidability" with your desired repository in the above commands.

<details><summary>Metadata</summary>

- Duration: 5827 ms
- Datetime: 2024-01-02T14:25:20.893326
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

