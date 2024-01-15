**Prompt:**
WINDOW COMMANDS
       search [options] pattern
           Search for windows with titles, names, or classes with a regular expression pattern. The output is line-delimited list of
           X window identifiers. If you are using "COMMAND CHAINING", the search command will only write window ids to stdout if  it
           is the last (or only) command in the chain; otherwise, it is silent.

           The  result  is  saved  to  the  window  stack for future chained commands. See "WINDOW STACK" and "COMMAND CHAINING" for
           details.

           Patterns are POSIX extended regular  expressions  (ERE),  e.  g.  "Chrom(e|ium)$"  for  windows  ending  in  "Chrome"  or
           "Chromium". See regex(7) for syntax details.  Matches are case-insensitive.

           The  default  options  are  "--name  --class  --classname  --role"  (unless  you  specify one or more of --name, --class,
           --classname, or --role).

           The options available are:

           --class
               Match against the window class.

           --classname
               Match against the window classname.

           --role
               Match against the window role.

           --maxdepth N
               Set recursion/child search depth. Default is -1, meaning infinite. 0 means  no  depth,  only  root  windows  will  be
               searched.  If  you  only  want  toplevel  windows, set maxdepth of 1 (or 2, depending on how your window manager does
               decorations).

           --name
               Match against the window name. This is the same string that is displayed in the window titlebar.

           --onlyvisible
               Show only visible windows in the results. This means ones with map state IsViewable.

           --pid PID
               Match windows that belong to a specific process id. This may not work for some X applications that do  not  set  this
               metadata on its windows.

           --screen N
               Select  windows  only  on  a  specific screen. Default is to search all screens. Only meaningful if you have multiple
               displays and are not using Xinerama.

           --desktop N
               Only match windows on a certain desktop. 'N' is a number. The default is to search all desktops.

           --limit N
               Stop searching after finding N matching windows. Specifying a limit will help speed up your search if you only want a
               few results.

               The default is no search limit (which is equivalent to '--limit 0')

           --title
               DEPRECATED. See --name.

           --all
               Require that all conditions be met. For example:

                xdotool search --all --pid 1424 --name "Hello World"

               This will match only windows that have "Hello World" as a name and are owned by pid 1424.

           --any
               Match windows that match any condition (logically, 'or'). This is on by default. For example:

                xdotool search --any --pid 1424 --name "Hello World"

               This will match any windows owned by pid 1424 or windows with name "Hello World"

           --sync
               Block until there are results. This is useful when you are launching an  application  and  want  to  wait  until  the
               application window is visible.  For example:

                google-chrome &
                xdotool search --sync --onlyvisible --class "google-chrome"

       selectwindow
           Get the window id (for a client) by clicking on it. Useful for having scripts query you humans for what window to act on.
           For example, killing a window by clicking on it:

            xdotool selectwindow windowkill

       behave window action command ...
           Bind an action to an event on a window. This lets you run additional xdotool commands whenever a matched event occurs.

           The  command  run  as a result of the behavior is run with %1 being the window that was acted upon. Examples follow after
           the event list.

           The following are valid events:

           mouse-enter
               Fires when the mouse enters a window. This is similar to 'mouse over' events in javascript, if that helps.

           mouse-leave
               Fires when the mouse leaves a window. This is the opposite of 'mouse-enter'

           mouse-click
               Fires when the mouse is clicked. Specifically, when the mouse button is released.

           focus
               Fires when the window gets input focus.

           blur
               Fires when the window loses focus.

           Examples:

            # Print the cursor location whenever the mouse enters a currently-visible
            # window:
            xdotool search --onlyvisible . behave %@ mouse-enter getmouselocation

            # Print the window title and pid whenever an xterm gets focus
            xdotool search --class xterm behave %@ focus getwindowname getwindowpid

            # Emulate focus-follows-mouse
            xdotool search . behave %@ mouse-enter windowfocus

       getwindowpid [window]
           Output the PID owning a given window. This requires effort from the application owning a window and may not work for  all
           windows. This uses _NET_WM_PID property of the window. See "EXTENDED WINDOW MANAGER HINTS" below for more information.

           If no window is given, the default is '%1'. If no windows are on the stack, then this is an error. See "WINDOW STACK" for
           more details.

           Example: Find the PID for all xterms:
            xdotool search --class xterm getwindowpid %@

       getwindowname [window]
           Output  the  name of a given window, also known as the title. This is the text displayed in the window's titlebar by your
           window manager.

           If no window is given, the default is '%1'. If no windows are on the stack, then this is an error. See "WINDOW STACK" for
           more details.

       getwindowgeometry [options] [window]
           Output the geometry (location and position) of a window. The values include: x, y, width, height, and screen number.

           --shell
               Output values suitable for 'eval' in a shell.

       getwindowfocus [-f]
           Prints the window id of the currently focused window. Saves the result to the window stack. See "WINDOW STACK"  for  more
           details.

           If the current window has no WM_CLASS property, we assume it is not a normal top-level window and traverse up the parents
           until we find a window with a WM_CLASS set and return that window id.

           If  you  really  want  the  window  currently  having  focus  and  don't  care  if  it  has  a WM_CLASS setting, then use
           'getwindowfocus -f'

       windowsize [options] [window] width height
           Set the window size of the given window. If no window is given, %1 is the  default.   See  "WINDOW  STACK"  and  "COMMAND
           CHAINING" for more details.

           Percentages  are  valid  for  width  and  height.  They  are relative to the geometry of the screen the window is on. For
           example, to make a window the full width of the screen, but half height:

            xdotool windowsize I<window> 100% 50%

           Percentages are valid with --usehints and still mean pixel-width relative to the screen size.

           The options available are:

           --usehints
               Use window sizing hints (when available) to set width and height.  This is useful on terminals for setting  the  size
               based on row/column of text rather than pixels.

           --sync
               After  sending the window size request, wait until the window is actually resized. If no change is necessary, we will
               not wait. This is useful for scripts that depend on actions being completed before moving on.

               Note: Because many window managers may ignore or alter the original resize request,  we  will  wait  until  the  size
               changes from its original size, not necessary to the requested size.

           Example: To set a terminal to be 80x24 characters, you would use:
            xdotool windowsize --usehints some_windowid 80 24

       windowmove [options] [window] x y
           Move  the  window  to  the  given  position.  If  no  window is given, %1 is the default. See "WINDOW STACK" and "COMMAND
           CHAINING" for more details.

           If the given x coordinate is literally 'x', then the window's current x position will be unchanged. The same applies  for
           'y'.

           Examples:

            xdotool getactivewindow windowmove 100 100    # Moves to 100,100
            xdotool getactivewindow windowmove x 100      # Moves to x,100
            xdotool getactivewindow windowmove 100 y      # Moves to 100,y
            xdotool getactivewindow windowmove 100 y      # Moves to 100,y

           Percentages  are  valid  for  width  and  height.  They  are relative to the geometry of the screen the window is on. For
           example, to make a window the full width of the screen, but half height:

            xdotool windowmove I<window> 100% 50%

           --sync
               After sending the window move request, wait until the window is actually moved. If no movement is necessary, we  will
               not wait. This is useful for scripts that depend on actions being completed before moving on.

           --relative
               Make movement relative to the current window position.

       windowfocus [options] [window]
           Focus a window. If no window is given, %1 is the default. See "WINDOW STACK" and "COMMAND CHAINING" for more details.

           Uses XSetInputFocus which may be ignored by some window managers or programs.

           --sync
               After  sending  the  window focus request, wait until the window is actually focused. This is useful for scripts that
               depend on actions being completed before moving on.

       windowmap [options] [window]
           Map a window. In X11 terminology, mapping a window means making it visible on the screen. If no window is  given,  %1  is
           the default. See "WINDOW STACK" and "COMMAND CHAINING" for more details.

           --sync
               After  requesting the window map, wait until the window is actually mapped (visible). This is useful for scripts that
               depend on actions being completed before moving on.

       windowminimize [options] [window]
           Minimize a window. In X11 terminology, this is called 'iconify.'  If no window is given, %1 is the default.  See  "WINDOW
           STACK" and "COMMAND CHAINING" for more details.

           --sync
               After  requesting  the  window minimize, wait until the window is actually minimized. This is useful for scripts that
               depend on actions being completed before moving on.

       windowraise [window_id=%1]
           Raise the window to the top of the stack. This may not work on all window managers. If no window  is  given,  %1  is  the
           default. See "WINDOW STACK" and "COMMAND CHAINING" for more details.

       windowreparent [source_window] destination_window
           Reparent  a window. This moves the source_window to be a child window of destination_window. If no source is given, %1 is
           the default.  "WINDOW STACK" window references (like %1) are valid for  both  source_window  and  destination_window  See
           "WINDOW STACK" and "COMMAND CHAINING" for more details.

       windowclose [window]
           Close  a window. This action will destroy the window, but will not try to kill the client controlling it. If no window is
           given, %1 is the default. See "WINDOW STACK" and "COMMAND CHAINING" for more details.

       windowquit [window]
           Close a window gracefully. This action sends a request, allowing the application to apply close  confirmation  mechanics.
           If no window is given, %1 is the default. See "WINDOW STACK" and "COMMAND CHAINING" for more details.

       windowkill [window]
           Kill  a  window. This action will destroy the window and kill the client controlling it. If no window is given, %1 is the
           default. See WINDOW STACK and "COMMAND CHAINING" for more details.

       windowunmap [options] [window_id=%1]
           Unmap a window, making it no longer appear on your screen. If no window is given, %1 is the default. See  "WINDOW  STACK"
           and "COMMAND CHAINING" for more details.

           --sync
               After  requesting  the  window unmap, wait until the window is actually unmapped (hidden). This is useful for scripts
               that depend on actions being completed before moving on.

       set_window [options] [windowid=%1]
           Set properties about a window. If no window is given, %1 is the default. See "WINDOW STACK" and  "COMMAND  CHAINING"  for
           more details.

           Options:

           --name newname
               Set window WM_NAME (the window title, usually)

           --icon-name newiconname
               Set window WM_ICON_NAME (the window title when minimized, usually)

           --role newrole
               Set window WM_WINDOW_ROLE

           --classname newclassname
               Set window class name (not to be confused with window class)

           --class newclass
               Set window class (not to be confused with window class name)

           --urgency value
               Set  window  urgency  hint.  If the value is 1, the window will be marked urgent, and the window manager will somehow
               highlight it for the user's attention.  If the value is 0, the window will be marked non-urgent.

           --overrideredirect value
               Set window's override_redirect value. This value is a hint to the window manager for whether  or  not  it  should  be
               managed. If the redirect value is 0, then the window manager will draw borders and treat this window normally. If the
               value is 1, the window manager will ignore this window.

               If  you change this value, your window manager may not notice the change until the window is mapped again, so you may
               want to issue 'windowunmap' and 'windowmap' to make the window manager take note.

**Response:**
WINDOW COMMANDS

search [options] pattern - Search for windows with titles, names, or classes using a regular expression pattern.

selectwindow - Get the window id by clicking on it.

behave window action command - Bind an action to an event on a window.

getwindowpid [window] - Output the PID owning a given window.

getwindowname [window] - Output the name of a given window.

getwindowgeometry [options] [window] - Output the geometry (location and position) of a window.

getwindowfocus [-f] - Prints the window id of the currently focused window.

windowsize [options] [window] width height - Set the window size of the given window.

windowmove [options] [window] x y - Move the window to the given position.

windowfocus [options] [window] - Focus a window.

windowmap [options] [window] - Map a window.

windowminimize [options] [window] - Minimize a window.

windowraise [window_id=%1] - Raise the window to the top of the stack.

windowreparent [source_window] destination_window - Reparent a window.

windowclose [window] - Close a window.

windowquit [window] - Close a window gracefully.

windowkill [window] - Kill a window.

windowunmap [options] [window_id=%1] - Unmap a window.

set_window [options] [windowid=%1] - Set properties about a window.

<details><summary>Metadata</summary>

- Duration: 33017 ms
- Datetime: 2023-10-16T13:52:03.488154
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

