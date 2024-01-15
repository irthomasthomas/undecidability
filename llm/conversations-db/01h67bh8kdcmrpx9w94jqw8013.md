**Prompt:**
Write a perfect commit message for: diff --git a/.gitignore b/.gitignore
index 854c596..67a4585 100644
--- a/.gitignore
+++ b/.gitignore
@@ -1,3 +1,4 @@
+.idea
 .bak
 # Byte-compiled / optimized / DLL files
 __pycache__/
diff --git a/.gitignore.bak b/.gitignore.bak
new file mode 100644
index 0000000..854c596
--- /dev/null
+++ b/.gitignore.bak
@@ -0,0 +1,161 @@
+.bak
+# Byte-compiled / optimized / DLL files
+__pycache__/
+*.py[cod]
+*$py.class
+
+# C extensions
+*.so
+
+# Distribution / packaging
+.Python
+build/
+develop-eggs/
+dist/
+downloads/
+eggs/
+.eggs/
+lib/
+lib64/
+parts/
+sdist/
+var/
+wheels/
+share/python-wheels/
+*.egg-info/
+.installed.cfg
+*.egg
+MANIFEST
+
+# PyInstaller
+#  Usually these files are written by a python script from a template
+#  before PyInstaller builds the exe, so as to inject date/other infos into it.
+*.manifest
+*.spec
+
+# Installer logs
+pip-log.txt
+pip-delete-this-directory.txt
+
+# Unit test / coverage reports
+htmlcov/
+.tox/
+.nox/
+.coverage
+.coverage.*
+.cache
+nosetests.xml
+coverage.xml
+*.cover
+*.py,cover
+.hypothesis/
+.pytest_cache/
+cover/
+
+# Translations
+*.mo
+*.pot
+
+# Django stuff:
+*.log
+local_settings.py
+db.sqlite3
+db.sqlite3-journal
+
+# Flask stuff:
+instance/
+.webassets-cache
+
+# Scrapy stuff:
+.scrapy
+
+# Sphinx documentation
+docs/_build/
+
+# PyBuilder
+.pybuilder/
+target/
+
+# Jupyter Notebook
+.ipynb_checkpoints
+
+# IPython
+profile_default/
+ipython_config.py
+
+# pyenv
+#   For a library or package, you might want to ignore these files since the code is
+#   intended to run in multiple environments; otherwise, check them in:
+# .python-version
+
+# pipenv
+#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
+#   However, in case of collaboration, if having platform-specific dependencies or dependencies
+#   having no cross-platform support, pipenv may install dependencies that don't work, or not
+#   install all needed dependencies.
+#Pipfile.lock
+
+# poetry
+#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
+#   This is especially recommended for binary packages to ensure reproducibility, and is more
+#   commonly ignored for libraries.
+#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
+#poetry.lock
+
+# pdm
+#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
+#pdm.lock
+#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
+#   in version control.
+#   https://pdm.fming.dev/#use-with-ide
+.pdm.toml
+
+# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
+__pypackages__/
+
+# Celery stuff
+celerybeat-schedule
+celerybeat.pid
+
+# SageMath parsed files
+*.sage.py
+
+# Environments
+.env
+.venv
+env/
+venv/
+ENV/
+env.bak/
+venv.bak/
+
+# Spyder project settings
+.spyderproject
+.spyproject
+
+# Rope project settings
+.ropeproject
+
+# mkdocs documentation
+/site
+
+# mypy
+.mypy_cache/
+.dmypy.json
+dmypy.json
+
+# Pyre type checker
+.pyre/
+
+# pytype static type analyzer
+.pytype/
+
+# Cython debug symbols
+cython_debug/
+
+# PyCharm
+#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
+#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
+#  and can be added to the global gitignore or merged into this file.  For a more nuclear
+#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
+#.idea/
diff --git a/.idea/workspace.xml b/.idea/workspace.xml
index bf5449a..94e7570 100644
--- a/.idea/workspace.xml
+++ b/.idea/workspace.xml
@@ -4,7 +4,12 @@
     <option name="autoReloadType" value="SELECTIVE" />
   </component>
   <component name="ChangeListManager">
-    <list default="true" id="8af50231-0cb3-4ef9-9ec2-5d8c8b56c2b1" name="Changes" comment="" />
+    <list default="true" id="8af50231-0cb3-4ef9-9ec2-5d8c8b56c2b1" name="Changes" comment="">
+      <change beforePath="$PROJECT_DIR$/.gitignore" beforeDir="false" afterPath="$PROJECT_DIR$/.gitignore" afterDir="false" />
+      <change beforePath="$PROJECT_DIR$/.idea/workspace.xml" beforeDir="false" afterPath="$PROJECT_DIR$/.idea/workspace.xml" afterDir="false" />
+      <change beforePath="$PROJECT_DIR$/Scripts/OPEN_QnA.sh" beforeDir="false" />
+      <change beforePath="$PROJECT_DIR$/Scripts/control_slideshow.sh" beforeDir="false" />
+    </list>
     <option name="SHOW_DIALOG" value="false" />
     <option name="HIGHLIGHT_CONFLICTS" value="true" />
     <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
