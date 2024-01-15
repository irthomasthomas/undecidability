**Prompt:**
Top 10 jq formatting examples

**Response:**
1. Basic Selection: Use `[]` to select all elements of an array.
```
jq '[]'
```

2. Simple Value Extraction: Extract values from a specific key in the JSON object.
```
jq '.key'
```

3. Conditional Filtering: Filter objects based on a specific condition.
```
jq '.[] | select(.key == "value")'
```

4. Array Projection: Extract specific elements from an array using indices or ranges.
```
jq '.[2,4,6]'
```

5. Object Projection: Select specific keys or key-value pairs from an object.
```
jq '.key1, .key2'
```

6. String Manipulation: Transform strings using built-in functions.
```
jq '.key | sub("old", "new")'
```

7. Sorting: Sort the elements of an array.
```
jq 'sort'
```

8. Aggregation: Compute aggregate values like sum, average, or maximum.
```
jq 'reduce .[] as $value (0; . + $value)'
```

9. Complex Filters: Combine multiple filters and conditions to extract specific data.
```
jq '.[] | select(.key1 == "value1") | .key2'
```

10. Output Formatting: Customize the output format, such as pretty printing.
```
jq '{ key: .key }'
```

These examples demonstrate various ways to format and manipulate JSON data using jq.

<details><summary>Metadata</summary>

- Duration: 9574 ms
- Datetime: 2023-08-31T12:40:45.672990
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
{"meta":{"id":"f3c84133-daa7-4fc2-a5b9-a1eecf75e8ab","node":"europe-west2","ms":1047,"api_balance":4.93},"data":[{"t":0,"rank":1,"url":"https://xkcd.com/1692/","title":"xkcd: Man Page","snippet":null},{"t":0,"rank":2,"url":"http://www.acme.com/software/thttpd/thttpd_man.html","title":"thttpd man page","snippet":"So for example, to make a custom error page for the authentication failure error, which is number 401, you would put your HTML into the file &quot;errors/err401.html&quot;. If no custom error file is found for a given error number, then the usual built-in error page is generated. thttpd will look first in the virtual host errors directory, and then in the se.."},{"t":0,"rank":3,"url":"https://rsync.samba.org/ftp/rsync/rsync.html","title":"rsync(1) man page","snippet":"This can be useful if you want to encrypt a daemon-style transfer&#39;s data, but since the daemon is started up fresh by the remote user, you may not be able to use features such as chroot or change the uid used by the daemon. Beginning in 3.2.0, this option is no longer auto-forwarded to the server side in order to allow you to specify different debu.."},{"t":0,"rank":4,"url":"https://terminusdb.com/blog/vector-database-and-vector-embeddings/","title":"Building a Vector Database to Make Use of Vector Embeddings","snippet":"The fact that this works has always seemed amazing to me, but it works even for fairly large documents provided our embedding space is of sufficiently high dimension. With modern deep learning methods, you can get excellent embeddings of complex documents.."}]} List 10 advanced examples using this source

**Response:**
1. Extract all titles from the JSON data:
```
jq '.data[].title' input.json
```

2. Filter and extract URLs for titles containing the term "man page":
```
jq '.data[] | select(.title | contains("man page")) | .url' input.json
```

3. Compute the average rank of the URLs:
```
jq '(.data[] | .rank) | add / length' input.json
```

4. Sort the URLs by rank in descending order:
```
jq '.data | sort_by(.rank) | reverse | .[].url' input.json
```

5. Extract the snippets for URLs with non-null snippets:
```
jq '.data | map(select(.snippet != null) | .snippet)' input.json
```

6. Group URLs by the starting character of the title:
```
jq 'group_by(.title[0]) | map({(.[0].title[0]): [.[] | .url]})' input.json
```

7. Count the number of URLs with the term "error" in the snippet:
```
jq '.data | map(select(.snippet | contains("error"))) | length' input.json
```

8. Extract the first 2 URLs with a rank above 1:
```
jq '.data | map(select(.rank > 1))[0:2] | .[].url' input.json
```

9. Replace the term "HTTP" with "HTTPS" in the URLs:
```
jq '.data | map(.url |= sub("HTTP"; "HTTPS"))' input.json
```

10. Select URLs with a rank between 2 and 4 and transform their titles to uppercase:
```
jq '.data[] | select(.rank >= 2 and .rank <= 4) | .title |= ascii_upcase' input.json
```

These examples demonstrate advanced jq usage to manipulate and extract specific information from the provided JSON data source. Please note that you need to replace "input.json" with the appropriate file or command to fetch the JSON data.

<details><summary>Metadata</summary>

- Duration: 13246 ms
- Datetime: 2023-08-31T12:43:27.905608
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

