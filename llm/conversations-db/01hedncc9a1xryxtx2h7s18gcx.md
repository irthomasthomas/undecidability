**Prompt:**
"\n          gh formatting\n\nBy default, the result of gh commands are output in line-based plain text format.\nSome commands support passing the --json flag, which converts the output to JSON format.\nOnce in JSON, the output can be further formatted according to a required formatting string by\nadding either the --jq or --template flag. This is useful for selecting a subset of data,\ncreating new data structures, displaying the data in a different format, or as input to another\ncommand line script.\n\nThe --json flag requires a comma separated list of fields to fetch. To view the possible JSON\nfield names for a command omit the string argument to the --json flag when you run the command.\nNote that you must pass the --json flag and field names to use the --jq or --template flags.\n\nThe --jq flag requires a string argument in jq query syntax, and will only print\nthose JSON values which match the query. jq queries can be used to select elements from an\narray, fields from an object, create a new array, and more. The jq utility does not need\nto be installed on the system to use this formatting directive. When connected to a terminal,\nthe output is automatically pretty-printed. To learn about jq query syntax, see:\nhttps://stedolan.github.io/jq/manual/v1.6/\n\nThe --template flag requires a string argument in Go template syntax, and will only print\nthose JSON values which match the query.\nIn addition to the Go template functions in the standard library, the following functions can be used\nwith this formatting directive:\n\n  autocolor: like color, but only emits color to terminals\n  color <style> <input>: colorize input using https://github.com/mgutz/ansi\n  join <sep> <list>: joins values in the list using a separator\n  pluck <field> <list>: collects values of a field from all items in the input\n  tablerow <fields>...: aligns fields in output vertically as a table\n  tablerender: renders fields added by tablerow in place\n  timeago <time>: renders a timestamp as relative to now\n  timefmt <format> <time>: formats a timestamp using Go's Time.Format function\n  truncate <length> <input>: ensures input fits within length\n  hyperlink <url> <text>: renders a terminal hyperlink\n\n\nTo learn more about Go templates, see: https://golang.org/pkg/text/template/.\n\nExamples\n\n# default output format\n$ gh pr list\nShowing 23 of 23 open pull requests in cli/cli\n\n#123  A helpful contribution          contribution-branch              about 1 day ago\n#124  Improve the docs                docs-branch                      about 2 days ago\n#125  An exciting new feature         feature-branch                   about 2 days ago\n\n\n# adding the --json flag with a list of field names\n$ gh pr list --json number,title,author\n[\n  {\n\t\"author\": {\n\t  \"login\": \"monalisa\"\n\t},\n\t\"number\": 123,\n\t\"title\": \"A helpful contribution\"\n  },\n  {\n\t\"author\": {\n\t  \"login\": \"codercat\"\n\t},\n\t\"number\": 124,\n\t\"title\": \"Improve the docs\"\n  },\n  {\n\t\"author\": {\n\t  \"login\": \"cli-maintainer\"\n\t},\n\t\"number\": 125,\n\t\"title\": \"An exciting new feature\"\n  }\n]\n\n\n# adding the --jq flag and selecting fields from the array\n$ gh pr list --json author --jq '.[].author.login'\nmonalisa\ncodercat\ncli-maintainer\n\n# --jq can be used to implement more complex filtering and output changes:\n$ bin/gh issue list --json number,title,labels --jq \\\n  'map(select((.labels | length) > 0))    # must have labels\n  | map(.labels = (.labels | map(.name))) # show only the label names\n  | .[:3]                                 # select the first 3 results'\n  [\n\t{\n\t  \"labels\": [\n\t\t\"enhancement\",\n\t\t\"needs triage\"\n\t  ],\n\t  \"number\": 123,\n\t  \"title\": \"A helpful contribution\"\n\t},\n\t{\n\t  \"labels\": [\n\t\t\"help wanted\",\n\t\t\"docs\",\n\t\t\"good first issue\"\n\t  ],\n\t  \"number\": 125,\n\t  \"title\": \"Improve the docs\"\n\t},\n\t{\n\t  \"labels\": [\n\t\t\"enhancement\",\n\t  ],\n\t  \"number\": 7221,\n\t  \"title\": \"An exciting new feature\"\n\t}\n  ]\n  \n# using the --template flag with the hyperlink helper\ngh issue list --json title,url --template '{{range .}}{{hyperlink .url .title}}{{\"\\n\"}}{{end}}'\n\n\n# adding the --template flag and modifying the display format\n$ gh pr list --json number,title,headRefName,updatedAt --template \\\n\t'{{range .}}{{tablerow (printf \"#%v\" .number | autocolor \"green\") .title .headRefName (timeago .updatedAt)}}{{end}}'\n\n#123  A helpful contribution      contribution-branch       about 1 day ago\n#124  Improve the docs            docs-branch               about 2 days ago\n#125  An exciting new feature     feature-branch            about 2 days ago\n\n\n# a more complex example with the --template flag which formats a pull request using multiple tables with headers:\n$ gh pr view 3519 --json number,title,body,reviews,assignees --template \\\n'{{printf \"#%v\" .number}} {{.title}}\n\n{{.body}}\n\n{{tablerow \"ASSIGNEE\" \"NAME\"}}{{range .assignees}}{{tablerow .login .name}}{{end}}{{tablerender}}\n{{tablerow \"REVIEWER\" \"STATE\" \"COMMENT\"}}{{range .reviews}}{{tablerow .author.login .state .body}}{{end}}\n'\n\n#3519 Add table and helper template functions\n\nResolves #3488\n\nASSIGNEE  NAME\nmislav    Mislav Marohni\u0107\n\n\nREVIEWER  STATE              COMMENT\nmislav    COMMENTED          This is going along great! Thanks for working on this \u2764\ufe0f\n\nSee also\n\n\n  gh\n\n\n          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n        "
 Reduce the number of words by a third, and format with github markdown 


