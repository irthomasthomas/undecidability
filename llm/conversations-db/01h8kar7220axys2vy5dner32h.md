**Prompt:**
TDROP(1)                                                                                                                          tdrop man page                                                                                                                         TDROP(1)

NAME
       Tdrop - make dropdown terminals and windows

SYNOPSIS
       tdrop [OPTIONS] [program name or cmd] [program options ...]

DESCRIPTION
            Tdrop  is used for hiding/unhiding programs to acheive quake/dropdown functionality. It can create a dropdown window if one does not already exist or turn the current window into a dropdown on the fly. It provides options to control the intial size and position
       of dropdowns, for example to leave panels visible or to deal with window borders. When used with a terminal, it provides an option to specify the name of a tmux session to automatically start. It also allows the user to specify arbitrary  options/flags  to  be  used
       when starting programs. It uses window IDs as opposed to classes, so it can be used with multiple windows of the same program.

            It also has the ability to automatically hide and automatically show dropdowns. For example, it can be used to automatically hide a terminal when opening something from it, e.g. an image viewer, video player, etc. Tdrop can         then automatically bring back
       the terminal whenever the image view, video player, etc. is closed. See the Examples section for more information.

Commands
       Tdrop expects the name of a program or 'current' (to use the current window) as the last argument to create a dropdown (optionally followed by any flags to that program). Alternatively, it can take one of auto_show, auto_hide, toggle_auto_hide, hide_all, or foreach.
       If hide_all is given instead of a program name, tdrop will hide all visible dropdowns.

       Foreach will run a run a command for each dropdown. For example, you can do the equivalent of hide_all with the following:

       tdrop foreach 'unmap $wid'

       To hide floating dropdowns only on herbstluftwm:

       tdrop foreach 'herbstclient compare clients.$(printf 0x%x $wid).floating = on && unmap $wid'

       Tdrop's functionality (except potentially foreach) is not particularly useful called directly from the command line. Commands should either be bound to a key, used in shell functions/aliases, or used with a file opener (e.g. in the rifle.conf).

