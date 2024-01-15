**Prompt:**
ELINKS(1)                                                                                             The Elinks text-browser                                                                                            ELINKS(1)

NAME
       elinks - lynx-like alternative character mode WWW browser

SYNOPSIS
       elinks [OPTION]... [URL]...

DESCRIPTION
       ELinks is a text mode WWW browser, supporting colors, table rendering, background downloading, menu driven configuration interface, tabbed browsing and slim code.

       Frames are supported. You can have different file formats associated with external viewers. mailto: and telnet: are supported via external clients.

       ELinks can handle both local files and remote URLs. The main supported remote URL protocols are HTTP, HTTPS (with SSL support compiled in) and FTP. Additional protocol support exists for BitTorrent finger, Gopher, SMB
       and NNTP.

       The homepage of ELinks can be found at <http://elinks.cz/>, where the ELinks manual is also hosted.

OPTIONS
       Most options can be set in the user interface or config file, so usually you do not need to care about them. Note that this list is roughly equivalent to the output of running ELinks with the option --long-help.

       -anonymous [0|1] (default: 0)
           Restricts ELinks so it can run on an anonymous account. Local file browsing, downloads, and modification of options will be disabled. Execution of viewers is allowed, but entries in the association table can't be
           added or modified.

       -auto-submit [0|1] (default: 0)
           Automatically submit the first form in the given URLs.

       -base-session <num> (default: 0)
           Used internally when opening ELinks instances in new windows. The ID maps to information that will be used when creating the new instance. You don't want to use it.

       -config-dir <str> (default: "")
           Path of the directory ELinks will read and write its config and runtime state files to instead of ~/.elinks. If the path does not begin with a '/' it is assumed to be relative to your HOME directory.

       -config-dump
           Print a configuration file with options set to the built-in defaults to stdout.

       -config-file <str> (default: "elinks.conf")
           Name of the configuration file that all configuration options will be read from and written to. It should be relative to config-dir.

       -config-help
           Print help for configuration options and exit.

       -default-mime-type (alias for mime.default_type)
           The default MIME type used for documents of unknown type.

       -default-keys [0|1] (default: 0)
           When set, all keybindings from configuration files will be ignored. It forces use of default keybindings and will reset user-defined ones on save.

       -dump [0|1] (default: 0)
           Print formatted plain-text versions of given URLs to stdout.

       -dump-charset (alias for document.dump.codepage)
           Codepage used when formatting dump output.

       -dump-color-mode (alias for document.dump.color_mode)
           Color mode used with -dump.

       -dump-width (alias for document.dump.width)
           Width of the dump output.

       -eval
           Specify configuration file directives on the command-line which will be evaluated after all configuration files has been read. Example usage: -eval 'set protocol.file.allow_special_files = 1'

       -force-html
           Makes ELinks assume documents of unknown types are HTML. Useful when using ELinks as an external viewer from MUAs. This is equivalent to -default-mime-type text/html.

       -?, -h, -help
           Print usage help and exit.

       -localhost [0|1] (default: 0)
           Restricts ELinks to work offline and only connect to servers with local addresses (ie. 127.0.0.1). No connections to remote servers will be permitted.

       -long-help
           Print detailed usage help and exit.

       -lookup
           Look up specified host and print all DNS resolved IP addresses.

       -no-connect [0|1] (default: 0)
           Run ELinks as a separate instance instead of connecting to an existing instance. Note that normally no runtime state files (bookmarks, history, etc.) are written to the disk when this option is used. See also
           -touch-files.

       -no-home [0|1] (default: 0)
           Disables creation and use of files in the user specific home configuration directory (~/.elinks). It forces default configuration values to be used and disables saving of runtime state files.

       -no-numbering (alias for document.dump.numbering)
           Prevents printing of link number in dump output.

           Note that this really affects only -dump, nothing else.

       -no-references (alias for document.dump.references)
           Prevents printing of references (URIs) of document links in dump output.

           Note that this really affects only -dump, nothing else.

       -remote
           Control a remote ELinks instance by passing commands to it. The option takes an additional argument containing the method which should be invoked and any parameters that should be passed to it. For ease of use, the
           additional method argument can be omitted in which case any URL arguments will be opened in new tabs in the remote instance.

           Following is a list of the supported methods:

           •   ping(): look for a remote instance

           •   openURL(): prompt URL in current tab

           •   openURL(URL): open URL in current tab

           •   openURL(URL, new-tab): open URL in new tab

           •   openURL(URL, new-window): open URL in new window

           •   addBookmark(URL): bookmark URL

           •   infoBox(text): show text in a message box

           •   reload(): reload the document in the current tab

           •   search(string): search in the current tab

           •   xfeDoCommand(openBrowser): open new window

       -session-ring <num> (default: 0)
           ID of session ring this ELinks session should connect to.  ELinks works in so-called session rings, whereby all instances of ELinks are interconnected and share state (cache, bookmarks, cookies, and so on). By
           default, all ELinks instances connect to session ring 0. You can change that behaviour with this switch and form as many session rings as you want. Obviously, if the session-ring with this number doesn't exist yet,
           it's created and this ELinks instance will become the master instance (that usually doesn't matter for you as a user much).

           Note that you usually don't want to use this unless you're a developer and you want to do some testing - if you want the ELinks instances each running standalone, rather use the -no-connect command-line option. Also
           note that normally no runtime state files are written to the disk when this option is used. See also -touch-files.

       -source [0|1] (default: 0)
           Print given URLs in source form to stdout.

       -touch-files [0|1] (default: 0)
           When enabled, runtime state files (bookmarks, history, etc.) are written to disk, even when -no-connect or -session-ring is used. The option has no effect if not used in conjunction with any of these options.

       -verbose <num> (default: 1)
           The verbose level controls what messages are shown at start up and while running:

           •   0 means only show serious errors

           •   1 means show serious errors and warnings

           •   2 means show all messages

       -version
           Print ELinks version information and exit.
       Generated using output from ELinks version 0.13.GIT.

