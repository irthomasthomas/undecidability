**Prompt:**
Speculate why does mpv player on arch saturate my cpu before my two nvidia gpus when playing multiple videos?

**Response:**
There could be several reasons for the observed behavior where mpv player on Arch Linux saturates the CPU before the two Nvidia GPUs when playing multiple videos. Here are a few possible explanations:

1. Hardware decoding: By default, mpv uses software decoding for video playback. Software decoding relies on the CPU to decode the video data and can be resource-intensive. If your Nvidia GPUs are not being utilized for hardware decoding, the CPU may be overloaded before the GPU resources are fully utilized.

2. Driver configuration: It is possible that the Nvidia GPU drivers are not properly configured to accelerate video playback in mpv. Make sure you have the latest Nvidia drivers installed and ensure that hardware acceleration options are enabled in your mpv configuration.

3. Video codec compatibility: The video codecs used in the multiple videos may not be optimally supported by the Nvidia GPU hardware decoding capabilities. Certain codecs may prioritize CPU decoding over GPU decoding, which could result in CPU saturation before GPU usage.

4. System resource allocation: The Linux kernel and other background processes may prioritize CPU usage over GPU resources. This can lead to CPU saturation before the GPUs are fully utilized. Adjusting system resource allocation settings or modifying kernel parameters might help ensure efficient utilization of GPU resources.

It is essential to delve into the specific configurations and settings of your Arch Linux system, specifically the mpv player and Nvidia GPU drivers, to investigate and resolve the issue thoroughly.

<details><summary>Metadata</summary>

- Duration: 21531 ms
- Datetime: 2023-11-02T20:20:46.340730
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

