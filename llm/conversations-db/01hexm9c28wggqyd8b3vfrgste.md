**Prompt:**
Write a bash terminal command to get a table of pc specs and available resources. dont install anything
Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
lshw -short

<details><summary>Metadata</summary>

- Duration: 1090 ms
- Datetime: 2023-11-10T22:05:21.797216
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
I dont have lshw and no internet

**Response:**
cat /proc/cpuinfo && free -h && df -h

<details><summary>Metadata</summary>

- Duration: 835 ms
- Datetime: 2023-11-10T22:05:43.973185
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

