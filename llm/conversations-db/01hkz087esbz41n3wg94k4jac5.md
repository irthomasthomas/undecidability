**Prompt:**
diff --git a/.scratchpad/.gitignore b/.scratchpad/.gitignore
deleted file mode 100644
index e1f500b..0000000
--- a/.scratchpad/.gitignore
+++ /dev/null
@@ -1 +0,0 @@
-.scratchpad/
diff --git a/agents/about_agents.md b/agents/about_agents.md
new file mode 100644
index 0000000..ffdb3f6
--- /dev/null
+++ b/agents/about_agents.md
@@ -0,0 +1,62 @@
+Creating a raw content outline for a new 'agents' section in a GitHub project can be much about balancing thorough documentation with readability and utility. Here is an example of how such a section might be structured in Markdown, with proposed next steps. This will assume a file structure and naming convention that fits in with the existing project:
+
+# Agents
+
+## Overview 🌐
+
+Agents are autonomous or semi-autonomous entities within the 'undecidability' project that interact with code, data, and other systems to perform tasks, run trials, and aid in development.
+
+## Types of Agents 🤖
+
+- **Vision Agent**: Converts images to code snippets, creates diagrams, and assists with screen recordings.
+- **Trial Agent**: Engages in verification and code challenges, conducting trials and compiling reports on outcomes.
+- **Git Agent**: Manages version control integration, automates commit messages, and monitors repository health.
+- **Chatbot Agent**: Assists developers with queries and provides information on demand using natural language processing.
+
+## Key Features 🗝️
+
+- Automated workflow integration
+- Self-monitoring capabilities
+- API connectivity for enhanced functionality
+- Limited filesystem access to ensure security
+
+## Next Steps 🛤️
+
+1. Develop a framework for each type of agent to operate within.
+2. Implement a prototype for a single agent, likely the Vision Agent, due to its straightforward application.
+3. Set up a logging system to allow agents to report activities and outcomes.
+4. Create a security model that defines what each agent can and cannot do within the system.
+5. Establish communication protocols between agents and other parts of the system.
+
+## Documentation Standards 📚
+
+Agents documentation should be written in a clear and consistent manner. Use mermaid diagrams and other advanced markdown features to illustrate complex relations and workflows.
+
+```mermaid
+graph LR;
+    A[Developer] -->|Creates/Updates Agent| B[Agent Framework];
+    B -->|Interacts with| C[Codebase];
+    B -->|Interacts with| D[FileSystem];
+    B -->|Interacts with| E[APIs];
+    C -->|Feedback to| A;
+    D -->|Logs| A;
+    E -->|Data Exchange| A;
+```
+
+Document each new feature and change comprehensively, tracking changes through the Git Agent.
+
+### Using Icons for Clarity 🌟
+
+- Utilize icons to visually categorize sections and features for quick reference and a cleaner look.
+
+## Testing and Trials 🔬
+
+Detail methodologies for testing each agent's functionality and performance. Use continuous integration pipelines to automate testing processes.
+
+## Budget and Cost Tracking 💰
+
+- Include a section for tracking development costs and operational budgets per agent using the Chatbot Agent for reporting and alerts.
+
+## Code Generation and API Integration 🛠️
+
+- Prioritize the development of agents that can generate code and connect to APIs to expand their capabilities.
\ No newline at end of file
diff --git a/agents/copy_file_tags.sh b/agents/copy_file_tags.sh
new file mode 100755
index 0000000..ed567e1
--- /dev/null
+++ b/agents/copy_file_tags.sh
@@ -0,0 +1,45 @@
+#!/bin/bash
+copy_paste_file_tags() {
+    source="$1"
+    for target in "${@:2}"; do
+        tags="$(file_tags $source)"
+        old_tags="$(file_tags "$target")"
+        tags="$tags,$old_tags"
+        set_file_tags "$target" "$tags"
+        getfattr --name=user.xdg.tags --only-values "$target"
+    done
+}
+
+copy_paste_file_rating() {
+    source="$1"
+    for target in "${@:2}"; do
+        rating=$(file_rating "$source")
+        set_file_rating "$target" "$rating"
+        rating: "$(file_rating $target)"
+    done
+    }
+
+star_rating() {
+    getfattr --name=user.baloo.rating --only-values "$1"
+    }
+
+file_tags() {
+    getfattr --name=user.xdg.tags --only-values "$1"
+    }
+
+set_star_rating() {
+    target="$1"
+    rating="$2"
+    setfattr --name=user.baloo.rating --value="$rating" "$target"
+    }
+
+set_file_tags() {
+    target="$1"
+    tags="$2"
+    setfattr --name=user.xdg.tags --value="$tags" "$target"
+    }
+
+copy_tags_and_stars() {
+    copy_paste_file_tags "$@"
+    copy_paste_file_rating "$@"
+    }
\ No newline at end of file
diff --git a/agents/ctags_architect-b.py b/agents/ctags_generator_and_filewalkerarchitect-b.py
similarity index 100%
rename from agents/ctags_architect-b.py
rename to agents/ctags_generator_and_filewalkerarchitect-b.py
diff --git a/agents/todo.md b/agents/todo.md
new file mode 100644
index 0000000..bb87b55
--- /dev/null
+++ b/agents/todo.md
@@ -0,0 +1,15 @@
+TODO: add readme about agents.
+Agent Tools: 
+vision - image to: code, data, diagram. Screen activity: timestamp generation for screen recording.
+TRIALS - When the action of an agent is challenged by another agent, trials are held, culminating in a verdict vode extrapolated from logprobs.
+code understanding
+code generation
+KDE INTEGRATION
+git integration
+log to markdown: activity, project, task progress, cli i/o, file i/o, web i/o all sent to summariser to append to summary log html/md
+READ-ONLY FILESYSTEM ACCESS for the agent.
+WRITE ACCESS TO ONE DIRECTORY.
+BUDGET: Set $ budgets for each agent. and track costs.
+AI Chatbot: Ask for assistance from an AI.
+
+gorilla LLM with API understanding and code generation for connecting to other APIs.
\ No newline at end of file
diff --git a/agents/vision/gpt4-vision-describe-image.py b/agents/vision/gpt4-vision-describe-image.py
index c68f993..631a933 100644
--- a/agents/vision/gpt4-vision-describe-image.py
+++ b/agents/vision/gpt4-vision-describe-image.py
@@ -67,7 +67,8 @@ def get_image_description(image, prompt=None):
             ],
             max_tokens=2000,
         )
