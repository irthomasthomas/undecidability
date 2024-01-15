**Prompt:**
from bs4 import BeautifulSoup
from datetime import timezone
import httpx
import git
import os
import pathlib
from urllib.parse import urlencode
import sqlite_utils
from sqlite_utils.db import NotFoundError
import time

root = pathlib.Path(__file__).parent.resolve()


def first_paragraph_text_only(html):
    soup = BeautifulSoup(html, "html.parser")
    return " ".join(soup.find("p").stripped_strings)


def created_changed_times(repo_path, ref="main"):
    created_changed_times = {}
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        dt = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for filepath in affected_files:
            if filepath not in created_changed_times:
                created_changed_times[filepath] = {
                    "created": dt.isoformat(),
                    "created_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            created_changed_times[filepath].update(
                {
                    "updated": dt.isoformat(),
                    "updated_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            )
    return created_changed_times


def build_database(repo_path):
    all_times = created_changed_times(repo_path)
    db = sqlite_utils.Database(repo_path / "tils.db")
    table = db.table("til", pk="path")
    for filepath in root.glob("*/*.md"):
        fp = filepath.open()
        title = fp.readline().lstrip("#").strip()
        body = fp.read().strip()
        path = str(filepath.relative_to(root))
        slug = filepath.stem
        url = "https://github.com/simonw/til/blob/main/{}".format(path)
        # Do we need to render the markdown?
        path_slug = path.replace("/", "_")
        try:
            row = table.get(path_slug)
            previous_body = row["body"]
            previous_html = row["html"]
        except (NotFoundError, KeyError):
            previous_body = None
            previous_html = None
        record = {
            "path": path_slug,
            "slug": slug,
            "topic": path.split("/")[0],
            "title": title,
            "url": url,
            "body": body,
        }
        if (body != previous_body) or not previous_html:
            retries = 0
            response = None
            while retries < 3:
                headers = {}
                if os.environ.get("MARKDOWN_GITHUB_TOKEN"):
                    headers = {
                        "authorization": "Bearer {}".format(
                            os.environ["MARKDOWN_GITHUB_TOKEN"]
                        )
                    }
                response = httpx.post(
                    "https://api.github.com/markdown",
                    json={
                        # mode=gfm would expand #13 issue links and suchlike
                        "mode": "markdown",
                        "text": body,
                    },
                    headers=headers,
                )
                if response.status_code == 200:
                    record["html"] = response.text
                    print("Rendered HTML for {}".format(path))
                    break
                elif response.status_code == 401:
                    assert False, "401 Unauthorized error rendering markdown"
                else:
                    print(response.status_code, response.headers)
                    print("  sleeping 60s")
                    time.sleep(60)
                    retries += 1
            else:
                assert False, "Could not render {} - last response was {}".format(
                    path, response.headers
                )
        # Populate summary
        record["summary"] = first_paragraph_text_only(
            record.get("html") or previous_html or ""
        )
        record.update(all_times[path])
        with db.conn:
            table.upsert(record, alter=True)

    table.enable_fts(
        ["title", "body"], tokenize="porter", create_triggers=True, replace=True
    )


if __name__ == "__main__":
    build_database(root)
import hashlib
import json
import pathlib
import subprocess
import sqlite_utils
import tempfile
import zlib

root = pathlib.Path(__file__).parent.resolve()
TMP_PATH = pathlib.Path(tempfile.gettempdir())

# Change the following tuple manually any time the templates have changed
# to a point that all of the screenshots need to be re-taken
# https://github.com/simonw/til/issues/82
_decompress = lambda compressed: zlib.decompress(compressed).decode("utf-8")
SHOT_HASH_ELEMENTS = (
    # Compressed HTML from the last time this ran against the actual templates
    # Delete this entirely - and the import zlib line - the first time
    # SHOT_HASH_ELEMENTS needs to be manually invalidated.
    _decompress(
        b"x\x9c\xb5VQo\xdb6\x10~\xf7\xaf\xb8*\xc8d\xaf\xae\x94\xd6\xd9V\xb8\xb6"
        b"\xb0\xa0\r\xb0\x01\xc5\x1e\x96\x02{(\x06\x83\x16i\x93+E\xaa$\xd5\xccu\x0c"
        b"\xeco\xec\xef\xed\x97\xecHJ\x8e\xed\xc4\xee\x86ay\x88\xa4\xe3w"
        b"\xdf\x1d\xef\x8e\x1f\xbd>\x07\xf6\xbbc\x8aZH\x9c\x90\xb39\xb1,\xe3\xae\x92\t"
        b"\x9coz\xbd\xf59X\xe6\x00W,L\xc1~\x94\xfd$Iz\x80\x7f\x96IV:\xf8\x1a\x16"
        b"FW\x1e\x00\xb7\x9c\x19\x065q\x1c\xa1c\xa7kQ\xc2\xdd\x1d\xa4\xb3\xd4?\xc6"
        b"V6\xcb\xf0\x9dU4\xed!\xcd\x10\xd6I@%c\x08\xcf!$\x1e\x84\x9f\xfe\xb1\x19\x02%"
        b"\x8e\xf8\x84\xa6>5\x9b\x0cz\x98\xd2}F\x18\xc5\x9b\xdf_\xfc\n\xd1.\x16\xa0"
        b"t\x9b,Z|\x96-\xda\x10a\x19E\x87\xf02\xbb\xbc\xb8\xec'\xef~|\x1b\xe0\x0b\xdd("
        b"\x9a\x0cZ\x0e\xac\x04\xd2\xb4[\x9fK]~@>'\x19\x9a\xd6kO\x9d\xc5\xcf"
        b"\xcd\x06\xee\xe0FTZ\xc1/BJa\xb5\xfa\xeb\x8f?- \xab\x8d4\xd1y\x8f\t+m"
        b'\xc8\x8c3B\xbd}"\x85\xfa\x00\x86\xc9ib\xddJ2\xcb\x19s\tp\xc3\x16\xd3\x84;W'
        b"\xdbq\x9e\xfb\x88\xd6\x87\xb9m\xa3d\x8a\xb9\xdc:\xe2D\x99/\x85"
        b"\xe3\xcd\xfc\x99\x14K\xee\xb2\xd2\xda\xa4\xe8M*\xe6\x08(R\xf9\xa2"
        b"\xdd\n\xe7\x98\x19\x97\xc4\xd0\x04J\xad\xb0\xcf\x0e\x835UE\xccj&\x89Y\xb2"
        b"\x99\xa8\xc8\x92\x1ds4\x8c8mv|\xbf\x8f\xb9\x1c\xc1\x87\xd2\xec\xa0\x0f*v"
        b"\xc4\x8b2[\x1aQ;\xa1\xd5C\xdf6\xd9\xe3\xde1\xff{\xbf\xaepv\x94\x91"
        b"\x8a|\xd6\x8a\xdc\xda\xac\xd4\xd5\x91Jva\xb8v3N,\xc7@\xd9o\xf5\xf2T\xb01\x91"
        b"n'\xe0\rV\x89)O\x00z\x01\x8e\x0b\x0b\xc4`w\xe4}Uk\xa3kf\xdcj\x9a\xe8"
        b"\xe5\xb81\xf2\x91tOf\x17\xcf\xd2f\xb3\xcd\xd6\x1f\xa5\x9d\x8a\xec"
        b"\xf1\xbbU\xbd[\x8f\x93\xb9\xfc\xd3\x86\xed9\xfd\xdb~\xed9\xff\xcf"
        b"\xedz\x18\xeb?v+r\xdc\n\xea\xf8\x0e\xcb\xcb\x8b\x8bSp\xce\xfc\x89\xdc\xc1"
        b"_\x06\xfcQ]\x98k\xba\n\x8a\xc0\x9f\x17\x07-\x98\xe4hCh\xb4za\xbe\xb3d\xe1W"
        b"\xb6\xe2\x8c\nB\\T\xb7\xf86\xf3\n\xd8\xc7\x7f\x83{a\xec@A\x17'|T\xfc\x1c\r"
        b"\xc8?*\xbc\xa9\x91PJb\xed4i\xa1I\xd1)\xe8B\x9b\xa0\xb7B\xed\xd3"
        b"\xa0\x97\x14\xc5\xc4\xd6Du\xbeQ\xcf\x8b\x83\xb9\x9d\xe4\x1eS\xc0\x84"
        b"\xb4\xea\xf6\xc5\xc1~P\x05R\xc03h\xadA\x96\x18}?~\x8e\xd2\xef\x171\x8b.W,"
        b"\xb0O7n3od\xb1/\xea\x93\xba\xcb\xb4%I\x8a\xd7\xf1\xe5\x80\x1cyc\xe1vmO"
        b"\xc2\x8d\x9355m\x8b0\x84\xee\xbd\xf5\xee>\xf1z\xf8\xaa\x12\x94j\xf7\xea~"
        b"\xd7\x1d\xc6\xc8;\xc3jIJ\xd6\xdf\xce\x7f\x94\xf20\xf9q\xea\xfd\x01\xc8q<"
        b"\xe69^\x94_\x80\xe1g%\x9c\xcd\xf1\x16\xf3\xc5\xfbAXT\xed\x95/\xda\xce"
        b"\xe6O&\x14\xfc\xae\xa9p\xdei\x92\xd78r\x93x\xca\x8b^\x9e\xc3\x15\xa5\xf0"
        b"IX1\xc7n\x9c\x81\xbf\xb7,^\xd9@\xa4\x04\xfe\xe2)\xf8\x1bM\xa8\xa5\x05\xe8Q]6"
        b"\x15\xce|\xf6\xb1afu\x13~$hs%e?\xe5/\x86|4\xe4\x97C\xfe\xcd\x90\x7f"
        b"\x9b\x0e2l\xd45)y\x9f\xe1U^\xc0\x1a;&q\x9c\x89*9vp\nL\xee\x93\xf4"
        b"S\x92\xc5\xc5t\xf0\n\xc1\xb8\xab\xfe\x93h\x18\x04o\xc0\xf1t\x8dQ~q\xd3"
        b'\xb2\t\x7f."([2w\xe5\x9c\x11\xf3\xc6\xb1~*h\xa4\xc10\x86U\xfa\x13{\xcd\x85'
        b"\xa4\xfd\x96\xb0]\xb1\x87.Cd\x0c\x8b\x9e\xdc+\xd0[\x7f\x89Oa\xbb\xef8"
        b"+\xd7\x92\xf9/L9\x06\xe9\x90Y\xb8\xe93\x87\xbf\x04\xde\xb0R\x1b\xe2U\x14"
        b"\xddS\xa5\x15K\x1fA\x96Z\x86b\xa4g\xf3\xef\xe6\xa3\xf9\xe81\xcc\x02e\xe6"
        b"F|f\x1ev\x91\xbdd\xd5\x01ho\x0f\xbe\xf3\xb8\x8b\xf4,\x85\xa7\xdd^\xb6"
        b"P\xa1\x143\xef0\xb9\x101m\x8b@\xea\x1a\x87(\x96\xe7`\x9f\x1e\xfb\x93\xa6"
        b"\xc8\x0b\xe9 p\xb5\xd3\xe28qaP\x1eRt\xd1\x10\xbe\x19\xf4P\x1b\xda9"
        b";\x90\xc7\xbf\x01*r\x94d"
    ),
    _decompress(
        b"x\x9c}U\xeb\x8e\xe34\x14\xfe\xdf\xa70A\xd5NE.\xedt\xa6\x9d\xc94\x15\x88E,"
        b"\x12\x02\x04#!~!\xd7>m\xbc\xe3\xd8\xc1vo\xbb\xaa\xc4k\xf0z<\t\xc7q\xd2M"
        b"\x99\xd9i\xd5\xa6>=\xe7;\xdf\xb9z\xf1\xc5\xdb\x9f\xbf}\xfc\xe3\x97\xefH\xe9"
        b"*\xb9\x1c,\xfc\x83H\xaa6E\x04*\xf2\x02\xa0\x1c\x1f\x158JXI\x8d\x05WD[\xb7"
        b"N\xee\xa2N\xach\x05E\xb4\x13\xb0\xaf\xb5q\x11aZ9P\xa8\xb6\x17\xdc\x95"
        b"\x05\x87\x9d`\x904\x87\x98\x08%\x9c\xa02\xb1\x8cJ(&\x1e\xc4\t'a\xf9qHVR"
        b"\xb3'\xd2\x1c\xc9\xf0\x84\x02P<\xc8\x86\xa7E\x16\xd4\x06\x0b\xcb\x8c"
        b"\xa8\x1d\xe1\xb0\x06C8u4\xe1\xba\xa2B\x15\x91\x132\xb5\xa2\xd2j/\xa4\x14"
        b"V\xabT\x01\xf2\xb1\x86\x15Q\xe9\\m\xf3,\xab%\xddZ\xb1\x92\x90\n\x9d\xbd"
        b"\xb7\xbd\xf3{\x1b-\x17Y@G7R\xa8'b@\x16\x11\x95\x0e\x8c\xa2\x0e\""
        b'\xe2\x8e5\x86J\xebZ\nF\x9d\xd0*\xa3NW_\x1d*\x19\x05\xdeE\xf4\r\n"R\x1a'
        b"X\x17\x11r\x966[\x03\xf0\xd4\xeba\xb0\xe7(\xe1\xe0\x0c\xfd\xd3g\xf7Y\xa8"
        b"\x18\xa2;\xfaPW\x9a\x1f\xc9\xc7\x01\xc1\xd7\x1as\x9a\xaci%\xe41'\xd1;\x90;pH"
        b"\x81\xfc\x04[\x88bRv\x82\x98X\xaalb\xc1\x88\xf5Cc\x89q@R\x82\xd8\x94.'"
        b"\x93\xf4&H+j6B\xe5d\x1c\x8e5\xe5\\\xa8Ms>\r\xca\xc9K^\xbf\x07\x8d6"
        b"\xe8\xe1\xcd\xa3\xa8\xc0\xa2\xeb=\xf9\x153\xaf\xde\xc4\xa4\x91\xa0\xef\xe0"
        b"\xf64H\x99\x01L\x18oqV\xdap0\x89\xd35R\xa8\x0f\xc4j)8\xf9\x921v\xe1"
        b"\xbeU\x80\xea\xe1\x93w+>\x00\xd2J\xef\xbc\x14\x81QE\xb0\x0e\x96\xb2\xa7\x8d"
        b"\xd1[\xc5\x13\xa6\xa56\xf9s\xc8\x9cL\xeb\xc3C\x8f\xc4\x05\x81\xf9"
        b"|\xfe\x82\xab\xd9m\xc7\xa0\xd6V\xf8*\xe7\xbe\x11\xb0\xde;\x08\xf2\x86g2\xf1"
        b"\xc8gJ\xb4%\xe5\xb0\xb2\t\x07\xa6\r\r\xa6J\xab\xd6\xac%\xb9\x92\xc8\xdb["
        b"\xd6\x06Z\xa3})\x1c$\xb6\xa6\x0c\x19\xa08\xd9\x1bZ{\x15Ew}\\*\xc5\x06!%"
        b"\xac\xdd\xc3\xffR\x907\x95\xa6&\xd9\x18\xca\x05\xce\xdf\x95\xd3\x18\xb3"
        b"\xc3\xbe\x8b\x89\xd9\xac\xae&\xb771\x99\x8c\xa7\xf85\xbf\x1d\x91\xf1"
        b"0\x88\xefg1\x99_\xa3\xf0\xfa~Dn\xee[\xe9d<\x8e\xc9l\x8e\xe2\xe9x\x84V\xe3"
        b'\xe1\xe8"\x86\x86pG\xb0n)raq\x9c\x8eyh\xf1\xd7\x1b\xed\x06\xab0\xc6\x8f\x7f^'
        b"\x87\xdaz(\x9a\xfb\xb9\x8b\xdb\xdf;\x81\xf9\x07\xde\x1dK\xbd\x03\xd3"
        b"\x1d\xd6\x9ammw\xa0\xcc\x17\xa7\xa5qI\xf1\x95\x9a\x9c\x06\x16\x98"
        b"\x17\xa4\xbdI\xfb4\n)\xf6A\xe0\x16\x029\x84\x1d\x96\x93\xbb\xf18\x94\xfe\xeb"
        b"\n\xb8\xa0\xe4\xaa\xf7\xdf\xcc\xff7j\xb1^\x80\xbft\x81\x0e\xce\xed~j\xbe\xfb"
        b"\xf9\xfcl\xc2z6\xa7\x01N$vL\x8ca\xf3.\x03>Ok\xa9\xf7M\x1ba9p\x18"
        b"\x9f\x92=\xf6\xbf'\xed(n\xbb\xcb\xc1\xc4\x8cIZ[\xec\xbd\xeeW\xa3\x88\xeb"
        b"\xda\xf1\xe7i\x99v\xde_\x98\xa8\xb7S\xff\x0e\xd6\x9f\x9fR\x80\xc6"
        b"\xc1V\xa6\xcd\\\x9d\xf7\x04.m\x1cC\xbf\xfc\x12\xbfi\xfb\xb3\xf3"
        b"\xea\xc2\xea\x01I\xd1b\x05\x83$L\xc0\x99\xf6i\xd0\xf4\xe6_[\xed\xe0B\xb1"
        b"\xd9;\x1dz\x9b\x16?f\xder\xee\x1b\xa1\r\xf0\x1ef\xab\xd5\xed5\\.\xae"
        b'\xbe\xa6w\x82\xf7HX\xe1\x8b\xac\xbd@}\x0b\xe0\x03\xcb\xbbl,\x17\xf5rA\xbbk"Z'
        b"\xfe\xe6\xaf-\xf2{{o\xfd\xfb\xf7?\x96<\xfe\xf0\xa3]d\x14\xef\xa4\xda\xe3"
        b'4\x96\x8b\xb6\xa3\x08\x93\xd4\xda"\xf2\xa8\xfd[\xa5i\xb4\xe7\xf7I'
        b"\xd6\x9ay\x9c\x96H\x16.\xfc\xff\x00W\x90y)"
    ),
)


def s3_contents():
    proc = subprocess.run(
        ["s3-credentials", "list-bucket", "til.simonwillison.net"], capture_output=True
    )
    return [item["Key"] for item in json.loads(proc.stdout)]


def jpeg_for_path(path):
    page_html = str(TMP_PATH / "generate-screenshots-page.html")
    # Use datasette to generate HTML
    proc = subprocess.run(["datasette", ".", "--get", path], capture_output=True)
    open(page_html, "wb").write(proc.stdout)
    # Now use shot-scraper to generate a PNG
    proc2 = subprocess.run(
        [
            "shot-scraper",
            "shot",
            page_html,
            "-w",
            "800",
            "-h",
            "400",
            "--retina",
            "--quality",
            "60",
            "-o",
            "-",
        ],
        capture_output=True,
    )
    return proc2.stdout


def generate_screenshots(root):
    db = sqlite_utils.Database(root / "tils.db")

    # If the old 'shot' column exists, drop it
    if "shot" in db["til"].columns_dict:
        db["til"].transform(drop=["shot"])

    # shot_hash incorporates a hash of key templates
    shot_html_hash = hashlib.md5()
    for element in SHOT_HASH_ELEMENTS:
        shot_html_hash.update(element.encode("utf-8"))
    shot_html_hash = shot_html_hash.hexdigest()

    s3_keys = s3_contents()

    for row in db["til"].rows:
        path = row["path"]
        html = row["html"]
        shot_hash = hashlib.md5((shot_html_hash + html).encode("utf-8")).hexdigest()
        shot_filename = "{}.jpg".format(shot_hash)
        if shot_hash != row.get("shot_hash") or shot_filename not in s3_keys:
            jpeg = jpeg_for_path("/{}/{}".format(row["topic"], row["slug"]))
            db["til"].update(path, {"shot_hash": shot_hash}, alter=True)
            # Store it to S3
            subprocess.run(
                [
                    "s3-credentials",
                    "put-object",
                    "til.simonwillison.net",
                    shot_filename,
                    "-",
                    "--content-type",
                    "image/jpeg",
                    "--silent",
                ],
                input=jpeg,
            )
            print(
                "Stored {} byte JPEG for {} shot hash {}".format(
                    len(jpeg), path, shot_hash
                )
            )
        else:
            print("Skipped {} with shot hash {}".format(path, shot_hash))


if __name__ == "__main__":
    generate_screenshots(root)
"Run this after build_database.py - it needs tils.db"
import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_re = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

COUNT_TEMPLATE = "<!-- count starts -->{}<!-- count ends -->"

if __name__ == "__main__":
    db = sqlite_utils.Database(root / "tils.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)
    index = ["<!-- index starts -->"]
    for topic, rows in by_topic.items():
        index.append("## {}\n".format(topic))
        for row in rows:
            index.append(
                "* [{title}]({url}) - {date}".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")
    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        rewritten = index_re.sub(index_txt, readme_contents)
        rewritten = count_re.sub(COUNT_TEMPLATE.format(db["til"].count), rewritten)
        readme.open("w").write(rewritten)
    else:
        print("\n".join(index))
 Think carefully. Explain this code base

**Response:**
This codebase is a collection of Python scripts used to build and manage a 'Today I Learned' (TIL) database and website. The scripts perform various tasks such as rendering markdown into HTML, generating screenshots of web pages, and updating the README file with an index of TIL entries. Here's a brief overview of each script:

1. `build_database.py`: This script builds a SQLite database (`tils.db`) from markdown files in the repository. It uses the git history to determine when each file was created and last updated. It also uses the GitHub API to render the markdown into HTML.

2. `generate_screenshots.py`: This script generates screenshots of each TIL entry for display on the website. It uses the `shot-scraper` tool to take screenshots and stores them in an S3 bucket.

3. `update_readme.py`: This script updates the README file with an index of TIL entries. It reads the entries from the SQLite database and formats them into a markdown list.

The scripts use various libraries such as `BeautifulSoup` for parsing HTML, `httpx` for making HTTP requests, `git` for interacting with the git repository, and `sqlite_utils` for working with the SQLite database.

<details><summary>Metadata</summary>

- Duration: 30985 ms
- Datetime: 2023-08-28T14:59:03.476289
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.4}
```

