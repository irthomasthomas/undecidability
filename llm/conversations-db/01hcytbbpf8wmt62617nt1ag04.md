**Prompt:**
TRUNCATE THE TEXT AS MUCH AS POSSIBLE. YOUR TARGET AUDIENCE IS AN IMPATIENT EXPERT. E.G Match against\n --name window name\n --role: window role\n --name: window name\n 
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

**Response:**
WINDOW COMMANDS: search [options] pattern

Search for windows with titles, names, or classes using a regular expression pattern. Output is a list of window identifiers. Use "--name", "--class", "--classname", or "--role" to specify which properties to search against.

Options:
- --maxdepth N: Set recursion/child search depth (default: -1)
- --onlyvisible: Only show visible windows
- --pid PID : Match windows belonging to a specific process ID
- --screen N : Select only on a specific screen (default: all screens)


<details><summary>Metadata</summary>

- Duration: 14485 ms
- Datetime: 2023-10-17T12:38:55.801962
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"frequency_penalty": 2.0, "presence_penalty": 1.0}
```

