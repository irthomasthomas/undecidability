**Prompt:**
translate this to python: gh label list -L 999 --json name,description --jq '.[] | "\(.name):\(.description)"'      

**Response:**
```python
import subprocess
import json

# Run the GitHub CLI command and capture the output
result = subprocess.run(
    ['gh', 'label', 'list', '-L', '999', '--json', 'name,description'],
    capture_output=True,
    text=True
)

# Parse the JSON output
labels = json.loads(result.stdout)

# Format the labels as "name:description"
formatted_labels = [f"{label['name']}:{label['description']}" for label in labels]

# Output the formatted labels
for label in formatted_labels:
    print(label)
```

<details><summary>Metadata</summary>

- Duration: 11564 ms
- Datetime: 2024-01-03T12:05:06.284903
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

