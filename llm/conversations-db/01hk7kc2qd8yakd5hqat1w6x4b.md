**Prompt:**
translate this to python: gh label list -L 999 --json name,description --jq '.[] | "\(.name):\(.description)"'      

**Response:**
```python
import subprocess
import json

command = ['gh', 'label', 'list', '-L', '999', '--json', 'name,description', '--jq', '.[] | "\(.name):\(.description)"']

output = subprocess.check_output(command).decode('utf-8')
labels = json.loads(output)

for label in labels:
    print(f"{label['name']}:{label['description']}")
```
Explanation:
1. The `subprocess` module is used to run the command `gh label list -L 999 --json name,description --jq '.[] | "\(.name):\(.description)"'` in the terminal.
2. The output of the command is captured and decoded from bytes to a string using the `decode('utf-8')` method.
3. The output is parsed as JSON using the `json.loads()` function.
4. A loop is used to iterate over each label in the parsed JSON.
5. The name and description of each label are printed using f-strings.

<details><summary>Metadata</summary>

- Duration: 4727 ms
- Datetime: 2024-01-03T12:04:29.935082
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

