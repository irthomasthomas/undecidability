**Prompt:**
Quickly, what is the exact bash command to grep the Exec= line after the [Desktop Entry] in file applications/brave-browser.desktop. Preview of file: applications/brave-browser.desktop?
Reply only with the exact command text and nothing else before or after.

**Response:**
awk '/Desktop Entry/,0' applications/brave-browser.desktop | grep Exec=

<details><summary>Metadata</summary>

- Duration: 1686 ms
- Datetime: 2023-07-31T18:01:09.581196
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.2}
```

