**Prompt:**
Write a bash terminal command to I have a collection of videos consisting of an MP4, an LRF, and an SRT file. I use the following command to rename them, however this will not work for the SRT files. How should those be handled?: exiftool -r -ext dng -ext jpg -ext tif -ext mov -ext mp4 -ext srt -ext lrf -ext raf -ext png  "-FileName<CreateDate" -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
 Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
exiftool -r -ext dng -ext jpg -ext tif -ext mov -ext mp4 -ext lrf -ext raf -ext png "-FileName<CreateDate" -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast && find . -type f -name "*.srt" -execdir sh -c 'mv "$0" "${0%.*}.srt"' {} \;

<details><summary>Metadata</summary>

- Duration: 4645 ms
- Datetime: 2023-09-23T12:07:57.892939
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

