**Prompt:**
NOTIFY-SEND(1)                                          User Commands                                         NOTIFY-SEND(1)

NAME
       notify-send - a program to send desktop notifications

SYNOPSIS

       notify-send [OPTIONS] {summary} [body]

DESCRIPTION
       With notify-send you can send desktop notifications to the user via a notification daemon from the command line.
       These notifications can be used to inform the user about an event or display some form of information without getting
       in the user’s way.

OPTIONS
       -?, --help
           Show help and exit.

       -a, --app-name=APP_NAME
           Specifies the app name for the notification.

       -A, --action=[NAME=]Text...
           Specifies the actions to display to the user. Implies --wait to wait for user input. May be set multiple times.
           The NAME of the action is output to stdout. If NAME is not specified, the numerical index of the option is used
           (starting with 1).

       -u, --urgency=LEVEL
           Specifies the urgency level (low, normal, critical).

       -t, --expire-time=TIME
           The duration, in milliseconds, for the notification to appear on screen.

           Not all implementations use this parameter. GNOME Shell and Notify OSD always ignore it, while Plasma ignores it
           for notifications with the critical urgency level.

       -i, --icon=ICON
           Specifies an icon filename or stock icon to display.

       -c, --category=TYPE[,TYPE...]
           Specifies the notification category.

       -h, --hint=TYPE:NAME:VALUE
           Specifies basic extra data to pass. Valid types are BOOLEAN, INT, DOUBLE, STRING, BYTE and VARIANT.

       -p, --print-id
           Print the notification ID.

       -r, --replace-id=REPLACE_ID
           The ID of the notification to replace.

       -w, --wait
           Wait for the notification to be closed before exiting. If the expire-time is set, it will be used as the maximum
           waiting time.

       -e, --transient
           Show a transient notification. Transient notifications by-pass the server's persistence capability, if any. And
           so it won't be preserved until the user acknowledges it.

SEE ALSO
       The Desktop Notification Spec on https://specifications.freedesktop.org/notification-spec/.

AUTHORS
       Andre Filipe de Assuncao e Brito <decko@noisemakers.org>
           Original author

       Paul van Tilburg <paulvt@debian.org>
           Original author

       Riccardo Setti <giskard@debian.org>
           Original author

libnotify                                                                                                     NOTIFY-SEND(1)
 What are stock icons and how do I use them?

**Response:**
Stock icons refer to a set of predefined icons that are commonly available in most desktop environments. These icons are provided by the window manager or the icon theme and can be used by applications to display consistent and familiar icons in their user interface.

To use stock icons with the `notify-send` command, you need to provide the name of the stock icon as the value for the `-i` or `--icon` option. The name of the stock icon is usually in the format `icon-name` or `icon-theme-icon-name`, where `icon-name` is the name of the specific icon you want to use and `icon-theme` is the name of the icon theme.

For example, if you want to use the "info" stock icon from the default icon theme, you can use the following command:

```
notify-send -i info "Title" "Message"
```

This will display a notification with the "info" icon.

Note that the availability of stock icons may vary depending on the desktop environment and the installed icon themes.

<details><summary>Metadata</summary>

- Duration: 11088 ms
- Datetime: 2023-08-23T15:06:20.939083
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
how do I find the list of available stock icons?

**Response:**
To find the list of available stock icons, you can use the `gtk3-icon-browser` tool. The tool allows you to browse and search for stock icons provided by the GTK theme.

Here are the steps to use `gtk3-icon-browser`:

1. Install the `gtk-3-examples` package, which includes the `gtk3-icon-browser` tool. Use the package manager for your Linux distribution to install it. For example, on Ubuntu, you can use the following command:

   ```
   sudo apt-get install gtk-3-examples
   ```

2. Once the `gtk3-icon-browser` tool is installed, you can launch it from the command line:

   ```
   gtk3-icon-browser
   ```

3. The tool will open a graphical interface where you can browse and search for available stock icons. You can scroll through the list of icons, filter them by name, or search for a specific icon using keywords.

4. When you find the stock icon you want to use, you can take note of its name and use it with the `notify-send` command's `-i` or `--icon` option. For example, if you find an icon named "dialog-information", you can use it like this:

   ```
   notify-send -i dialog-information "Title" "Message"
   ```

This method allows you to explore the stock icons provided by the GTK theme and choose the ones that suit your requirements.

<details><summary>Metadata</summary>

- Duration: 14747 ms
- Datetime: 2023-08-23T15:07:11.667747
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

