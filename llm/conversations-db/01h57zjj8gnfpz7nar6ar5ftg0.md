**Prompt:**
bash record from mic using rec. Answer just the code

**Response:**
To record audio from the microphone using the `rec` command in Bash, you can use the following code:
```bash
rec -c 1 -r 44100 audio.wav
```
In this example, we are using `rec` to record mono audio (1 channel) at a sample rate of 44100 Hz and saving the recorded audio to a file named `audio.wav`. Adjust the channel (`-c`) and sample rate (`-r`) parameters as per your requirement.

<details><summary>Metadata</summary>

- Duration: 3350 ms
- Datetime: 2023-07-13T15:58:01.208898
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

