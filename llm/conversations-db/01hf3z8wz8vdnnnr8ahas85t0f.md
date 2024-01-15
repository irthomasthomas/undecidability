**Prompt:**
Change default browser from arch linux terminal

**Response:**
To change the default web browser on Arch Linux from the terminal, you will typically use the `xdg-settings` command, which is a command-line tool provided by `xdg-utils` package for configuring the default applications of a user's desktop environment.

First, make sure you have `xdg-utils` installed:

```bash
sudo pacman -S xdg-utils
```

Then, you can set the default browser using the `xdg-settings` command. For example, if you want to set Firefox as your default browser, you would use:

```bash
xdg-settings set default-web-browser firefox.desktop
```

Please note that the `.desktop` file for your desired browser must exist in `/usr/share/applications/` or `~/.local/share/applications/`. The name of the `.desktop` file might vary depending on the browser you want to set as default. For example, it could be `google-chrome.desktop` for Google Chrome or `chromium.desktop` for Chromium.

If you're not sure about the exact name of the `.desktop` file for your browser, you can list the available `.desktop` files using:

```bash
ls /usr/share/applications/*.desktop
```

or

```bash
ls ~/.local/share/applications/*.desktop
```

After you've set the new default browser, you can verify the change with:

```bash
xdg-settings get default-web-browser
```

This should return the `.desktop` file of the browser you've just set as default.

Keep in mind that some desktop environments might have their own settings that override the `xdg-settings`. If you're using GNOME, KDE, or another desktop environment with its own settings manager, you might need to use their specific tools or settings panels to change the default browser.

<details><summary>Metadata</summary>

- Duration: 11924 ms
- Datetime: 2023-11-13T09:12:36.435315
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

