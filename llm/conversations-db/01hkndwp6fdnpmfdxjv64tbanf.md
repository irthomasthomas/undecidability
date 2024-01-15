**Prompt:**
Reformat the outputs to be pretty gh markdown
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

```bash
labels_csv=$(echo "$labels" | tr '\n' ',' | sed 's/,$//')
echo "labels_csv: $labels_csv" >&2

issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
```

<details><summary>Metadata</summary>

- Duration: 5948 ms
- Datetime: 2024-01-08T20:58:03.538693
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

