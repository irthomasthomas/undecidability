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

**Response:**
WINDOW COMMANDS
       search [options] pattern
           Search windows with titles, names, or classes using a regular expression pattern. Output is a list of window identifiers. Use "COMMAND CHAINING" to save results to the window stack. Options include:
           --class: match against window class
           --classname: match against window classname
           --role: match against window role
           --maxdepth N: set recursion/child search depth
           --name: match against window name
           --onlyvisible: show only visible windows
           --pid PID: match windows belonging to a specific process id
           --screen N: select windows only on a specific screen
           --desktop N: only match windows on a certain desktop
           --limit N: stop searching after finding N matching windows
           --title: DEPRECATED. See --name.
           --all: require all conditions to be met
           --any: match windows that match any condition
           --sync: block until there are results.

<details><summary>Metadata</summary>

- Duration: 21332 ms
- Datetime: 2023-10-16T13:59:13.578960
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.4}
```

**Prompt:**
reorder them like so: Match against:\n--class\n--classname\n--name etc etc

**Response:**
WINDOW COMMANDS
       search [options] pattern
           Search windows with titles, names, or classes using a regular expression pattern. Output is a list of window identifiers. Use "COMMAND CHAINING" to save results to the window stack. Options include:
           - Match against:
               --class: match against window class
               --classname: match against window classname
               --name: match against window name
               --role: match against window role
             other options...

<details><summary>Metadata</summary>

- Duration: 12306 ms
- Datetime: 2023-10-16T14:01:26.241239
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