**Response:**
"gh formatting

By default, the result of gh commands are output in line-based plain text format. Some commands support passing the --json flag, which converts the output to JSON format. Once in JSON, the output can be further formatted according to a required formatting string by adding either the --jq or --template flag. This is useful for selecting a subset of data, creating new data structures, displaying the data in a different format, or as input to another command line script.

The --json flag requires a comma separated list of fields to fetch. To view the possible JSON field names for a command omit the string argument to the --json flag when you run the command. Note that you must pass the --json flag and field names to use the --jq or --template flags.

The --jq flag requires a string argument in jq query syntax, and will only print those JSON values which match the query. jq queries can be used to select elements from an array, fields from an object, create a new array, and more. The jq utility does not need to be installed on the system to use this formatting directive. When connected to a terminal, the output is automatically pretty-printed. To learn about jq query syntax, see: https://stedolan.github.io/jq/manual/v1.6/

The --template flag requires a string argument in Go template syntax, and will only print those JSON values which match the query. In addition to the Go template functions in the standard library, the following functions can be used with this formatting directive:

- autocolor: like color, but only emits color to terminals
- color <style> <input>: colorize input using https://github.com/mgutz/ansi
- join <sep> <list>: joins values in the list using a separator
- pluck <field> <list>: collects values of a field from all items in the input
- tablerow <fields>...: aligns fields in output vertically as a table
- tablerender: renders fields added by tablerow in place
- timeago <time>: renders a timestamp as relative to now
- timefmt <format> <time>: formats a timestamp using Go's Time.Format function
- truncate <length> <input>: ensures input fits within length
- hyperlink <url> <text>: renders a terminal hyperlink

To learn more about Go templates, see: https://golang.org/pkg/text/template/.

Examples

# default output format
$ gh pr list
Showing 23 of 23 open pull requests in cli/cli

#123 A helpful contribution contribution-branch about 1 day ago
#124 Improve the docs docs-branch about 2 days ago
#125 An exciting new feature feature-branch about 2 days ago

# adding the --json flag with a list of field names
$ gh pr list --json number,title,author
[
  {
    "author": {
      "login": "monalisa"
    },
    "number": 123,
    "title": "A helpful contribution"
  },
  {
    "author": {
      "login": "codercat"
    },
    "number": 124,
    "title": "Improve the docs"
  },
  {
    "author": {
      "login": "cli-maintainer"
    },
    "number": 125,
    "title": "An exciting new feature"
  }
]

# adding the --jq flag and selecting fields from the array
$ gh pr list --json author --jq '.[].author.login'
monalisa
codercat
cli-maintainer

# --jq can be used to implement more complex filtering and output changes:
$ bin/gh issue list --json number,title,labels --jq \
  'map(select((.labels | length) > 0))    # must have labels
  | map(.labels = (.labels | map(.name))) # show only the label names
  | .[:3]                                 # select the first 3 results'
  [
    {
      "labels": [
        "enhancement",
        "needs triage"
      ],
      "number": 123,
      "title": "A helpful contribution"
    },
    {
      "labels": [
        "help wanted",
        "docs",
        "good first issue"
      ],
      "number": 125,
      "title": "Improve the docs"
    },
    {
      "labels": [
        "enhancement",
      ],
      "number": 7221,
      "title": "An exciting new feature"
    }
  ]

# using the --template flag with the hyperlink helper
gh issue list --json title,url --template '{{range .}}{{hyperlink .url .title}}{{"\n"}}{{end}}'

# adding the --template flag and modifying the display format
$ gh pr list --json number,title,headRefName,updatedAt --template \
  '{{range .}}{{tablerow (printf "#%v" .number | autocolor "green") .title .headRefName (timeago .updatedAt)}}{{end}}'

#123 A helpful contribution contribution-branch about 1 day ago
#124 Improve the docs docs-branch about 2 days ago
#125 An exciting new feature feature-branch about 2 days ago

# a more complex example with the --template flag which formats a pull request using multiple tables with headers:
$ gh pr view 3519 --json number,title,body,reviews,assignees --template \
'{{printf "#%v" .number}} {{.title}}

{{.body}}

{{tablerow "ASSIGNEE" "NAME"}}{{range .assignees}}{{tablerow .login .name}}{{end}}{{tablerender}}
{{tablerow "REVIEWER" "STATE" "COMMENT"}}{{range .reviews}}{{tablerow .author.login .state .body}}{{end}}
'

#3519 Add table and helper template functions

Resolves #3488

ASSIGNEE NAME
mislav Mislav Marohni\u0107

REVIEWER STATE COMMENT
mislav COMMENTED This is going along great! Thanks for working on this \u2764\ufe0f

See also

gh"

<details><summary>Metadata</summary>

- Duration: 130300 ms
- Datetime: 2023-11-04T17:14:28.782298
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.5}
```