OPTIONS
       E.g.
       $ tdrop -y 15 termite
       $ tdrop --y-offset=15 termite
       $ tdrop --y-offset 15 termite

       Note that all hook and command related options can make use of any tdrop variables (such as $width, $height, $xoff, $yoff, $class, $wid, etc.). Note that for some of the hooks, the window id is not guarunteed to be known (since the window may not have yet been cre‐
       ated), so any scripts that make use of these should check if it is defined (pre-map and pre-float; wid will never be known for pre-create).

       -w WIDTH,  --width=WIDTH
              Specify  a  width  for  a  created window as a number or percentage. A negative number is allowed (e.g. '-w -4') in which case the width will be that many pixels less than 100% of the screen size (or monitor size if '-m' is being used). This fixes the problem
              where 100% width may actually go over the screen due to window borders/decoration. The other other geometry options also accept negative values ('-h', '-x', and '-y'). If both the width and height are specified as empty/"", do not  alter  the  window's  size.
              (default: 100%)

       -h HEIGHT,  --height=HEIGHT
              Specify a height for a created window as a number or percentage. If both the width and height are specified as empty/"", do not alter the window's size. (default: 45%)

       -x OFFSET,  --x-offset=OFFSET
              Specify the x position for a created window as a number or percentage. If both the x and y offsets are specified as empty/"", do not alter the window's position. (default: 0)

       -y OFFSET,  --y-offset=OFFSET
              Specify the y position for a created window as a number or percentage. If both the x and y offsets are specified as empty/"", do not alter the window's position. (default: 1, see BUGS)

       -s NAME,  --session=NAME
              Specify  a tmuxinator, tmuxifier, or tmux session name to start. An existing tmux session has highest precedence and will be connected to with '-d', detaching other attached clients. If a there is no tmuxinator/tmuxifier/etc. session of the given name, a nor‐
              mal tmux session with the name will be created. If this option is not given, tmux will not be used. Note that this option requires that the program be a supported terminal. (default: none)

       -n NUMBER,  --number=NUMBER
              Specify a number (or any extra text) to differentiate between dropdowns of the same program (this is only needed when using multiple dropdowns of the same program). This flag can also be used for creating multiple different dropdowns on the  fly  ('current').
              Note that it is not necessary to use this to deal with multi-user systems as tdrop stores dropdown information separately for each user. (default: none)

       -c COMMAND,  --pre-create-hook=COMMAND
              Specify a command to execute before first creating or initializing a dropdown (before mapping a normal dropdown or before unmapping the 'current' window). This flag has no effect for the auto_(hide|show) commands. (default: none)

       -C,  --post-create-hook=COMMAND
              Specify a command to execute after first creating or initializing a dropdown (after mapping a normal dropdown or after unmapping the 'current' window). This flag has no effect for the auto_(hide|show) commands. (default: none)

       -p COMMAND,  --pre-map-hook=COMMAND
              Specify a command to execute before showing/mapping a dropdown. Note that this will run when showing a dropdown for the first time even when --pre-create-hook is used. (default: none)

       -P COMMAND,  --post-map-hook=COMMAND
              Specify a command to execute after showing/mapping a dropdown. Note that this will run when hiding a dropdown for the first time even when --post-create-hook is used. (default: none)

       -u COMMAND,  --pre-unmap-hook=COMMAND
              Specify a command to execute before hiding/unmapping a dropdown. (default: none)

       -U COMMAND,  --post-unmap-hook=COMMAND
              Specify a command to execute after hiding/unmapping a dropdown. (default: none)

       -l COMMAND,  --pre-map-float-command=COMMAND
              Specify  a  command execute before showing/mapping a dropdown in order to float the dropdown (e.g. a bspwm oneshot rule). This may be useful if you don't want to float all windows of a given program and tdrop doesn't automatically support this for your window
              manager with the -a flag. This will override any default floating command when used with -a.

       -L COMMAND,  --post-map-float-command=COMMAND
              Specify a command execute after showing/mapping a dropdown in order to float the dropdown. This may be useful if you don't want to float all windows of a given program and tdrop doesn't automatically support this for your window manager with the -a flag. This
              can be used if your window manager does not support floating rules at all; for example, it can be used to fake a key combination (e.g. using xdotool) that will float the current window. This will override any default floating command when used with -a.

       -d DEC_SIZE,  --decoration-fix=DEC_SIZE
              Specify a window decoration/border size in the form <x decoration size>x<y decoration size> to be taken into account when saving window position. This should not be necessary for most window managers and is only used with  'auto_show',  e.g.  'tdrop  -d  1x22
              auto_show' for blackbox. (default: none)

       -S,  --no-subtract-when-same
              This  option is a more complicated companion to -d that is also unlikely to be needed. This is used to determine how to calculate the X and Y position of a window using xwininfo when 'auto_hide' is used (if the absolute and relative X or Y values are reported
              as the same, this option determines the behavior). If you are sure you have the decoration size correct, but windows are still being restored in an incorrect position with 'auto_show', you may want to try using this. Takes no argument. (default: false)

       -i,  --is-floating
              Specify a command that will determine whether the current window is floating ($wid can be used in the command instead). Only used for the auto_hide command. This will be used to save whether the current window is floating or not. When restoring the window, if
              there is a float command and the window was previously floating, it will be floated. (default: none)

       -f,  --program-flags
              NOTE: Using this flag is deprecated; it may be removed in the future. Instead, specify program flags after the program (e.g. "tdrop kitty --name foo").

              Specify flags/options that the terminal or program should be called with. For example, to set the title of the terminal, something like 'tdrop -f "--title mytitle" <program>' can be used.

              Caution: If there is a tmux session specified (with -s), the option to execute a program (usually -e for terminal programs) is implicitly added by tdrop! (default: none)

       -a,  --auto-detect-wm
              If there are available settings for the detected window manager for the -l, -L, -d, and/or -i options, automatically set them. Takes no argument. Manually specified settings take precedence. This can be used both for dropdowns and  the  auto_(hide|show)  com‐
              mands. Takes no argument. (default: false)

       -m,  --monitor-aware
              This  option only applies for dropdowns (not auto-hiding and auto-showing). Specify that geometry values should be relative to the current monitor. For example, if the width is a percentage or negative value, the pixel width will be calculated as a percentage
              of the current monitor's width (instead of the combined width of all monitors). If the monitor changes, this option will cause a dropdown to be resized to fit the given percentages. Note that this option assumes xrandr is being used  and  requires  xrandr  to
              work. (default: false)

       -t,  --pointer-monitor-detection
              Use  mouse  pointer location for detecting which monitor is the current one so terminal will be displayed on it. Without this option, the monitor with currently active window is considered the current one. This option is only effective if -m / --monitor-aware
              option is enabled.

       -A,  --activate
              Always activate/show the dropdown if it is not currently focused. Only hide the dropdown if it is currently focused.

       --monitor=NAME
              Specify the monitor to base geometry calculations on when using -m / --monitor-aware instead of detecting the monitor by the actively focused window or mouse pointer.

        --wm=NAME
              Specify the window manager name (which determines the default settings when -a is specified). This may be useful if you've change the name of your window manager using wmname as this will prevent tdrop from correctly detecting the real  window  manager  name.
              This could also potentially be useful if the all the default -a settings for another window manager work with the current one (e.g. if using a similar but differently named fork of some window manager). (default: automatically detected)

        --class=NAME
              Providing  this  option lets tdrop know what the class (or classname) of the window is (it does not actually set the class for a window). This is used for window managers like bspwm that use the class for floating rules. For some commonly used programs, tdrop
              will already use the correct class. This option is useful when the program name and class are not the same and there is not already a default mapping between the two. (default: the program name or a known substitution)

              Both the class and classname of a window can be obtained using xprop (see WM_CLASS). As for the difference, generally the class starts with an uppercase letter and the classname starts with a lowercase letter. The xprop output may only list one for some  pro‐
              grams (e.g. urxvt only has "urxvt"). Currently this option is only useful for bspwm, and it does not matter whether the class or classname (which bspwm calls an instance name) is provided, so the user does not really need to worry about the distinction.

        --name=NAME
              This  option  only  applies  for dropdowns (not auto-hiding and auto-showing). Set a new name for the dropdown window (see _NET_WM_NAME and WM_NAME in xprop output). This option may be useful if you want to add specific rules just for dropdowns with a program
              like compton by giving them a common title. (default: none)

        --clear
              Used to clear a saved window id for the given program or 'current' instead of creating a dropdown. Takes no argument.

        --no-cancel
              Specifies that manually re-showing an auto-hidden window with tdrop should not cancel an auto_show. Takes no argument. See the examples.

        --timeout
              Specifies the timeout in to wait for a window to appear when starting a program before giving up. This prevents a tdrop process from sticking around forever if a program fails to start. (default: 10)

        --debug
              Print information for debugging to stdout and to /tmp/tdrop_<user>/log. Takes no argument. (default: false)

       -r,  --remember
              Store window geometry when hiding and restore geometry when showing instead of using the specified -x, -y, -w, and -h arguments. If used in combination with -m, the x and y positions will be shifted relative to the current monitor when storing/restoring.  For
              example, if you close the dropdown on the leftmost monitor where x is 0 and restore on a monitor to the right, tdrop will offset x so it shows up on the right monitor. This option takes no argument. (default: false)

       -N,  --no-manage
              This is shorthand for -x "", -y "", -w "", -h "" and is incompatible with them (do not set both). When specified, tdrop will not enforce any geometry on the dropdown. This can be useful in combination with --remember if you want to ignore the default geometry
              values and not have tdrop alter the window geometry when first creating the dropdown. Takes no argument. (default: false)

        --help
              Print basic help information. Takes no argument.

