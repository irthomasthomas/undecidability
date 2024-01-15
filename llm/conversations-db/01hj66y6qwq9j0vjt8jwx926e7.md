**Prompt:**
This always opens terminator in centre. I want it be in the top left corner. Write the whole solution, I have no hands. Heres fiddy dollars.

tdrop -x 0% -y 0% --width=48% --height=48% terminator

**Response:**
To open Terminator in the top left corner, use the `--geometry` option with the appropriate X and Y coordinates. Here's the command:

```sh
terminator --geometry=+0+0
```

<details><summary>Metadata</summary>

- Duration: 2801 ms
- Datetime: 2023-12-21T12:52:18.059311
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.4}
```

