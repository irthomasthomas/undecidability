**Prompt:**
Think of a new idea for a SMALL neat little linux cli tool written in bash. Write your feature request and detailed instructions to the programmer for him to build. Make sure to include all information required. And specify an automated test

**Response:**
Feature Request: Linux CLI Tool - Bash Directory Cleaner

Description:
I would like to request a new Linux CLI tool, called "Bash Directory Cleaner," which will automate the process of cleaning up directories by removing unnecessary files and organizing the remaining files into designated subdirectories. This tool should be written in bash scripting language to ensure compatibility across different Linux distributions.

Instructions for the Programmer:

1. Command-Line Arguments:
   a. "-h" or "--help": Display a help message and provide information about the tool, its usage, and available options.
   b. "-d <directory>" or "--directory <directory>": Specify the target directory to be cleaned. If no directory is provided, the current directory should be considered as the target.
   c. "-e <extension1,extension2,...>" or "--extensions <extension1,extension2,...>": Specify a comma-separated list of file extensions that should be preserved during the cleaning process. All other files with extensions not listed should be removed.
   d. "-o <directory>" or "--organize <directory>": Specify the destination directory where the tool should organize the remaining files based on their extensions. If not provided, a default directory named "organized" should be created within the target directory, and the files should be moved there.
   e. "-t" or "--test": Run an automated test to ensure the tool is functioning correctly and cleaning the directory as expected.

2. Directory Cleaning Process:
   The Bash Directory Cleaner tool should follow the following steps:
   a. Check if the target directory exists. If not, display an error message and exit.
   b. If the "-d" option is used, change the current directory to the one specified.
   c. List all files in the directory.
   d. Remove all files that do not match the provided extensions using the "-e" option. Display a message for each file removed.
   e. If the "-o" option is used, check if the destination directory exists. If not, create it.
   f. Move all remaining files to the destination directory, while preserving the directory structure. Display a message for each file moved. If the "-o" option is not used, create a "organized" directory within the target directory and move the files there.
 
3. Testing:
   Automate the following test scenario:
   a. Create a dummy directory structure with several files and subdirectories.
   b. Run the Bash Directory Cleaner tool on this dummy directory, specifying the "-e" option to preserve only a selected few extensions.
   c. Verify that the files with preserved extensions are moved to the designated destination directory (either specified through "-o" option or to the default "organized" directory).
   d. Ensure that all other files without the preserved extensions are removed from the directory.
   e. Display appropriate messages for each file removed or moved during the cleaning process.
   f. Check the resultant directory structure to confirm that the tool organized the remaining files correctly.

Note: The automated test should be repeatable, ensuring that it can be used for regression testing in the future, even if the directory or file structure changes.

Thank you for considering this feature request. Looking forward to seeing the "Bash Directory Cleaner" tool in action!

<details><summary>Metadata</summary>

- Duration: 20935 ms
- Datetime: 2023-08-30T19:05:24.520687
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

