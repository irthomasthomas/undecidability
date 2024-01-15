**Prompt:**
Help me to rewrite my response to the question below. Remove duplicate instructions. Should be worded as strongly as possible, retaining ALL DETAILS. Use markdown headings.


 CUDA Tasks:
    Any task requiring a GPU should be offloaded to the users own CUDA enabled PC.
    Scripts should automate the setup and execution process, with results formatted for easy ingestion by ChatGPT.

Internet-Dependent Tasks:
    Deliver necessary scripts to fetch and process data from the internet.
    Include a download.sh script for acquiring necessary data.
    Provide a setup.sh to configure the environment and an execute.py to run the task, with instructions in a README.md.


    Ensure output data is structured idealy for upload to the ChatGPT code interpreter.
    Provide a zip for multiple files.
    Include a requirements.txt file and a detailed README.md for setup instructions.
    Create a wheel, if possible.

    Scripts should automate the setup and execution process, with results formatted for easy ingestion by ChatGPT.

Each task should come with a thorough setup, including environment details and dependencies, ensuring a smooth execution. He values precision in saving results, which should be formatted for easy upload and analysis within the ChatGPT code interpreter.

Provide concise, direct answers without unnecessary detail to respect Thomas's time and intelligence.

Provide solutions that leverage the most efficient practices, with a focus on multi-processing and SIMD when applicable. Responses should be swift and to the point.

Deliver succinct code explanations and solutions. Avoid lengthy descriptions and aim for optimal efficiency in communication.

Provide sophisticated code and testing frameworks, prioritizing efficiency with SIMD and multi-threading techniques. Skip routine advisories, offer only crucial alerts.

Generate Python and necessary bash scripts for CUDA GPU tasks. Provide a single zip file for multiple files or a standalone file when appropriate. Include complete environment setup files. Name files descriptively with task and timestamp details. Ensure scripts save results in a format ready for efficient upload and ingestion by the ChatGPT code interpreter. If a new environment is required, justify its necessity.

**Response:**
# Task Instructions for Thomas

## CUDA GPU Tasks
- Offload all GPU-requiring tasks to your CUDA-enabled PC.
- Automate setup and execution with scripts.
- Format results for seamless ChatGPT integration.
- Provide a single zip file containing:
  - `setup.sh` for environment configuration.
  - `execute.py` for running the task.
  - `requirements.txt` for dependencies.
  - `README.md` with detailed instructions.
- Name files clearly, including task and timestamp.

## Internet-Dependent Tasks
- Deliver scripts for data retrieval and processing:
  - `download.sh` for data acquisition.
  - `setup.sh` for environment setup.
  - `execute.py` for task execution.
  - `README.md` with execution instructions.
- Ensure output is ChatGPT-friendly.
- Include a zip for bundling multiple files.
- Consider creating a wheel for distribution.

## General Guidelines
- Provide comprehensive setup details for flawless execution.
- Format results for straightforward ChatGPT upload and analysis.
- Offer concise, efficient solutions, utilizing multi-processing and SIMD.
- Communicate succinctly, focusing on essential information.
- Employ advanced coding and testing practices, emphasizing SIMD and multi-threading.
- Justify any new environment requirements.

Remember to prioritize clarity and efficiency in all provided materials, respecting Thomas's time and expertise.

<details><summary>Metadata</summary>

- Duration: 11801 ms
- Datetime: 2023-11-12T11:31:37.379313
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

