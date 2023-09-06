**Title:** KDE Activity and GitHub Repository Linking Tool

**I. Introduction**

The solution is a tool that improves focus and productivity by linking KDE activities with associated GitHub repositories. Within each KDE activity, terminal commands are constrained to the directory of the linked project. Shifting to directories outside the project scope results in prompt actions including switching KDE activities or creating tasks/notes for later.

**II. General Requirements**

The development environment should include:
- Manjaro (Arch) Linux
- KDE Desktop Environment for managing activities
- GitHub repositories for project management and issues
- Github Actions
- Bash or Zsh shell for script creation
- QDbus for KDE activity management
- gh (githubs git wrapper cli) for version control and repository management

**III. Functional Requirements**

1. The tool should be able to retrieve the current KDE activity name and Activity ID.

    Example functions for KDE activity fetch:

    ```
    current_activity_id() {
        qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
    }

    activity_name_from_id() {
        qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$1"
    }
    ```

2. Match the fetched activity name to a Github repo of the same name in a predefined local storage location, if it exists.

3. If the current working directory (CWD) is not the directory for the matched repository, the tool should navigate the terminal session to the correct directory.

4. The tool should constrain the terminal’s “cd” command to only directories within the associated project directory (related to the KDE activity).

5. If a user attempts to “cd” to an unrelated directory:

  a. The tool should deny the request.

  b. The tool should display a prompt allowing the user to:

        i. Switch to a different KDE activity linked to the desired directory if it exists.

        ii. Create a note or a To-Do item related to the requested path to be handled later.

6. The tool should refresh the terminal constraints each time KDE activity is changed.


**IV. Non-Functional Requirements**

1. Portability: The software should be runnable from any Linux terminal.
2. Usability: The system should provide clear and concise prompts when needed.
3. Resilience: The program should handle errors gracefully, displaying useful error messages.

**V. Maintenance and Support**

The developer should periodically maintain the tool for bug fixes, improvements, and compatibility with ongoing updates of KDE, Git and qdbus.

In conclusion, the tool aims to streamline task management and focus for developers who work on diverse projects simultaneously. By linking project directories to KDE activities, the tool creates an environment conducive for increased productivity and efficiency.
