**Prompt:**
in elinks on arch linux, give some exapmle lua commands to use

**Response:**
ELinks on Arch Linux does come with the support for lua scripting, however, this requires the interpreter to be installed on your system. Lua provides a way to automate some tasks in ELinks or add some functionality.

But there isn't a substantial amount of documentation available for the usage of lua within ELinks.

Note: ELinks lua scripting is not same as using lua on command line or its own interpreter. The functions and usage are specific to what ELinks has defined it to use.

1. To execute lua per file from commandline:
```
elinks -eval 'require("filename_without_lua_extension")'
```
2. To execute Lua string from commandline:
```
elinks -eval 'function hello() return ("Hello, world!") end'
```
3. You can add functionality with Lua for keybindings in ELinks, for example:
```
elinks.conf
-----
set scriptfile = "~/.elinks/hooks.lua"

hooks.lua 
-----
function goto_prev_link()
    move_link(-1)
end
set_kbcontext('document')
bind_key('1', 'goto_prev_link')
```
Again, your mileage may vary with Lua scripting in ELinks as it's not covered well in the documentation. The best way would be to check out the source code of ELinks to understand what functions are available to use.

<details><summary>Metadata</summary>

- Duration: 25604 ms
- Datetime: 2023-08-23T19:10:04.381817
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