ENVIRONMENT VARIABLES
       COMSPEC, SHELL
           The shell used for File -> OS Shell on DOS/Windows and UNIX, respectively.

       EDITOR
           The program to use for external editor (when editing textareas).

       ELINKS_CONFDIR
           The location of the directory containing configuration files. If not set the default is ~/.elinks/.

       ELINKS_TWTERM, LINKS_TWTERM
           The command to run when selecting File -> New window and if TWDISPLAY is defined (default twterm -e).

       ELINKS_XTERM, LINKS_XTERM
           The command to run when selecting File -> New window and if DISPLAY is defined (default xterm -e).

       FTP_PROXY, HTTP_PROXY, HTTPS_PROXY
           The host to proxy the various protocol traffic through.

       NO_PROXY
           A comma separated list of URLs which should not be proxied.

       HOME
           The path to the users home directory. Used when expanding ~/.

       HOME_ETC
           If set the location of the directory containing configuration files is $HOME_ETC/.elinks/ instead of ~/.elinks/.

       WWW_HOME
           Homepage location (as in lynx(1)).

FILES
       Configuration files controlled by ELinks are located in the user configuration directory, defaulting to ~/.elinks/. In addition to the files listed below, a user defined CSS stylesheet can be defined using the
       document.css.stylesheet option.

       /etc/elinks.conf
           Site-wide configuration file.

       ~/.elinks/elinks.conf
           Per-user config file, loaded after site-wide configuration.

       ~/.elinks/bookmarks
           Bookmarks file.

       ~/.elinks/cookies
           Cookies file.

       ~/.elinks/exmodehist
           Exmode history file.

       ~/.elinks/formhist
           Form history file.

       ~/.elinks/globhist
           History file containing most recently visited URLs.

       ~/.elinks/gotohist
           GoTo URL dialog history file.

       ~/.elinks/hooks.{js,lua,pl,py,rb,scm}
           Browser scripting hooks.

       ~/.elinks/searchhist
           Search history file.

       ~/.elinks/socket
           Internal ELinks socket for communication between its instances.

       ~/.mailcap, /etc/mailcap
           Mappings of MIME types to external handlers.

       ~/.mime.types, /etc/mime.types
           Mappings of file extensions to MIME types.

BUGS
       Please report any other bugs you find to the either the ELinks mailing list at <elinks-users@linuxfromscratch.org> or if you prefer enter them into the bug tracking system <http://bugzilla.elinks.cz/>. More information
       about how to get in contact with developers and getting help can be found on the community page <http://elinks.cz/community.html>.

LICENSE
       ELinks is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License <http://www.gnu.org/copyleft/gpl.html> as published by the Free Software Foundation; version 2 of the
       License.

AUTHORS
       The Links browser - on which ELinks is based - was written by Mikulas Patocka <mikulas@artax.karlin.mff.cuni.cz>. ELinks was written by Petr Baudis <pasky@ucw.cz>. See file AUTHORS in the source tree for a list of
       people contributing to this project.

       This manual page was written by Peter Gervai <grin@tolna.net>, using excerpts from a (yet?) unknown Links fan for the Debian GNU/Linux system (but may be used by others). Contributions from Francis A. Holop. Extended,
       clarified and made more up-to-date by Petr Baudis <pasky@ucw.cz>. Updated by Zas <zas@norz.org>. The conversion to Asciidoc and trimming was done by Jonas Fonseca <fonseca@diku.dk>.

SEE ALSO
       elinkskeys(5), elinks.conf(5), links(1), lynx(1), w3m(1), wget(1)

ELinks 0.13.GIT                                                                                             07/11/2009                                                                                                   ELINKS(1)
 options for recording browsing history

**Response:**
ELinks has several options for recording browsing history. These options can be controlled through the configuration file elinks.conf or through the user interface.

1. History File: By default, ELinks stores the most recently visited URLs in the file ~/.elinks/globhist. This file can be customized using the "global-history-file" option in the configuration file.

2. History Length: ELinks allows you to set the maximum number of URLs to be stored in the history file. This can be done using the "global-history-size" option in the configuration file.

3. Saving History: By default, ELinks saves the history file automatically when the browser is closed. This behavior can be controlled using the "autosave-history" option in the configuration file.

4. Clearing History: ELinks provides the option to clear the browsing history. This can be done through the user interface by selecting "File" -> "Clear History" or by using the hotkey "Ctrl + Shift + H".

5. Visit History: ELinks keeps track of the order in which URLs are visited. This visit history can be accessed through the user interface by selecting "Go" -> "Visit History" or by using the hotkey "Ctrl + H".

6. Bookmark History: ELinks allows you to bookmark URLs for quick access. These bookmarks are stored in the file ~/.elinks/bookmarks. They can be managed through the user interface by selecting "Bookmarks" -> "Manage Bookmarks" or by using the hotkey "Ctrl + B".

7. Form History: ELinks stores the history of form input for web pages. This can be helpful when filling out forms on websites. The form history is stored in the file ~/.elinks/formhist.

These options provide control over the recording and management of browsing history in ELinks. By customizing these options, users can tailor the browsing experience to their needs.

<details><summary>Metadata</summary>

- Duration: 23522 ms
- Datetime: 2023-08-25T13:13:47.716014
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{}
```