@@ -29,12 +34,14 @@
     "RunOnceActivity.OpenProjectViewOnStart": "true",
     "RunOnceActivity.ShowReadmeOnStart": "true",
     "WebServerToolWindowFactoryState": "false",
+    "git-widget-placeholder": "main",
     "last_opened_file_path": "/home/thomas/Development/Projects/StreamDeck",
     "node.js.detected.package.eslint": "true",
     "node.js.detected.package.tslint": "true",
     "node.js.selected.package.eslint": "(autodetect)",
     "node.js.selected.package.tslint": "(autodetect)",
-    "settings.editor.selected.configurable": "preferences.keymap",
+    "nodejs_package_manager_path": "npm",
+    "settings.editor.selected.configurable": "preferences.editor",
     "vue.rearranger.settings.migration": "true"
   }
 }]]></component>
@@ -74,7 +81,11 @@
       <option name="number" value="Default" />
       <option name="presentableId" value="Default" />
       <updated>1685093533678</updated>
-      <workItem from="1685109927546" duration="648000" />
+      <workItem from="1685109927546" duration="15476000" />
+      <workItem from="1685548649931" duration="75000" />
+      <workItem from="1685548729946" duration="599000" />
+      <workItem from="1685559021631" duration="2055000" />
+      <workItem from="1685639846713" duration="4960000" />
     </task>
     <servers />
   </component>
diff --git a/Scripts/OPEN_QnA.sh b/scripts/OPEN_QnA.sh
similarity index 100%
rename from Scripts/OPEN_QnA.sh
rename to scripts/OPEN_QnA.sh
diff --git a/Scripts/control_slideshow.sh b/scripts/control_slideshow.sh
similarity index 64%
rename from Scripts/control_slideshow.sh
rename to scripts/control_slideshow.sh
index 12d8148..1b75102 100755
--- a/Scripts/control_slideshow.sh
+++ b/scripts/control_slideshow.sh
@@ -6,19 +6,21 @@ function get_window_id() {
   wmctrl -l -x | grep "$SEARCH_TERM" | awk '{print $1}'
 }
 
-sleep 0.5
+sleep 0.2
 key_cmd="$1"
-sleep 0.1
+sleep 0.2
 wid=$(get_window_id "Slideshow")
 xdotool key --window "$wid" space
 sleep 0.1
 xdotool windowactivate "$wid"
-sleep 0.1
+sleep 0.2
 # xdotool key --window "$wid" "$key_cmd"
 # xdotool key "$key_cmd"
 
-xdotool keydown ctrl
-xdotool keydown $key_cmd
-xdotool keyup $key_cmd
-xdotool keyup ctrl
+xdotool keydown --window "$wid" ctrl
+xdotool keydown --window "$wid" $key_cmd
+xdotool keyup --window "$wid" $key_cmd
+xdotool keyup --window "$wid" ctrl
+xdotool key --window "$wid" Right
 sleep 0.1
+
diff --git a/scripts/control_slideshow.sh.bak b/scripts/control_slideshow.sh.bak
new file mode 100755
index 0000000..8c4e775
--- /dev/null
+++ b/scripts/control_slideshow.sh.bak
@@ -0,0 +1,26 @@
+#!/bin/bash
+# Send commands to a digikam Slideshow. Assumes a Slideshow is active.
+
+function get_window_id() {
+  SEARCH_TERM="$1"
+  wmctrl -l -x | grep "$SEARCH_TERM" | awk '{print $1}'
+}
+
+sleep 0.2
+key_cmd="$1"
+sleep 0.2
+wid=$(get_window_id "Slideshow")
+xdotool key --window "$wid" space
+sleep 0.1
+xdotool windowactivate "$wid"
+sleep 0.2
+# xdotool key --window "$wid" "$key_cmd"
+# xdotool key "$key_cmd"
+
+xdotool keydown --window "$wid" ctrl
+xdotool keydown --window "$wid" $key_cmd
+xdotool keyup --window "$wid" $key_cmd
+xdotool keyup --window "$wid" ctrl
+xdotool key --window "$wid" right
+sleep 0.1
+
. Always keep it concise and brief!

**Response:**
Update .gitignore and workspace.xml files, rename two scripts, and make minor modifications to control_slideshow.sh script

<details><summary>Metadata</summary>

- Duration: 1555 ms
- Datetime: 2023-07-25T20:23:30.649045
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

