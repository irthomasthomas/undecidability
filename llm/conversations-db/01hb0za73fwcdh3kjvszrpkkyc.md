**Prompt:**
Write a bash terminal command to I have a collection of videos consisting of an MP4, an LRF, and an SRT file. I use the following command to rename them, however this will not work for the SRT files. How should those be handled?: exiftool -r -ext dng -ext jpg -ext tif -ext mov -ext mp4 -ext lrf -ext raf -ext png "-FileName<CreateDate" -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast && find . -type f -name "*.srt" -execdir sh -c 'mv "$0" "${0%.*}.srt"' {} ;
Warning: [minor] The ExtractEmbedded option may find more tags in the media data - ./DJI_0294.MP4
    1 directories scanned
    2 image files updated
find: missing argument to `-execdir'
 Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
exiftool -r -ext dng -ext jpg -ext tif -ext mov -ext mp4 -ext lrf -ext raf -ext png "-FileName<CreateDate" -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast && find . -type f -name "*.srt" -execdir sh -c 'mv "$0" "${0%.*}.srt"' {} \;

<details><summary>Metadata</summary>

- Duration: 5355 ms
- Datetime: 2023-09-23T12:12:55.555322
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

