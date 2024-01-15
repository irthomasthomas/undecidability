**Prompt:**
Add a cover image to an mkv video?

**Response:**
To add a cover image to an MKV video file, you can use the `mkvpropedit` command from the MKVToolNix suite. Here's a command-line example:

```sh
mkvpropedit video.mkv --attachment-name "cover.jpg" --attachment-mime-type "image/jpeg" --add-attachment cover.jpg
```

Replace `video.mkv` with the path to your MKV file and `cover.jpg` with the path to your image file. The `--attachment-name` and `--attachment-mime-type` options are used to specify the filename and MIME type that will be stored in the MKV file.

<details><summary>Metadata</summary>

- Duration: 9216 ms
- Datetime: 2023-11-21T13:33:11.483528
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