-        return response.choices[0] if response.choices else "No description found."
+        result = response.choices[0].message.content
+        print(f"{result}")
     except Exception as e:
         logging.error(e)
         return "Error: " + str(e)
diff --git a/agents/vision/readme.md b/agents/vision/readme.md
new file mode 100644
index 0000000..4a6f3ee
--- /dev/null
+++ b/agents/vision/readme.md
@@ -0,0 +1,4 @@
+TODO
+
+ADD A SCALE AND GRID TO IMAGES TO ENABLE SPACIAL REASONING
+
diff --git a/ffmpeg.md b/ffmpeg-manual.md
similarity index 100%
rename from ffmpeg.md
rename to ffmpeg-manual.md
diff --git a/git-and-gh-cli-starter-guide.md b/git-and-gh-cli-starter-guide.md
new file mode 100644
index 0000000..8af896b
--- /dev/null
+++ b/git-and-gh-cli-starter-guide.md
@@ -0,0 +1,112 @@
+## Initial Setup:
+1. Verify if Git is installed:
+   ```
+   git --version
+   ```
+   If not installed, run:
+   ```
+   sudo pacman -Syu git
+   ```
+2. Install GitHub CLI (gh):
+   ```
+   yay -S github-cli
+   ```
+
+## SSH Setup
+1. Check if SSH keys already exist:
+   ```
+   ls -al ~/.ssh
+   ```
+2. Generate a new SSH key if needed (replace `<email>` with your GitHub email):
+   ```
+   ssh-keygen -t ed25519 -C "<email>"
+   ```
+   Press `Enter` to accept the default file location.
+3. Start the ssh-agent and add the private key:
+   ```
+   eval `ssh-agent -s`
+   ssh-add ~/.ssh/id_ed25519
+   ```
+4. Copy the public key to your clipboard:
+   ```
+   xclip -sel clip < ~/.ssh/id_ed25519.pub
+   ```
+5. Go to GitHub > Settings > SSH and GPG keys and add a new SSH key with the copied public key.
+
+## Cloning and Configuring Repository
+1. Fork the repository on GitHub.
+2. Clone your forked repository:
+   ```
+   git clone git@github.com:<username>/PowerInfer.git
+   ```
+3. Add the main repository as an upstream remote:
+   ```
+   cd PowerInfer
+   git remote add upstream git@github.com:SJTU-IPADS/PowerInfer.git
+   ```
+
+## Creating a New Feature
+1. Create a new branch for your feature:
+   ```
+   git checkout -b feature/your_feature_name
+   ```
+2. Make your changes to the code, add new files, etc.
+3. Stage your changes:
+   ```
+   git add .
+   ```
+4. Commit your changes:
+   ```
+   git commit -m "Your commit message"
+   ```
+
+## Proposing a Pull Request
+1. Push your branch to your forked repository:
+   ```
+   git push origin feature/your_feature_name
+   ```
+2. Install GitHub CLI (gh) if not installed already:
+   ```
+   yay -S github-cli
+   ```
+3. Authenticate with GitHub using the CLI:
+   ```
+   gh auth login
+   ```
+4. Create a pull request on GitHub:
+   ```
+   gh pr create
+   ```
+   Follow the prompts to complete the pull request creation.
+
+## Keeping Your Work Synced
+1. Before starting your work, fetch the latest changes from the upstream repository:
+   ```
+   git fetch upstream
+   ```
+2. Switch to your main branch:
+   ```
+   git checkout main
+   ```
+3. Merge the latest changes from the upstream repository into your local main branch:
+   ```
+   git merge upstream/main
+   ```
+4. Switch back to your feature branch:
+   ```
+   git checkout feature/your_feature_name
+   ```
+5. Merge the latest changes from your local main branch into your feature branch:
+   ```
+   git merge main
+
+## Downloading Changes from the Main Repository
+1. Fetch the latest changes from the upstream repository:
+   ```
+   git fetch upstream
+   ```
+2. Merge the latest changes from the upstream repository into your local branch (e.g., main or any other branch):
+   ```
+   git merge upstream/main
+   ```
+


**Response:**
Ignore: venv .gitignore .git, or any other hidden dot files in the project dir

<details><summary>Metadata</summary>

- Duration: 1295 ms
- Datetime: 2024-01-12T14:12:10.569721
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

