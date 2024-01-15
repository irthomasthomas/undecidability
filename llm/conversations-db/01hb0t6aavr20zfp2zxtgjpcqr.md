**Prompt:**
Write a bash terminal command to this dir contains files like: VID_20220521112744.m4a.wav. Rename them to remove the .m4a section, but leave the basename and .wav. Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
for file in *.m4a.wav; do mv "$file" "${file/.m4a/}"; done

<details><summary>Metadata</summary>

- Duration: 1732 ms
- Datetime: 2023-09-23T10:43:28.534612
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

