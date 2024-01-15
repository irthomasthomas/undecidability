**Prompt:**
Debug command: tdrop -n Default - TopLeft -x 0% -y 0% --width=48% --height=48% --post-map-hook wmctrl -r 'konsole - Drop Down - Default - TopLeft' -b add,sticky konsole --class=Default - TopLeft --title konsole - Drop Down - Default - TopLeft
konsole: Unknown option 'class'.

**Response:**
The issue in the command is that the option "--class" is being interpreted as a separate argument instead of being part of the value for the "--title" option. To fix this, you can enclose the value for "--title" in quotes. Here's the corrected command:

tdrop -n Default -TopLeft -x 0% -y 0% --width=48% --height=48% --post-map-hook "wmctrl -r 'konsole - Drop Down - Default - TopLeft' -b add,sticky" konsole --title 'konsole - Drop Down - Default - TopLeft'

<details><summary>Metadata</summary>

- Duration: 13426 ms
- Datetime: 2023-10-15T19:02:21.562633
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

