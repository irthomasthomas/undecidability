**Prompt:**
Write a bash terminal command to marry an app window to the terminal window it was launched from, such that mapping and unmapping operates on both the application and the seperate terminal window
Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
xdotool search --onlyvisible --pid $(xdotool getwindowpid $(xdotool getactivewindow)) windowmap --sync

<details><summary>Metadata</summary>

- Duration: 3765 ms
- Datetime: 2023-10-19T09:59:38.271144
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

