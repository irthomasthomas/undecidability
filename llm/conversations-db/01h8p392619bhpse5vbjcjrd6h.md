**Prompt:**
What is the exact zsh command to: I need to strip any lines similar to this before piping it to another tool: troff:<standard input>:2686: warning: cannot select font 'CW'
troff:<standard input>:2686: warning: cannot select font 'CW'
troff:<standard input>:2686: warning: cannot select font 'CW'
troff:<standard input>:2687: warning: cannot select font 'CW'
troff:<standard input>:2694: warning: cannot select font 'CW'
troff:<standard input>:2701: warning: cannot select font 'CW'
troff:<standard input>:2701: warning: cannot select font 'CW'?


**Response:**
grep -v "troff:<standard input>:"

<details><summary>Metadata</summary>

- Duration: 1554 ms
- Datetime: 2023-08-25T10:19:13.454655
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

