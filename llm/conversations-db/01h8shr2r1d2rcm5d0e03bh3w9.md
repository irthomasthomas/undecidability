**Prompt:**
In manjaro (arch) linux, quickly preview a png photo, without opening it in the default image viewer

**Response:**
The easiest way to quickly preview a photo is to install a terminal file manager which has the ability to preview files like 'Ranger'. To install 'Ranger', use the following steps:

1) Open the terminal.

2) Type the following command to install Ranger:

```
sudo pacman -S ranger
```

3) To preview a photo, navigate to the directory containing the photo using the 'cd' command. 

For example, if your photo is in the Downloads folder you can type:

```
cd ~/Downloads
```

4) Open Ranger by simply typing 'ranger' into the terminal:

```
ranger
```

5) Once in Ranger, you can navigate through directories using arrow keys or 'h', 'j', 'k', 'l' keys. Most of the controls are similar to Vim. When you highlight a photo file, it's preview will be shown in Ranger.

Remember, 'Ranger' will need to be run in a terminal emulator that supports image previews for this to work.

Please note that this depends on your terminal and may not work on all terminals. It is confirmed to work on "Kitty", "URxvt" and "st" with some configuration. For others like "GNOME Terminal" and "Alacritty", it may require additional software or scripts.

<details><summary>Metadata</summary>

- Duration: 21618 ms
- Datetime: 2023-08-26T18:29:28.845727
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

