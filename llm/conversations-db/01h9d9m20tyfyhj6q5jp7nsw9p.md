**Prompt:**
In KDE Plasma 5 running on manjaro (Arch) linux, how do I list the xdg
file tags, like dolphin uses? In the terminal. \n\n echo balooctl --help\n\nUsage: balooctl [options] command status enable disable purge suspend resume check index clear config monitor indexSize failed

Options:
  -f, --format <format>  Output format <multiline|json|simple>.
                         The default format is "multiline".
                         Only applies to "balooctl status <file>"
  -v, --version          Displays version information.
  -h, --help             Displays help on commandline options.
  --help-all             Displays help including Qt specific options.

Arguments:
  command                The command to execute
  status                 Print the status of the indexer
  enable                 Enable the file indexer
  disable                Disable the file indexer
  purge                  Remove the index database
  suspend                Suspend the file indexer
  resume                 Resume the file indexer
  check                  Check for any unindexed files and index them
  index                  Index the specified files
  clear                  Forget the specified files
  config                 Modify the Baloo configuration
  monitor                Monitor the file indexer
  indexSize              Display the disk space used by index
  failed                 Display files which could not be indexed

**Response:**
To list the XDG file tags in KDE Plasma 5 running on Manjaro (Arch) Linux using the terminal, you can use the following command:

```
balooctl config
```

This command will display the Baloo configuration, including the XDG file tags.

<details><summary>Metadata</summary>

- Duration: 2677 ms
- Datetime: 2023-09-03T10:32:36.004657
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

