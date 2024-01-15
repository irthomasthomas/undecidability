**Prompt:**
What are the options for --audio-source?

**Response:**
The `--audio-source` option in scrcpy allows you to select the audio source for audio forwarding. As of my knowledge cutoff date in early 2023, the available audio sources you can specify with this option are:

- `output`: Captures the device's audio output (what you would hear from the device's speakers or headphones).
- `mic`: Captures audio from the device's microphone.

To use this option, you would include it in your scrcpy command like this:

```sh
scrcpy --audio-source=output
```

or

```sh
scrcpy --audio-source=mic
```

The default value for `--audio-source` is `output`, which means that if you don't specify this option, scrcpy will capture the device's audio output by default.

<details><summary>Metadata</summary>

- Duration: 7010 ms
- Datetime: 2023-11-15T12:15:15.945575
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

