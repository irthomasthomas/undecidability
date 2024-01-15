**Prompt:**
In KDE Plasma 5 running on manjaro (Arch) linux, how do I list the xdg
file tags, like dolphin uses? In the terminal

**Response:**
The tags used by Dolphin are stored in a database file named `baloofiles` by the `baloo` file indexer.

First, we need to find the `baloofiles`:

```
locate baloofiles
```

This usually yields a result like:

```
~/.local/share/baloo/file/fileMap.sqlite3
~/.local/share/baloo/file/idTreeDb.sqlite3
~/.local/share/baloo/file/inodeDb.sqlite3
~/.local/share/baloo/file/mtimesDb.sqlite3
~/.local/share/baloo/file/positionDb.sqlite3
~/.local/share/baloo/file/urlDb.sqlite3
~/.local/share/baloo/file/fileMap.sqlite3-journal
~/.local/share/baloo/file/idTreeDb.sqlite3-journal
~/.local/share/baloo/file/inodeDb.sqlite3-journal
~/.local/share/baloo/file/mtimesDb.sqlite3-journal
~/.local/share/baloo/file/positionDb.sqlite3-journal
~/.local/share/baloo/file/urlDb.sqlite3-journal
```

The file you're interested in is `~/.local/share/baloo/file/fileMap.sqlite3`.

You can inspect the database using sqlite3 like this:

```
sqlite3 ~/.local/share/baloo/file/fileMap.sqlite3
```

This gets you an sqlite3 prompt. To see all the tags, you can type this query:

```
SELECT * FROM tagsTable;
```

To quit, simply use `.quit`

Remember, you need `sqlite3` command line interface for SQLite installed. If not installed, you can install it using package manager:

```
sudo pacman -S sqlite
```

NOTE: 
- Manipulating `baloo` files directly should be done cautiously. 
- Please make sure that the `baloo_file` process is not running before manipulating the database, which can be done with the command `balooctl disable` and re-enabled with `balooctl enable`.

<details><summary>Metadata</summary>

- Duration: 26575 ms
- Datetime: 2023-09-03T10:28:57.281776
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

