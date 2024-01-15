**Prompt:**
Here is a BASH script that accepts a file. Each line contains a query string. For each query_string, grep it against stdin, and print the matches.

#!/bin/bash

**Response:**

file=$1
while read -r query_string 
do
    echo "$query_string" | ./config-server &
done < $file

Please generate code completing the task which will replace the below region.


https://www.codewars.com/kata/run-a-bash-script-to-accept-a-file-and-search-each-line-in-stdin-for-a-given-query-string

This kata is a variation of the previous "Run a Bash script to accept a file" kata. In this new task, you will write a BASH script that accepts a file as input and performs a grep operation on each line in stdin against a query string provided by the user. The output should be printed out for each match found.

Example:

If the content of config-server is:
```
openai key
openai development server
config-server
```
And you run your script with the file as input, passing it to the query string "key" like so `./config-server key`
The output should be:
```
openai key
```
If the content of config-server is:
```
openai key
openai development server
config-server 1234567890
```
And you run your script with the file as input, passing it to the query string "key" like so `./config-server key`
The output should be empty since there are no exact matches for "key". If instead, you pass in a query of "1234567890" like so `./config-server 1234567890`, the script will return:
```
config-server 1234567890

<details><summary>Metadata</summary>

- Duration: 39443 ms
- Datetime: 2023-11-02T21:10:25.951647
- Model: Unknown

</details>

**Options:**
```json
{}
```

