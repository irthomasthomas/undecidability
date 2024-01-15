**Prompt:**
in kde Plasma 5 on manjaro linux, list the stock icons in terminal

**Response:**
In the KDE Plasma environment, it is not possible to get a list of stock icons directly from the terminal because this information isn't stored in text format that can be accessed or printed via command line. Moreover, these icons are stored as image files, typically in the /usr/share/icons directory.

You can navigate to this directory and list subdirectories, each corresponding to an icon theme. Within each theme's folder, icons are typically categorized in subfolders like "actions", "apps", "devices", "status", etc.

Here is a command that can give you a list of directories and files within the icons directory:

```bash
ls /usr/share/icons
```

Keep in mind that this will also include icons for other desktop environments, if they are installed.

However, if you want to check icons specifically for KDE Plasma, you may navigate to 'Breeze' folder under icons directory which is default icon theme for Plasma 5.

For a more graphical representation, you may use File manager (Dolphin in Plasma) to view these icons.

<details><summary>Metadata</summary>

- Duration: 21212 ms
- Datetime: 2023-08-23T15:08:54.157730
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

