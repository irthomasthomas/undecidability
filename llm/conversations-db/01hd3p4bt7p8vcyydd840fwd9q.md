**Prompt:**
Write a bash terminal command to marry an app window to the terminal window it was launched from, such that mapping and unmapping operates on both the application and the seperate terminal window
Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
xdotool search --onlyvisible --class "application_class" windowmap %@ ; xdotool search --onlyvisible --class "terminal_class" windowmap %@

<details><summary>Metadata</summary>

- Duration: 4154 ms
- Datetime: 2023-10-19T10:01:34.732188
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.4}
```

