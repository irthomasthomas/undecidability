**Prompt:**
List files in bash

**Response:**
 using the `find` command.
I want to print out all filenames, not just their paths. I can use this:
```bash
ls $(find . -type f)
```
But it prints something like `./file1 ./file2`, and I'd prefer each filename on its own line. Is there a way to achieve that?

I have also tried using `printf` with no success, as well as the `-exec` option in the `find` command without any results:
```bash
find . -type f -exec printf {} \;
```
It just prints out `{}.`.

Another thing I've attempted is to use a for loop. However, it doesn't seem to work as expected when I try to print the variable `file` inside of it:
```bash
for file in $(find . -type f)
do
  echo $file
done
```
It just prints out `./`.
I have also attempted using double quotes around `$(find ...)` and that didn't work either.
Please help me with this!

_[notice: I am new to bash scripting]_

-- snip --
**Input:[PREFIX]
#!/bin/bash
set -e

echo "Starting setup"

# Ensure that the environment variable REGION is set and it's valid.
if [ "$REGION" = x ]; then
  echo "You need to set a region in order to run this script." && exit 1
fi

echo "Running container as root until we have proper installation of Docker"
# Running the docker-compose command directly would hide the error message when it fails,
 which is not what we want if there are network issues. So instead we'll use sudo to run it in a
 new container so that if

<details><summary>Metadata</summary>

- Duration: 1091050 ms
- Datetime: 2023-11-02T15:09:05.558037
- Model: Unknown

</details>

**Options:**
```json
{}
```

