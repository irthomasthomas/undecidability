**Prompt:**
Think of a new idea for a neat linux cli tool written in bash. Write your feature request and detailed instructions to the programmer for him to build. Make sure to include all information required. And specify an automated test

**Response:**
Feature Request:
Development of a Linux CLI tool in bash, named as "DistFileShare", that would allow users to easily share files across different Linux distributions within the same network.

Instructions:
1. Tool should be built as a Bash Shell Script and should be compatible across all enhancements of Bourne shell (bash, ksh, sh)
2. Tool should detect IP addresses within the same network and facilitate seamless file sharing
3. Tool should prompt user to select the target Linux distribution to send the file to
4. It should prompt the user to select the file or directory to be shared
5. The tool should provide a progress report on the file transfer process and notify the user once the file transfer is complete
6. The receiving system should not need to have the tool installed to receive files
7. The tool should handle interruptions in the network and resume file transfer once the network is available
8. In case the file or directory already exists in the receivers end, the tool should warn the user and ask for overwrite confirmation
9. Please handle all possible exceptions and test thoroughly for bugs and potential security loopholes

Automated Test:

Below is the suggested automated test that should cover all basic functionalities of DistFileShare CLI tool.

1. Setup: Have at least two virtual or physical Linux machines in the same network.
2. Install the DistFileShare tool on one of the machines (Sender).
3. Generate random files of different sizes (few KBs to few GBs) and directories in the sender's machine.
4. Begin tests:

   a. Use our tool to send files and directories from sender to other machines. Make sure to also test sending hidden files.
   
   b. During the file transfer, intermittently disconnect and reconnect the network. The tool should be able to handle these interruptions and resume file transfer smoothly.
   
   c. Have files with the same names on the receivers end and check if the tool correctly prompts the overwriting warning.
   
5. Validation: For each sent file, compare the hash (md5, sha-1, etc.) of sent and received file. The hashes should match.
6. Repeat step 4 and 5 for different Linux distributions.
   
End of test: If steps 4 and 5 are done properly for different Linux distributions, our tool is working as intended.

<details><summary>Metadata</summary>

- Duration: 37988 ms
- Datetime: 2023-08-30T18:56:31.929126
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

