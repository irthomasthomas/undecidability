# QnA: CLI Tool for Technical Q&A Logging

QnA is a command-line interface (CLI) tool designed to help developers and technical professionals record and manage their questions, problems, and corresponding answers or solutions. This tool is particularly useful for logging insights derived from Large Language Models (LLMs) or LLM+Websearch interactions.

## Features

- Record technical questions and their answers
- Store solutions derived from LLMs or LLM+Websearch
- Quick search and retrieval of past Q&As
- Simple tagging system for easy categorization
- Clipboard integration for seamless copy-paste operations

## Requirements

- Linux operating system with X11
- Bash shell
- xclip (for clipboard operations)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/qna.git
   ```

2. Navigate to the cloned directory:
   ```
   cd qna
   ```

3. Make the script executable:
   ```
   chmod +x qna.sh
   ```

4. (Optional) Add the script to your PATH for easy access:
   ```
   echo 'export PATH=$PATH:/path/to/qna' >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage

Basic usage:
```
./qna.sh [options] [command]
```

Commands:
- `add`: Add a new question and answer
- `search`: Search for existing Q&As
- `list`: List all Q&As
- `tag`: Add or remove tags from a Q&A

Options:
- `-q`: Specify a question
- `-a`: Specify an answer
- `-t`: Add tags
- `-c`: Copy answer to clipboard

Examples:
```
# Add a new Q&A
./qna.sh add -q "How to check disk usage in Linux?" -a "Use the 'du' command" -t "linux,command-line"

# Search for Q&As
./qna.sh search "disk usage"

# List all Q&As
./qna.sh list

# Add a tag to an existing Q&A
./qna.sh tag 1 "important"

# Copy an answer to clipboard
./qna.sh -c 1
```

## Data Storage

Q&As are stored in a simple text file format in `~/.qna/data.txt`. Each entry is separated by a delimiter for easy parsing.

## Limitations

- This is a proof-of-concept implementation and may have limitations in terms of scalability and feature set.
- Currently only supports Linux systems with X11.
- No built-in backup or sync functionality.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is a proof of concept and may contain bugs or security issues. Use at your own risk.
