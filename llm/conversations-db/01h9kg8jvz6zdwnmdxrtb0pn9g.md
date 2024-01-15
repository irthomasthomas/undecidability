**Prompt:**
What is the best terminal command, small function, or script to run in order to: List my most frequently used commands?


**Response:**
history | awk '{print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 1527 ms
- Datetime: 2023-09-05T20:24:07.814967
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
I use zsh

**Response:**
history 1 | awk '{print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 1577 ms
- Datetime: 2023-09-05T20:24:41.386691
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
If $2 is sudo, get the next command in the string

**Response:**
history 1 | awk '{if ($2 == "sudo") print $3; else print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 2132 ms
- Datetime: 2023-09-05T20:29:31.358462
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
or, if it is echo, get the next one

**Response:**
history 1 | awk '{if ($2 == "sudo") print $3; else if ($2 == "echo") print $3; else print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 3437 ms
- Datetime: 2023-09-05T20:30:17.407059
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
$2 is "help" skip

**Response:**
history 1 | awk '{if ($2 == "sudo" || $2 == "echo") print $3; else if ($2 != "help") print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 2949 ms
- Datetime: 2023-09-05T20:31:27.401756
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
ignore apt

**Response:**
history 1 | awk '{if ($2 == "sudo" || $2 == "echo") print $3; else if ($2 != "help" && $2 != "apt") print $2}' | sort | uniq -c | sort -nr | head

<details><summary>Metadata</summary>

- Duration: 3373 ms
- Datetime: 2023-09-05T20:32:20.934753
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

