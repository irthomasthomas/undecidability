**Prompt:**
escape $ in yaml so its not detected as a variable?

**Response:**
To escape the `$` character in YAML so that it is not detected as a variable, you can use the double quotation marks (`"`). By enclosing the string that contains the `$` character in double quotes, it will be treated as a literal string without any variable interpolation.

Here is an example:

```yaml
example_key: "$100"
```

In this YAML snippet, the value of `example_key` will be the string `"$100"`, preserving the `$` character as part of the value.

<details><summary>Metadata</summary>

- Duration: 3675 ms
- Datetime: 2024-01-07T14:08:29.453008
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

