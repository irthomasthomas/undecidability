**Prompt:**
Example python script 

**Response:**
Here is an example Python script that calculates the factorial of a given number using recursion:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)
```

In this script, the `factorial` function takes an integer `n` as input and calculates its factorial using recursion. The base case is when `n` is 0, in which case it returns 1. Otherwise, it multiplies `n` with the factorial of `n-1` and returns the result.

The user is prompted to enter a number, which is stored in the `number` variable. The `factorial` function is called with this number as input, and the result is stored in the `result` variable. Finally, the script prints the factorial of the given number.

<details><summary>Metadata</summary>

- Duration: 4287 ms
- Datetime: 2023-12-15T20:32:16.177093
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

