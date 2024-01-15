**Prompt:**
bash record from mic

**Response:**
To record audio from the microphone in bash, you can use the `arecord` command. Here's an example of how you can use it:

1. First, check the available recording devices on your system by running the following command:
```shell
arecord -l
```
This will display a list of available recording devices along with their corresponding device indices.

2. Once you have identified the desired recording device, you can start the recording using the following command:
```shell
arecord -D <device> -f cd -t wav -V stereo -c 2 -r 44100 output.wav
```
Replace `<device>` with the desired recording device's index or name.

This command specifies the options for recording:
- `-D` specifies the recording device.
- `-f` specifies the audio format (in this case, CD quality).
- `-t` specifies the audio file type (WAV in this example).
- `-V` specifies the recording volume (stereo in this example).
- `-c` specifies the number of channels (2 for stereo).
- `-r` specifies the sample rate (44100 Hz in this example).
- `output.wav` is the name of the output file where the recorded audio will be saved.

3. Press `Ctrl+C` to stop the recording.

After executing the command, the recording will be saved in the specified file (`output.wav` in this example).

<details><summary>Metadata</summary>

- Duration: 8905 ms
- Datetime: 2023-07-13T15:56:53.889754
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

