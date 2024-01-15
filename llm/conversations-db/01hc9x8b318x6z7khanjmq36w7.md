**Prompt:**
 ~ streamdeck                                       
Traceback (most recent call last):
  File "/usr/bin/streamdeck", line 5, in <module>
    from streamdeck_ui.gui import start
  File "/usr/lib/python3.11/site-packages/streamdeck_ui/gui.py", line 10, in <module>
    import pkg_resources
ModuleNotFoundError: No module named 'pkg_resources'

**Response:**
The error message indicates that the required module `pkg_resources` is not found. 

To resolve this issue, you can try installing the `setuptools` package, which includes the `pkg_resources` module:

```shell
pip install setuptools
```

If you already have `setuptools` installed but are still facing the issue, you can try upgrading it:

```shell
pip install --upgrade setuptools
```

Once the installation or upgrade is complete, try running the `streamdeck` command again, and the error should be resolved.

<details><summary>Metadata</summary>

- Duration: 3283 ms
- Datetime: 2023-10-09T09:45:50.732957
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

