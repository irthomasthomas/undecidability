**Prompt:**
translate this to python: gh label list -L 999 --json name,description --jq '.[] | "\(.name):\(.description)"'      

**Response:**
```python
import subprocess
import json

command = ['gh', 'label', 'list', '-L', '999', '--json', 'name,description', '--jq', '.[] | "\(.name):\(.description)"']

result = subprocess.run(command, capture_output=True, text=True)
output = result.stdout.strip()

labels = json.loads(output)
for label in labels:
    print(f"{label['name']}:{label['description']}")
```

Explanation:
1. The `subprocess` module is used to run the command `gh label list -L 999 --json name,description --jq '.[] | "\(.name):\(.description)"'` in the shell.
2. The `capture_output=True` argument captures the command's output.
3. The `text=True` argument ensures that the output is returned as a string.
4. The output is then parsed as JSON using `json.loads()`.
5. Finally, a loop is used to print the name and description of each label in the desired format.

<details><summary>Metadata</summary>

- Duration: 5345 ms
- Datetime: 2024-01-03T12:04:55.732197
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

