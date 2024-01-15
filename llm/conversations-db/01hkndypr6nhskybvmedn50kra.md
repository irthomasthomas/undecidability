**Prompt:**
Reformat the suggested labels and body to be pretty gh markdown
 task_list="- [ ] [${TITLE}](${URL})"
    suggested_labels="## Suggested labels

$gh_markdown_highlight_generated_labels"
    
    BODY="$task_list

$DESCRIPTION

$suggested_labels"
    labels_csv=$(echo "$labels" | tr '
' ',' | sed 's/.$//')
    echo "labels_csv: $labels_csv" >&2
    
    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")

**Response:**
```markdown
- [ ] [${TITLE}](${URL})

${DESCRIPTION}

## Suggested labels

\`\`\`
$gh_markdown_highlight_generated_labels
\`\`\`
```

The `labels_csv` variable is correctly formatted for a shell script and does not need Markdown formatting. The `issue_url` variable is the result of a command and also does not require Markdown formatting.

<details><summary>Metadata</summary>

- Duration: 3541 ms
- Datetime: 2024-01-08T20:59:12.049073
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

