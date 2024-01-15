**Prompt:**
#!

**Response:**
 /usr/bin/env python

import sys


def is_palindrome(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False


def main():
    for line in sys.stdin:
        word = line.strip()
        print(is_palindrome(word))


if __name__ == '__main__':
    main()


<details><summary>Metadata</summary>

- Duration: 1664 ms
- Datetime: 2023-11-27T20:50:36.203028
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 0.5}
```

