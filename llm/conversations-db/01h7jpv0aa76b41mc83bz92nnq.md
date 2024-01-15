**Prompt:**
After thinking it through carefully, my top 5 favourite linux shell one-liners are... ?

**Response:**
1. Find and delete all files of a certain extension in a directory and its subdirectories:
```
find /path/to/directory -type f -name '*.txt' -delete
```
 
2. Sort a file numerically and print the last 10 lines:
```
sort -n file.txt | tail -n 10
```

3. Count the number of occurrences of a specific word in a file:
```
grep -o 'word' file.txt | wc -l
```

4. Remove duplicate lines from a file and keep the original order intact:
```
awk '!seen[$0]++' file.txt
```

5. Convert all filenames in a directory to lowercase:
```
rename 'y/A-Z/a-z/' *
```

<details><summary>Metadata</summary>

- Duration: 3354 ms
- Datetime: 2023-08-11T16:28:22.952427
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