EXAMPLES
   Making Dropdowns
       Use a key binding program such as sxhkd to bind keys to these commands.

       The simplest example to make a dropdown for an xterm:
       $ tdrop xterm

       When  using  a  tiling  window manager like bspwm, dropdowns like guake will by default be tiled instead of floated. One can create a rule to float every instance of guake or another dropdown. However, one may not want to float every instance of a terminal used with
       tdrop. Tdrop allows the user to run their own commands at various points during execution, for example before mapping the window:
       $ tdrop -p "bspc rule -a xterm -o floating=on" xterm

       Tdrop also provides tested settings for certain window managers. One can use the '-a' flag if settings exist for the current window manager. For example, if bspwm is the window manager, the following command is the same as the above command and will work  for  what‐
       ever terminal/program is specified and will also work with 'tdrop auto_show'. For a list of window managers with tested settings see the readme or the script itself.
       $ tdrop -a xterm

       Tdrop supports controlling the initial size and placement of a terminal. The border of a window may need to be taken into an account. For example, I use a border size of 2, so I use 4 less than my screen size. I also use a y-offset of 14 so that the dropdown doesn't
       hide my panel:
       $ tdrop -a -w 1362 -y 14 xterm

       Tdrop can also create a tmux session if it does not exist:
       $ tdrop -a -w 1362 -y 14 -s dropdown xterm

       Tdrop allows for having multiple dropdowns of the same type:
       $ tdrop xterm
       $ tdrop -n 1 xterm
       $ tdrop -n 2 xterm

       Tdrop works with normal windows (with some potential visual annoyance, see BUGS):
       $ tdrop zathura
       # the current window
       $ tdrop current

       Once a window is turned into a dropdown, the key bound to 'tdrop ... current' will continue to toggle that window until it is closed. Then the key can be used to create a new dropdown. '-n' can also be used to have multiple 'current' keys. If an active window is ac‐
       cidentally turned into a dropdown, it can be cleared:
       $ tdrop --clear current
       # clear a specific number
       $ tdrop -n 1 --clear current

   Auto-hiding/showing
       These example will work even for non-dropdown terminals.

       Tdrop  provides the functionality to get programs/terminals out of the way when opening other programs. For example, when opening an image viewer from a normal floating dropdown, the dropdown will be over the image viewer. This requires an extra hotkey press to hide
       the dropdown. If one wants to return to the dropdown after looking at images, the hotkey must be once again invoked. Tdrop allows for this process to be automated.

       For example, this could be added to a shell's config/startup file:
       hide_on_open() { tdrop -a auto_hide; "$@" && tdrop -a auto_show }

       To use it in an alias when writing a commit message in an graphical $EDITOR started from a terminal:
       alias gc='hide_on_open git commit'

       This will hide the terminal window when opening the commit editor and then reshow the terminal once the editor is closed. It should also maintain the window's position and size when showing it. If the window moves down and to the right every time it  is  auto-hidden
       and  then shown again, the user may need to specify a -d value. Alternatively, if one already exists for the user's window manager, -a can be used to automatically set it. The -l and -L options are also used with auto_show and can be set automatically with -a if de‐
       fault settings exist for the current window manager.

       Note that for tiling window managers that support 'tdrop -a auto_show', reshowing a window will always float the window (even if it was orignally tiled) if -i is not specified. To prevent this, also use 'tdrop -a auto_hide' if your window manager is supported.  Oth‐
       erwise, -i must be manually specified with auto_hide.

       This functionality might lead to some unwanted "re-shows" of dropdown. Consider a situation in which one opens an image viewer from a dropdown and leaves it open for a while, resuming normal use of the dropdown. When the image viewer is closed, the dropdown appears,
       unwanted. Tdrop is smart about this and won't "re-show" a dropdown if it has been manually toggled since an auto-hide. If you don't want this check to happen, use '--no-cancel' in your dropdown key binding.

       Auto-hiding functionality is particularly nice to use with a file opener like rifle:
       mime ˆimage, has sxiv, X, flag f = tdrop auto_hide ; sxiv -a -- "$@" && tdrop -a auto_show

