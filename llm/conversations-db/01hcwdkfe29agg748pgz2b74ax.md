**Prompt:**
Edit this manual so it can be quickly scanned by an expert:\nWINDOW COMMANDS
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
                xdotool search --sync --onlyvisible --class "google-chrome" \n *INSTRUCTIONS* BE CONCISE, BUT INCLUDE MUCH. DO INCLUDE EVERY OPTION AND FLAG IN THE MANUAL. DO NOT OMIT ANY DETAILS.

**Response:**
WINDOW COMMANDS

search [options] pattern:
- Searches for windows with titles, names, or classes that match a regular expression pattern.
- Returns a line-delimited list of X window identifiers.
- If used in "COMMAND CHAINING", the search command will only output window ids to stdout if it is the last (or only) command in the chain; otherwise, it will be silent.

Result Saving:
- The result is saved to the window stack for future chained commands. Refer to "WINDOW STACK" and "COMMAND CHAINING" sections for details.

Pattern Syntax:
- Patterns are POSIX extended regular expressions (ERE).
- Examples: "Chrom(e|ium)$" matches windows ending in "Chrome" or "Chromium".
- Case-insensitive matching.

Default Options:
- By default, the options "--name --class --classname --role" are enabled unless you specify one or more of --name, --class, --classname, or --role.

Available Options:
--class
- Matches against the window class.

--classname
- Matches against the window classname.

--role
- Matches against the window role.

--maxdepth N
- Sets recursion/child search depth. Default is infinite (-1).
- 0 means no depth, searching only root windows.
- Set maxdepth of 1 (or 2 depending on your window manager's decorations) to limit the search to top-level windows.

--name
- Matches against the window name, which is displayed in the window titlebar.

--onlyvisible
- Displays only visible windows in the results.
- Includes map state IsViewable.

--pid PID
- Matches windows belonging to a specific process id.
- Note: This may not work for certain X applications that do not set this metadata on their windows.

--screen N
- Selects windows only on a specific screen.
- Default is to search all screens.
- Useful when using multiple displays without Xinerama.

--desktop N
- Matches windows on a certain desktop.
- 'N' is the desktop number.
- Default is to search all desktops.

--limit N
- Stops searching after finding N matching windows.
- Helps speed up the search if you only need a few results.
- Default is no search limit (equivalent to '--limit 0').

--title (DEPRECATED) 
- Same as --name option. Use --name instead.

--all
- Requires that all conditions be met for matching windows.
- Example: "xdotool search --all --pid 1424 --name "Hello World"" matches windows with "Hello World" as the name and owned by pid 1424.

--any (default)
- Matches windows that fulfill any of the given conditions (logically, 'or').
- Example: "xdotool search --any --pid 1424 --name "Hello World"" matches windows owned by pid 1424 or with name "Hello World".

--sync
- Blocks until there are search results.
- Useful when launching an application and waiting for its window to become visible.
- Example:
    google-chrome &
    xdotool search --sync --onlyvisible --class "google-chrome"

*INSTRUCTIONS*
- Be concise but include important details.
- Include every option and flag in the manual.
- Do not omit any details.

<details><summary>Metadata</summary>

- Duration: 75160 ms
- Datetime: 2023-10-16T14:16:40.745821
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"presence_penalty": 2.0}
```

