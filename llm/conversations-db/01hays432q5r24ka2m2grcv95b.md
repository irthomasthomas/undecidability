**Prompt:**
Write a bash terminal command to concatenate two mkv files Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
ffmpeg -i file1.mkv -i file2.mkv -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" output.mkv

<details><summary>Metadata</summary>

- Duration: 3976 ms
- Datetime: 2023-09-22T15:46:15.886035
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

