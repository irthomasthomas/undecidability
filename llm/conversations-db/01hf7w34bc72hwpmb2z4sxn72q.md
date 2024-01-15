**Prompt:**
What does the man say about mic?

**Response:**
The `scrcpy` manual does not have a dedicated section for "mic," but it does mention options related to audio, which include the microphone. Here are the relevant options that involve the microphone:

- `--audio-source=source`: This option allows you to select the audio source. The two possible values are `output` (the device's audio output, such as the sound from a game or video) and `mic` (the device's microphone input). By default, `scrcpy` captures the device's audio output.

- `--audio-codec=name`: This option lets you select an audio codec (`opus`, `aac`, or `raw`) for encoding the audio stream from the device.

- `--audio-bit-rate=value`: This option sets the bit rate for audio encoding, which affects the quality of the audio stream.

- `--audio-buffer=ms`: This option configures the audio buffering delay in milliseconds, which can affect audio latency and the likelihood of buffer underrun (audio glitches).

- `--audio-encoder=name`: This option allows you to use a specific MediaCodec audio encoder, which can be listed using the `--list-encoders` option.

- `--no-audio`: This option disables audio forwarding altogether, so no audio from the device (neither from the output nor the microphone) will be captured.

If you want to capture audio from the device's microphone instead of the audio output, you would use the `--audio-source=mic` option when starting `scrcpy`.

<details><summary>Metadata</summary>

- Duration: 10120 ms
- Datetime: 2023-11-14T21:34:01.187481
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

