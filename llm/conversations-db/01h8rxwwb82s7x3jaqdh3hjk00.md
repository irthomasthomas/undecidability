**Prompt:**
Handbrake Version: 1.6.1 (2023021700)
[12:53:08] gtkgui: Modified Preset: /Hardware/H.265 NVENC 1080p
[12:53:08] Starting work at: Sat Aug 26 12:53:08 2023

[12:53:08] 1 job(s) to process
[12:53:08] json job:
{
    "Audio": {
        "AudioList": [
            {
                "Bitrate": 160,
                "CompressionLevel": -1.0,
                "DRC": 0.0,
                "DitherMethod": "auto",
                "Encoder": "av_aac",
                "Gain": 0.0,
                "Mixdown": "stereo",
                "NormalizeMixLevel": false,
                "PresetEncoder": "av_aac",
                "Quality": -3.0,
                "Samplerate": 0,
                "Track": 0
            }
        ],
        "CopyMask": [
            "copy:aac"
        ],
        "FallbackEncoder": "none"
    },
    "Destination": {
        "AlignAVStart": false,
        "ChapterList": [
            {
                "Duration": {
                    "Hours": 0,
                    "Minutes": 26,
                    "Seconds": 16,
                    "Ticks": 141843600
                },
                "Name": "Chapter 1"
            }
        ],
        "ChapterMarkers": false,
        "File": "/home/tommy/Videos/DVD (2).mp4",
        "InlineParameterSets": false,
        "Mp4Options": {
            "IpodAtom": false,
            "Mp4Optimize": true
        },
        "Mux": "m4v"
    },
    "Filters": {
        "FilterList": [
            {
                "ID": 4,
                "Settings": {
                    "mode": "7"
                }
            },
            {
                "ID": 7,
                "Settings": {
                    "mode": 0
                }
            },
            {
                "ID": 14,
                "Settings": {
                    "crop-bottom": 0,
                    "crop-left": 0,
                    "crop-right": 0,
                    "crop-top": 0,
                    "height": 576,
                    "width": 720
                }
            }
        ]
    },
    "Metadata": {
        "Name": "DVD"
    },
    "PAR": {
        "Den": 45,
        "Num": 64
    },
    "SequenceID": 0,
    "Source": {
        "Angle": 0,
        "Path": "/run/media/tommy/DVD",
        "Range": {
            "End": 1,
            "Start": 1,
            "Type": "chapter"
        },
        "Title": 1
    },
    "Subtitle": {
        "Search": {
            "Burn": true,
            "Default": false,
            "Enable": false,
            "Forced": false
        },
        "SubtitleList": []
    },
    "Video": {
        "Bitrate": 5000,
        "ChromaLocation": 1,
        "ColorInputFormat": 0,
        "ColorMatrix": 6,
        "ColorOutputFormat": 0,
        "ColorPrimaries": 5,
        "ColorRange": 1,
        "ColorTransfer": 1,
        "Encoder": "nvenc_h264",
        "HardwareDecode": 0,
        "Level": "auto",
        "Options": "",
        "Preset": "medium",
        "Profile": "auto",
        "QSV": {
            "AdapterIndex": 0,
            "AsyncDepth": 0,
            "Decode": false
        },
        "Tune": "",
        "Turbo": false,
        "TwoPass": false
    }
}
[12:53:08] CPU: AMD Ryzen 9 5950X 16-Core Processor            
[12:53:08]  - logical processor count: 32
[12:53:08] Intel Quick Sync Video support: no
[12:53:08] hb_scan: path=/run/media/tommy/DVD, title_index=1
disc.c:437: error opening file BDMV/index.bdmv
disc.c:437: error opening file BDMV/BACKUP/index.bdmv
[12:53:08] bd: not a bd - trying as a stream/file instead
libdvdnav: Can't read name block. Probably not a DVD-ROM device.
[12:53:08] scan: DVD has 12 title(s)
[12:53:08] scan: scanning title 1
[12:53:08] scan: duration is 00:26:16 (1576040 ms)
[12:53:08] pgc_id: 1, pgn: 1: pgc: 0x7fbf2000eff0
[12:53:08] scan: checking audio 1
[12:53:08] scan: id=0x80bd, lang=English (AC3), 3cc=eng ext=0
[12:53:08] scan: title 1 has 1 chapters
[12:53:08] scan: chap 1, 1576040 ms
[12:53:08] scan: aspect = 16:9
[12:53:08] scan: decoding previews for title 1
[12:53:08] scan: title angle(s) 1
[12:53:08] scan: audio 0x80bd: ac3, rate=48000Hz, bitrate=192000 English (AC3) (2.0 ch) (192 kbps)
[12:53:08] scan: 10 previews, 720x576, 25.000 fps, autocrop = 0/0/0/0, aspect 16:9, PAR 64:45, color profile: 5-1-6, chroma location: left
[12:53:08] libhb: scan thread found 1 valid title(s)
[12:53:08] Starting Task: Encoding Pass
[12:53:08] Skipping vfr filter
[12:53:08] Skipping crop/scale filter
[12:53:08] job configuration:
[12:53:08]  * source
[12:53:08]    + /run/media/tommy/DVD
[12:53:08]    + title 1, chapter(s) 1 to 1
[12:53:08]  * destination
[12:53:08]    + /home/tommy/Videos/DVD (2).mp4
[12:53:08]    + container: MPEG-4 (libavformat)
[12:53:08]      + optimized for HTTP streaming (fast start)
[12:53:08]  * video track
[12:53:08]    + decoder: mpeg2video 8-bit (yuv420p)
[12:53:08]      + bitrate 200 kbps
[12:53:08]    + filter
[12:53:08]      + Decomb (mode=7)
[12:53:08]    + Output geometry
[12:53:08]      + storage dimensions: 720 x 576
[12:53:08]      + pixel aspect ratio: 64 : 45
[12:53:08]      + display dimensions: 1024 x 576
[12:53:08]    + encoder: H.264 (NVEnc)
[12:53:08]      + preset:  medium
[12:53:08]      + profile: auto
[12:53:08]      + level:   auto
[12:53:08]      + bitrate: 5000 kbps, pass: 0
[12:53:08]      + color profile: 5-1-6
[12:53:08]      + chroma location: left
[12:53:08]  * audio track 1
[12:53:08]    + decoder: English (AC3) (2.0 ch) (192 kbps) (track 1, id 0x80bd)
[12:53:08]      + bitrate: 192 kbps, samplerate: 48000 Hz
[12:53:08]    + mixdown: Stereo
[12:53:08]    + encoder: AAC (libavcodec)
[12:53:08]      + bitrate: 160 kbps, samplerate: 48000 Hz
libdvdnav: Can't read name block. Probably not a DVD-ROM device.
[12:53:08] sync: expecting 39401 video frames
[12:53:08] encavcodecInit: H.264 (Nvidia NVENC)
[12:53:08] encavcodec: encoding at rc=vbr, multipass=fullres, Bitrate 5000
[12:53:08] encavcodec: encoding with stored aspect 64/45
[mpeg2video @ 0x7fbf34003180] Application has requested 17 threads. Using a thread count greater than 16 is not recommended.
[12:53:08] sync: first pts video is 0
[12:53:08] sync: "Chapter 1" (1) at frame 1 time 0
[12:53:08] sync: first pts audio 0x80bd is 0
[12:53:47] reader: done. 1 scr changes
[12:53:47] work: average encoding speed for job is 1024.278198 fps
[12:53:47] decomb: deinterlaced 39401 | blended 0 | unfiltered 0 | total 39401
[12:53:47] ac3-decoder done: 49245 frames, 0 decoder errors
[12:53:47] mpeg2video-decoder done: 39401 frames, 0 decoder errors
[12:53:47] sync: got 39401 frames, 39401 expected
[12:53:47] sync: framerate min 25.000 fps, max 25.000 fps, avg 25.000 fps
[aac @ 0x7fbf080d1e80] Ignoring attempt to flush encoder that doesn't support it
[aac @ 0x7fbf080d1e80] Qavg: 1119.508
[mp4 @ 0x7fbf09016b40] Starting second pass: moving the moov atom to the beginning of the file
[12:53:47] mux: track 0, 39401 frames, 933163532 bytes, 4736.63 kbps, fifo 1024
[12:53:47] mux: track 1, 73868 frames, 31409948 bytes, 159.43 kbps, fifo 2048
[12:53:47] Finished work at: Sat Aug 26 12:53:47 2023

