**Prompt:**
Bash_Command_Writer
Quickly, what is the right bash command to Record from my mic in bash? Here is output of: arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Generic [HD-Audio Generic], device 0: ALC1220 Analog [ALC1220 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Generic [HD-Audio Generic], device 2: ALC1220 Alt Analog [ALC1220 Alt Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0?
Say nothing else. Your output will be executed in shell directly, so only reply with the exact command text.

**Response:**
The right bash command to record from your mic would be:

```bash
arecord -f cd -D plughw:1,0 -t wav capture.wav
```

<details><summary>Metadata</summary>

- Duration: 1907 ms
- Datetime: 2023-07-13T17:21:47.626272
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

