**Prompt:**
Write a bash terminal command to Debug command: tdrop -n Default - TopLeft -x 0% -y 0% --width=48% --height=48% --post-map-hook wmctrl -r 'konsole - Drop Down - Default - TopLeft' -b add,sticky konsole --class=Default - TopLeft --title konsole - Drop Down - Default - TopLeft
konsole: Unknown option 'class'. Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
tdrop -n Default -TopLeft -x 0% -y 0% --width=48% --height=48% --post-map-hook "wmctrl -r 'konsole - Drop Down - Default - TopLeft' -b add,sticky" konsole --title "konsole - Drop Down - Default - TopLeft"

<details><summary>Metadata</summary>

- Duration: 6929 ms
- Datetime: 2023-10-15T18:57:14.685383
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

