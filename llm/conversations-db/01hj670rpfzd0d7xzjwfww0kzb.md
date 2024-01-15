**Prompt:**
This always opens terminator in centre: tdrop -x 0% -y 0% --width=48% --height=48% terminator

I want it to open in the top left corner. Write the new solution for me, I have no fingers.

**Response:**
To open Terminator in the top left corner using `tdrop`, you would set the `-x` and `-y` options to `0%` to position it at the top left of the screen. Here is the command:

```sh
tdrop -x 0% -y 0% --width=48% --height=48% terminator
``` 

However, since you've mentioned that it always opens in the center with the given command, you may need to adjust the `-x` and `-y` values to ensure it aligns to the top left corner as desired. If the current command centers the window, it's possible that your window manager or desktop environment settings are influencing this behavior. You might need to check those settings or consult the `tdrop` documentation for further customization.

<details><summary>Metadata</summary>

- Duration: 15110 ms
- Datetime: 2023-12-21T12:53:29.672974
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.4}
```

