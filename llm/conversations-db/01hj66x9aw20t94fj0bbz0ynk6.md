**Prompt:**
This always opens terminator in centre. I want it be in the top left corner

tdrop -x 0% -y 0% --width=48% --height=48% terminator

**Response:**
Use the `--geometry` option to set the window position to the top left corner:

```sh
terminator --geometry=+0+0
```

<details><summary>Metadata</summary>

- Duration: 3268 ms
- Datetime: 2023-12-21T12:51:47.479230
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.4}
```