BUGS
       If -y is set to 0, a window may be subsequently moved to the middle when showing/mapping it with xdotool. This may have to do with the window border.

AUTHOR
       Fox Kiester <noct at posteo.net>
       Source: https://github.com/noctuid/tdrop

SEE ALSO
       xdotool(1), sxhkd(1), xprop(1), xwininfo(1), tmux(1)

tdrop 0.5.0                                                                                                                      11 February 2015                                                                                                                        TDROP(1)
 can I make a hidden window be unhidden when a document is sent to be opened in that window?

**Response:**
Yes, it is possible to use the tdrop command to automatically unhide a hidden window when a document is sent to be opened in that window. Here's an example of how you can achieve this:

1. First, you need to create a shell script that will handle opening the document in the appropriate program and unhide the window.
```bash
#!/bin/bash
# Open document in the desired program
program="your-program-name"
document="$1"
$program "$document"

# Unhide the window
tdrop -a auto_show
```
Save this script, for example, as `open_with_tdrop.sh` and make it executable (`chmod +x open_with_tdrop.sh`).

2. Then, configure your file opener (e.g., xdg-open or mimeopen) to use this script to open documents in your desired program.

For example, you can configure xdg-open by editing the `~/.config/mimeapps.list` file and replacing the default program for the document type with the path to your script:

```plaintext
[Default Applications]
application/pdf=open_with_tdrop.sh %f
image/jpeg=open_with_tdrop.sh %f
```

Make sure to replace `application/pdf` and `image/jpeg` with the appropriate MIME types for your documents.

With this setup, when you open a document of the specified type, it will be opened in your desired program, and the tdrop window will be automatically unhidden.

Note: This approach assumes that you have already set up tdrop to hide and unhide the desired window with the `tdrop` command.

<details><summary>Metadata</summary>

- Duration: 20491 ms
- Datetime: 2023-08-24T08:31:47.765673
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{}
```

