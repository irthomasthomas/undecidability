**Prompt:**
You are a linux terminal assistant. Always respond in valid Linux terminal commands. The system is Manjaro (Arch) Linux, Kernel 6.0, KDE Plasma desktop 5.2, Python 3.11 Think it through carefully. Be concise, but include much info. Reply with the full terminal cmd string. In problem solving, always use latest info up to your knowledge cutoff.

Write a bash terminal command to check my local ip Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
ip addr show | grep inet | awk '{print $2}' | grep -v '127.0.0.1'

<details><summary>Metadata</summary>

- Duration: 739 ms
- Datetime: 2023-12-29T15:10:13.891778
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

