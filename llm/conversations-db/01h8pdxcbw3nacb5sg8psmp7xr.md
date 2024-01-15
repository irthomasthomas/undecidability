**Prompt:**
APROPOS(1)                                                                                              Manual pager utils                                                                                              APROPOS(1)

NAME
       apropos - search the manual page names and descriptions

SYNOPSIS
       apropos [-dalv?V] [-e|-w|-r] [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] keyword ...

DESCRIPTION
       Each manual page has a short description available within it.  apropos searches the descriptions for instances of keyword.

       keyword  is  usually  a  regular  expression, as if (-r) was used, or may contain wildcards (-w), or match the exact keyword (-e).  Using these options, it may be necessary to quote the keyword or escape (\) the special
       characters to stop the shell from interpreting them.

       The standard matching rules allow matches to be made against the page name and word boundaries in the description.

       The database searched by apropos is updated by the mandb program.  Depending on your installation, this may be run by a periodic cron job, or may need to be run manually after new manual pages have been installed.

OPTIONS
       -d, --debug
              Print debugging information.

       -v, --verbose
              Print verbose warning messages.

       -r, --regex
              Interpret each keyword as a regular expression.  This is the default behaviour.  Each keyword will be matched against the page names and the descriptions independently.  It can match  any  part  of  either.   The
              match is not limited to word boundaries.

       -w, --wildcard
              Interpret  each keyword as a pattern containing shell style wildcards.  Each keyword will be matched against the page names and the descriptions independently.  If --exact is also used, a match will only be found
              if an expanded keyword matches an entire description or page name.  Otherwise the keyword is also allowed to match on word boundaries in the description.

       -e, --exact
              Each keyword will be exactly matched against the page names and the descriptions.

       -a, --and
              Only display items that match all the supplied keywords.  The default is to display items that match any keyword.

       -l, --long
              Do not trim output to the terminal width.  Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written NAME sections.

       -s list, --sections=list, --section=list
              Search only the given manual sections.  list is a colon- or comma-separated list of sections.  If an entry in list is a simple section, for example "3", then the displayed list of descriptions will include  pages
              in sections "3", "3perl", "3x", and so on; while if an entry in list has an extension, for example "3perl", then the list will only include pages in that exact part of the manual section.

       -m system[,...], --systems=system[,...]
              If this system has access to other operating systems' manual page descriptions, they can be searched using this option.  To search NewOS's manual page descriptions, use the option -m NewOS.

              The  system specified can be a combination of comma-delimited operating system names.  To include a search of the native operating system's whatis descriptions, include the system name man in the argument string.
              This option will override the $SYSTEM environment variable.

       -M path, --manpath=path
              Specify an alternate set of colon-delimited manual page hierarchies to search.  By default, apropos uses the $MANPATH environment variable, unless it is empty or unset, in which case it will determine  an  appro‐
              priate manpath based on your $PATH environment variable.  This option overrides the contents of $MANPATH.

       -L locale, --locale=locale
              apropos  will  normally determine your current locale by a call to the C function setlocale(3) which interrogates various environment variables, possibly including $LC_MESSAGES and $LANG.  To temporarily override
              the determined value, use this option to supply a locale string directly to apropos.  Note that it will not take effect until the search for pages actually begins.  Output such as the help message will always  be
              displayed in the initially determined locale.

       -C file, --config-file=file
              Use this user configuration file rather than the default of ~/.manpath.

       -?, --help
              Print a help message and exit.

       --usage
              Print a short usage message and exit.

       -V, --version
              Display version information.

EXIT STATUS
       0      Successful program execution.

       1      Usage, syntax or configuration file error.

       2      Operational error.

       16     Nothing was found that matched the criteria specified.

ENVIRONMENT
       SYSTEM If $SYSTEM is set, it will have the same effect as if it had been specified as the argument to the -m option.

       MANPATH
              If $MANPATH is set, its value is interpreted as the colon-delimited manual page hierarchy search path to use.

              See the SEARCH PATH section of manpath(5) for the default behaviour and details of how this environment variable is handled.

       MANWIDTH
              If  $MANWIDTH  is  set, its value is used as the terminal width (see the --long option).  If it is not set, the terminal width will be calculated using the value of $COLUMNS, and ioctl(2) if available, or falling
              back to 80 characters if all else fails.

       POSIXLY_CORRECT
              If $POSIXLY_CORRECT is set, even to a null value, the default apropos search will be as an extended regex (-r).  Nowadays, this is the default behaviour anyway.

FILES
       /usr/share/man/index.(bt|db|dir|pag)
              A traditional global index database cache.

       /var/cache/man/index.(bt|db|dir|pag)
              An FHS compliant global index database cache.

       /usr/share/man/.../whatis
              A traditional whatis text database.

SEE ALSO
       man(1), whatis(1), mandb(8)

AUTHOR
       Wilf. (G.Wilford@ee.surrey.ac.uk).
       Fabrizio Polacco (fpolacco@debian.org).
       Colin Watson (cjwatson@debian.org).

BUGS
       https://gitlab.com/man-db/man-db/-/issues
       https://savannah.nongnu.org/bugs/?group=man-db

2.11.2                                                                                                      2023-01-08                                                                                                  APROPOS(1)
 find man pages from github.

**Response:**
Apropos is a command-line tool that allows users to search for manual pages based on keywords. It searches for instances of keywords in the names and descriptions of the manual pages.

The tool supports various options to refine the search, such as interpreting keywords as regular expressions, patterns with shell-style wildcards, or exact matches. Users can also specify the manual sections to search, alternate systems to include, and alternate man page hierarchies to search.

The matching rules allow matches to be made against both the page name and word boundaries in the description. The tool can display verbose warning messages and provide debugging information if needed.

The database searched by apropos is updated by the mandb program. Users may need to run mandb manually after installing new manual pages or rely on a periodic cron job for updating the database.

Some important options of apropos are:

- `-d, --debug`: Print debugging information.
- `-v, --verbose`: Print verbose warning messages.
- `-r, --regex`: Interpret each keyword as a regular expression (default behavior).
- `-w, --wildcard`: Interpret each keyword as a pattern containing shell-style wildcards.
- `-e, --exact`: Match the keywords exactly against the page names and descriptions.
- `-a, --and`: Only display items that match all the supplied keywords (default is to display items that match any keyword).
- `-l, --long`: Do not trim output to the terminal width.
- `-s list, --sections=list, --section=list`: Search only the given manual sections.
- `-m system[,...], --systems=system[,...]`: Search other operating systems' manual page descriptions.
- `-M path, --manpath=path`: Specify an alternate set of manual page hierarchies to search.
- `-L locale, --locale=locale`: Override the determined locale with the supplied string.
- `-C file, --config-file=file`: Use a user configuration file instead of the default.
- `-?, --help`: Print a help message and exit.
- `--usage`: Print a short usage message and exit.
- `-V, --version`: Display version information.

The exit status of the apropos command can indicate success, usage/syntax/configuration error, operational error, or no matches found.

The environment variables that affect the behavior of apropos include SYSTEM, MANPATH, MANWIDTH, and POSIXLY_CORRECT.

Some related commands and tools to apropos are man, whatis, and mandb.

The apropos tool is maintained by the man-db project. Bugs and issues can be reported on the project's GitLab or Savannah bug trackers.

The version of apropos mentioned in this manual is 2.11.2, and the manual page was last updated on January 8, 2023.

If you want to find man pages from GitHub, you can use the GitHub search functionality or explore man page repositories hosted on GitHub.

<details><summary>Metadata</summary>

- Duration: 22330 ms
- Datetime: 2023-08-25T13:24:44.225306
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