[12:53:47] libhb: work result = 0
 Log file from handbrake run. Summarize useful benchmarking statistics

**Response:**
Handbrake Version: 1.6.1 (2023021700)
Time of processing: Sat Aug 26 12:53:08 2023 - Sat Aug 26 12:53:47 2023
Number of jobs: 1
Video track: 
- Decoder: mpeg2video 8-bit (yuv420p)
- Bitrate: 200 kbps
- Filter: Decomb (mode=7)
- Output geometry: 720 x 576
- Encoder: H.264 (NVEnc)
- Preset: medium
- Profile: auto
- Level: auto
- Bitrate: 5000 kbps
Audio track: 
- Decoder: English (AC3) (2.0 ch) (192 kbps)
- Bitrate: 192 kbps
- Samplerate: 48000 Hz
- Mixdown: Stereo
- Encoder: AAC (libavcodec)
- Bitrate: 160 kbps
- Samplerate: 48000 Hz
Summary of statistics:
- Average encoding speed: 1024.278198 fps
- Deinterlaced frames: 39401
- Blended frames: 0
- Unfiltered frames: 0
- Total frames: 39401
- Decoded audio frames: 49245
- Decoded video frames: 39401
- Framerate: min 25.000 fps, max 25.000 fps, avg 25.000 fps
- Qavg (average quality): 1119.508
- Track 0: 39401 frames, 933163532 bytes, 4736.63 kbps
- Track 1: 73868 frames, 31409948 bytes, 159.43 kbps

<details><summary>Metadata</summary>

- Duration: 16054 ms
- Datetime: 2023-08-26T12:42:40.177317
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{}
```

