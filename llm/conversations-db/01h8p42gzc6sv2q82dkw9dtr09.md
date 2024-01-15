**Prompt:**
Can I alias a missing font in linux so that troff does not complain about cannot select font 'CW'

**Response:**
Yes, you can manually specify a substitution for the missing font in Groff or Troff on Linux.

Here's an instructions on how to do that:

1. Edit your troff or groff alias file, the common locations are `/usr/share/groff/current/font/devps/` or `/usr/share/groff/current/font/devpdf/`. If these directories do not exist, you might want to search for them using the `locate devps` command.

2. Look for a file in the above directory called `download` or `FONT_ALIAS`.

3. Open the `download` or `FONT_ALIAS` file with a text editor and add an alias for the missing font. The syntax is `<missing_font_name> <font_to_use>`.

For example, if troff cannot select the font 'CW', but you happen to have a font 'PA', you could add to the alias file:

```
CW PA
```

4. Save the file and exit the text editor.

5. After that run the `updmap` command on the command prompt to update the map file.

Now, troff should use the 'PA' font when 'CW' is requested.

Please note that this method assumes that the font you are "aliasing" to (in this case 'PA') works correctly within troff/groff. If it doesn't, you may need to download additional fonts or specify different available ones in its stead.

<details><summary>Metadata</summary>

- Duration: 29338 ms
- Datetime: 2023-08-25T10:32:40.016790
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

