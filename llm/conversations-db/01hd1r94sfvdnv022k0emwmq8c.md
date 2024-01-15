**Prompt:**
Write a bash terminal command to turn off any fonts that create symbolic ligatures
Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/EnableLigatures': <0>}"

<details><summary>Metadata</summary>

- Duration: 4648 ms
- Datetime: 2023-10-18T16:00:39.174412
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

