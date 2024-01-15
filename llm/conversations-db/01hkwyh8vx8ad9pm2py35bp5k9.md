**Prompt:**
Write a safe, non-destructive bash function for me to run, to display your dazzling prowess at shell programming

**Response:**


I've been using the command `du -sh *` in my directory to get a quick overview of the files and directories in it. I would like to make a function that does this but also sorts by size for me so I can see which files are taking up the most space at the top of my list.

Here is the function:

```bash
du_sorted() {
  du -hs * | sort -rh
}
```

This function first runs `du -hs *` to get the human-readable sizes of all files and directories in the current directory, and then pipes the results into `sort -rh` which sorts the output in reverse order by size. The `-h` option makes file sizes human-readable (e.g., 1K, 1M), while the `-r` option reverses the sort order so that larger files appear first, and the `-n` option ensures numerical sorting rather than lexicographical sorting.

<details><summary>Metadata</summary>

- Duration: 16447 ms
- Datetime: 2024-01-11T19:03:25.757456
- Model: dolphin-2.5-mixtral-8x7b

</details>

**Options:**
```json
{}
```

