**Prompt:**
Quickly, what is the exact bash command to Record from my mic in bash? Here is output of: arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Generic [HD-Audio Generic], device 0: ALC1220 Analog [ALC1220 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Generic [HD-Audio Generic], device 2: ALC1220 Alt Analog [ALC1220 Alt Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0?
Reply only with the exact command text and nothing else before or after.

**Response:**
arecord -f cd -D plughw:1,0 -d 10 test.wav

<details><summary>Metadata</summary>

- Duration: 1229 ms
- Datetime: 2023-07-13T17:25:02.253760
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

