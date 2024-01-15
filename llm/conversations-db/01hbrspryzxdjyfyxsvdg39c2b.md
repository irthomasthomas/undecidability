**Prompt:**
Open video in mpv player zoomed 50%

**Response:**
To open a video in MPV player and zoom it to 50%, you can follow these steps:

1. Open your preferred terminal or command prompt on your computer.
2. Navigate to the directory containing the video file. For example, if the video file is in the "Videos" folder on your desktop, you can use the following command to navigate there:

```bash
cd ~/Desktop/Videos
```

3. Once you are in the correct directory, use the following command to open the video in MPV player and set the zoom level to 50%:

```bash
mpv --vf=scale=50 my_video.mp4
```

Replace "my_video.mp4" with the actual name of your video file.

4. MPV will launch and play the video with a zoomed-in 50% scale.

Note: The zoom level can be adjusted by changing the value after `scale=` in the command. For example, `--vf=scale=75` will set the zoom level to 75%.

<details><summary>Metadata</summary>

- Duration: 4336 ms
- Datetime: 2023-10-02T18:16:42.989969
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

