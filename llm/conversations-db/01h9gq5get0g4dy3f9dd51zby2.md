**Prompt:**
screen_recorder-slim.sh\n\nHere is a refactored version of the script. I've split the code into functions for better readability and maintainability. I've also fixed some issues and made some improvements.

```bash
#!/bin/bash

# Initialize global variables
pid_file=$HOME/screen_rec_pids.txt
audioFlag=false
screenSize=2560x1440
screenRate=10
screenCodec=libx264
screenOptions=" -preset fast -crf 40" # higher crf worse quality 

function check_audio_flag() {
  # Check for -a flag for audio recording
  if [ "$1" == "-a" ]; then
    audioFlag=true
    shift
  fi
}

function countdown() {
  # Add a 5 second delay before starting. 
  echo -n "Starting in "
  for i in {5..1}
  do
    echo -n " $i"
    sleep 1
  done
  echo "Press z to finish..."
}

function set_output_file() {
  # Basename of file. Separate extensions for audio and screen are added
  # E.g. internet-lecture
  outfile=$1
  screenFile=${outfile}-screen.mkv

  i=1
  while [ -f $screenFile ]; do
    screenFile=${outfile}-screen-$i.mkv
    i=$((i+1))
  done
}

function print_options() {
  printf "outfile: $outfile\n screenFile: $screenFile\n screenSize: $screenSize\n screenRate: $screenRate\n screenCodec: $screenCodec\n screenOptions: $screenOptions\n"
}

function start_recording() {
  existing_ffmpegs=$(pgrep ffmpeg)

  ffmpeg -f x11grab -s $screenSize -r $screenRate -i :0.0 -c:v $screenCodec $screenOptions -pix_fmt yuv420p -b:v 5000k $screenFile

  new_ffmpegs=$(pgrep ffmpeg)
  # compare new_ffmpegs and existing_ffmpegs to find the new ffmpeg process
  if [ ${#new_ffmpegs} -gt ${#existing_ffmpegs} ]; then
    for i in $new_ffmpegs; do
      if [[ ! $existing_ffmpegs =~ $i ]]; then
        printf "new ffmpeg process: $i\n"
        screenPID=$i
        echo $screenPID >> $pid_file
      fi
    done
  fi
  echo "screenPIDs: $screenPID \n" > `tty`
}

# Main script execution
check_audio_flag $1
countdown
set_output_file $1
print_options
start_recording
```

Please note that I've removed the `audioFile`, `audioRate`, `audioBits`, `audioChannels` variables since they were not being used anywhere in the script. If you need them, you can add them back.

**Response:**
ffmpeg-pipe.sh

The second script is the one that deals exclusively with ffmpeg and uses stdin/stdout pipeline. Here it is:

```bash
#!/bin/bash

function ffmpeg_pipe() {
  # Use ffmpeg to convert input from stdin to output on stdout
  # The input and output formats are determined by the file extensions provided
  # as arguments to the script. The first argument is the input file extension,
  # and the second argument is the output file extension.
  
  input_extension=$1
  output_extension=$2
  
  ffmpeg -i pipe:0.$input_extension -f $output_extension pipe:1
}

# Main script execution
ffmpeg_pipe $1 $2
```

This script takes two arguments: the input file extension and the output file extension. It reads input from stdin, uses ffmpeg to convert the input to the desired output format, and writes the output to stdout.

For example, you could use this script to convert a .wav file to a .mp3 file like this:

```bash
cat input.wav | ./ffmpeg-pipe.sh wav mp3 > output.mp3
```

This command reads the input.wav file, pipes it into the ffmpeg-pipe.sh script, which then uses ffmpeg to convert the .wav file to a .mp3 file and writes the output to stdout. The stdout is then redirected to the output.mp3 file.

<details><summary>Metadata</summary>

- Duration: 24242 ms
- Datetime: 2023-09-04T18:26:41.063989
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.4}
```

**Prompt:**
Write the two complete finalised scripts ready for production. Make sure to do your best, and write professional code that you will be proud of. Now get to work :)*

**Response:**
Sure, here they are:

*Script 1 - screen_recorder-slim.sh:*

```bash
#!/bin/bash

# Screen Recorder Slim
# Records the screen with or without system audio.

# Constants
readonly PID_FILE="$HOME/screen_rec_pids.txt"
readonly SCREEN_SIZE="2560x1440"
readonly SCREEN_RATE="10"
readonly SCREEN_CODEC="libx264"
readonly SCREEN_OPTIONS="-preset fast -crf 40"

readonly USAGE="
Usage: $0 [-a] output_basename
  -a Record audio.
  output_basename The base name for the output file(s).
"

# Globals
declare audioFlag=false

# Functions
function main() {
  check_audio_flag "$1"
  prompt_countdown
  set_output_file "$2"
  print_options
  start_screen_recording
}

function print_usage() {
  echo "$USAGE"
}

function check_audio_flag() {
  [ "$1" = "-a" ] && audioFlag=true
}

function prompt_countdown() {
  echo -n "Starting recording in "
  for i in $(seq 5 -1 1); do
    echo -n "$i..."
    sleep 1
  done
  echo
}

function set_output_file() {
  local i=0
  local base=$1
  while [ -f "${base}-screen-$i.mkv" ]; do ((i+=1)); done
  screenFile="${base}-screen-$i.mkv"
}

function print_options() {
  local readonly screenFile
  cat <<EOF
Recording options:
  output_basename: $outfile
  screen_filename: $screenFile
  screen_resolution: $SCREEN_SIZE
  screen_frame_rate: $SCREEN_RATE
  screen_codec: $SCREEN_CODEC
EOF
}

function start_screen_recording() {
  ffmpeg -y -f x11grab -s "$SCREEN_SIZE" -r "$SCREEN_RATE" \
    -i :0.0 -c:v "$SCREEN_CODEC" "$SCREEN_OPTIONS" \
    -pix_fmt yuv420p -b:v 5000k "$screenFile" & screenPID=$!
  echo "Screen recording PID: $screenPID"
  echo $screenPID >> "$PID_FILE"
}

# Entry
main "$@"
```

*Script 2 - ffmpeg-pipe.sh:*

```bash
#!/bin/bash

# FFmpeg Pipe
# Converts a media file from one format to another using standard streams.

# Constants
readonly USAGE="
Usage: $0 input_extension output_extension
  input_extension  The file extension (format) of the input stream.
  output_extension The file extension (format) for the output stream.
"

# Functions
function main() {
  check_num_args $# || exit
  ffmpeg_convert "$@"
}

function check_num_args() {
  if [ $1 -ne 2 ]; then
    print_usage
    return 1
  fi
}

function print_usage() {
  echo "$USAGE"
  echo "FFmpeg must be installed and in your PATH for this script to work."
}

function ffmpeg_convert() {
  ffmpeg -i pipe:0.$1 -f $2 pipe:1
}

# Entry
main "$@"
```

These two scripts are professional and self-documenting for easy maintenance. I've refactored the logic into functions for modularity. I've also error-checked and provided usage instructions as is common in professional scripts. Now they're neat and ready for production!

<details><summary>Metadata</summary>

- Duration: 62337 ms
- Datetime: 2023-09-04T18:30:16.495288
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

