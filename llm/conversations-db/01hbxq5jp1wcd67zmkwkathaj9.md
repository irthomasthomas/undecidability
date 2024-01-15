**Prompt:**
❯ streamdeck
Exception in thread Thread-1 (_run):
Traceback (most recent call last):
  File "/usr/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/stream_deck_monitor.py", line 117, in _run
    self.attached(streamdeck_id, streamdeck)
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/api.py", line 219, in attached
    self.update_streamdeck_filters(serial_number)
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/api.py", line 661, in update_streamdeck_filters
    self.update_button_filters(serial_number, page, button)
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/api.py", line 700, in update_button_filters
    filters.append(TextFilter(text, font, font_size, font_color, vertical_align, horizontal_align))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/display/text_filter.py", line 25, in __init__
    self.true_font = ImageFont.truetype(font, font_size)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/PIL/ImageFont.py", line 791, in truetype
    return freetype(font)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/PIL/ImageFont.py", line 788, in freetype
    return FreeTypeFont(font, size, index, encoding, layout_engine)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/PIL/ImageFont.py", line 226, in __init__
    self.font = core.getfont(
                ^^^^^^^^^^^^^
OSError: cannot open resource


**Response:**
The error message you are seeing indicates that there is an issue with loading a font resource required by the Stream Deck software. This could be caused by a missing or inaccessible font file.

To troubleshoot this issue, you can try the following steps:

1. Make sure that the font specified in the `streamdeck_ui` configuration is correctly installed on your system. You can check for the font file in the specified location.

2. If the font is missing, you can try reinstalling it or using a different font that you have installed on your system. Update the configuration file accordingly.

3. If the font is present and accessible, it's possible that there is a permissions issue preventing the software from accessing the font file. Ensure that the file has the correct permissions and is readable by the user running the Stream Deck software.

4. If none of the above steps resolve the issue, you can try reinstalling the Stream Deck software or checking for any updates that may address this problem.

Please let me know if you need further assistance or more detailed instructions for any of the troubleshooting steps.

<details><summary>Metadata</summary>

- Duration: 7769 ms
- Datetime: 2023-10-04T16:08:31.073760
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
walk me through it

**Response:**
Certainly! Here's a step-by-step guide to troubleshooting the font-related issue with the Stream Deck software:

1. Open a file manager and navigate to the location specified in the error message: `/usr/lib/python3.11/site-packages/streamdeck_ui/display/text_filter.py`. Check the configuration file to see which font is being used.

2. Make sure that the font mentioned in the configuration file is installed on your system. You can check for the presence of the font file in the specified location or search for it using your file manager or a command-line tool like `find`.

3. If the font file is missing, you can try reinstalling it. Depending on your distribution, you may be able to install the missing font package using your package manager. For example, on Manjaro, you can use the `pamac` or `pacman` command to search and install fonts. For instance, you can try `sudo pamac install ttf-dejavu` to install the DejaVu font package.

4. If the font is installed or after reinstalling it, check its permissions. Right-click on the font file, select "Properties," and navigate to the "Permissions" tab. Ensure that the file has read permissions for the user running the Stream Deck software.

5. If the permissions are correct, try running the Stream Deck software again and see if the issue persists. If the problem persists, it may be necessary to reinstall the Stream Deck software or check for any updates that might address the font-related problem.

Remember, if you need any further assistance or encounter any difficulties during any of these steps, I'm here to help!

<details><summary>Metadata</summary>

- Duration: 9744 ms
- Datetime: 2023-10-04T16:10:45.329383
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

