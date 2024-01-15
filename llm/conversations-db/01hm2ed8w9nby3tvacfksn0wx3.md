**Prompt:**
diff --git a/agents/vision/chat-with-gpt4-about-screencast-narration.md b/agents/vision/chat-with-gpt4-about-screencast-narration.md
new file mode 100644
index 0000000..1a4df62
--- /dev/null
+++ b/agents/vision/chat-with-gpt4-about-screencast-narration.md
@@ -0,0 +1,115 @@
+Refining and combining your codes into a single polished version would involve the following steps:
+
+1. Modularizing key functionalities (screenshot capturing, image comparison, image processing for GPT-4-Vision, and description generation).
+2. Implementing error handling and logging consistently across all modules.
+3. Ensuring that the processed images fit the input requirements of GPT-4-Vision API.
+4. Streamlining the flow of operations, from taking screenshots to generating and yielding narrations.
+
+Here is the integrated script:
+
+```python
+import os
+import time
+import logging
+import numpy as np
+import subprocess
+from datetime import datetime
+from PIL import Image, ImageChops
+from openai import OpenAI
+
+logging.basicConfig(level=logging.INFO)
+
+def take_screenshot(output_directory='/tmp'):
+    if not os.path.exists(output_directory):
+        os.makedirs(output_directory)
+    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
+    screenshot_path = os.path.join(output_directory, f'screenshot_{timestamp}.png')
+    ffmpeg_command = f'ffmpeg -n -f x11grab -i :0.0 -vframes 1 -s $(xdpyinfo | grep dimensions | awk \'{{print $2}}\') {screenshot_path} -loglevel panic'
+    result = subprocess.run(ffmpeg_command, shell=True, capture_output=True)
+    if result.returncode != 0:
+        logging.error("Failed to take screenshot.")
+        return None
+    return screenshot_path
+
+def calculate_similarity(image1_path, image2_path):
+    try:
+        image1 = Image.open(image1_path)
+        image2 = Image.open(image2_path)
+        if image1.size != image2.size or image1.size == (0, 0):
+            logging.error("Images have different dimensions or are empty.")
+            return None
+        diff = ImageChops.difference(image1, image2)
+        diff_array = np.array(diff)
+        similarity = np.sum(np.abs(diff_array) > 0)
+        return 100 - (similarity * 100 / diff_array.size)
+    except Exception as e:
+        logging.error(f"Error calculating similarity: {str(e)}")
+        return None
+
+def gptv_describe(base64_image1, base64_image2):
+    client = OpenAI()
+    response = client.chat.completions.create(
+        model="gpt-4-vision-preview",
+        messages=[
+            {
+                "role": "user",
+                "content": [
+                    {
+                        "type": "image_url",
+                        "image_url": {
+                            "url": f"data:image/jpeg;base64,{base64_image1}"
+                        },
+                    },
+                    {
+                        "type": "image_url",
+                        "image_url": {
+                            "url": f"data:image/jpeg;base64,{base64_image2}"
+                        },
+                    },
+                ],
+            }
+        ],
+        max_tokens=300,
+    )
+    if not response.choices:
+        logging.error("Empty response from OpenAI.")
+        return None
+    return response.choices[0].message.content
+
+def image_to_base64(image_path):
+    with open(image_path, "rb") as image_file:
+        return base64.b64encode(image_file.read()).decode('utf-8')
+
+def monitor_screenshots(interval=10, similarity_threshold=99.5):
+    base_image_path = take_screenshot()
+    if base_image_path is None:
+        return
+    image1_base64 = image_to_base64(base_image_path)
+
+    while True:
+        new_screenshot_path = take_screenshot()
+        if new_screenshot_path is None:
+            continue
+        similarity = calculate_similarity(base_image_path, new_screenshot_path)
+        if similarity is not None and similarity < similarity_threshold:
+            image2_base64 = image_to_base64(new_screenshot_path)
+            description = gptv_describe(image1_base64, image2_base64)
+            if description:
+                yield description
+            base_image_path = new_screenshot_path
+            image1_base64 = image2_base64
+        elif similarity is None:
+            logging.warning("Error in similarity calculation.")
+        else:
+            logging.info("No significant changes detected.")
+            os.remove(new_screenshot_path)
+        time.sleep(interval)
+
+if __name__ == "__main__":
+    print("Starting screenshot monitoring...")
+    for description in monitor_screenshots():
+        print(description)
+```
+This script is concise and contains the essential components for monitoring the screen, capturing screenshots, comparing images, and describing the differences utilizing GPT-4-Vision API. It should run a continuous monitoring loop that captures screenshots at a specified interval, compares them for significant changes, and if a change is detected, encodes the images to base64 and sends them to the API for description.
+
+Remember to install all the dependencies and configure OpenAI API keys before running the script.
\ No newline at end of file
diff --git a/agents/vision/narator.py b/agents/vision/narator.py
new file mode 100644
index 0000000..cb2141e
--- /dev/null
+++ b/agents/vision/narator.py
@@ -0,0 +1,100 @@
+from IPython.display import display, Image, Audio
+
+import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
+import base64
+import time
+from openai import OpenAI
+import os
+import requests
+
+client = OpenAI()
+
+def extract_frames():
+    """Extract frames from a video and return them as a list of base64-encoded strings."""
+    v1 = "/home/thomas/Videos/complete-auto-data-entry-ai_EDIT_1.mkv"
+    # video = cv2.VideoCapture("/home/thomas/Development/AI/openai/openai-cookbook/examples/data/bison.mp4")
+    video = cv2.VideoCapture(v1)
+
+    base64Frames = []
+    while video.isOpened():
+        success, frame = video.read()
+        if not success:
+            break
+        _, buffer = cv2.imencode(".jpg", frame)
+        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
+
+    video.release()
+    print(len(base64Frames), "frames read.")
+    return base64Frames
+
+# base64Frames = extract_frames()
+# display_handle = display(None, display_id=True)
+# for img in base64Frames:
+#     display_handle.update(Image(data=base64.b64decode(img.encode("utf-8"))))
+#     time.sleep(0.025)
+
+def describe_frame_by_second(base64Frames):
+    """Describe a series of frames using OpenAI's API."""
+    PROMPT_MESSAGES = [
+        {
+            "role": "user",
+            "content": [
+                    "These are frames from a video that I want to upload.  Generate a compelling description that I can upload along with the video.",
+                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50]),
+            ],
+        },
+    ]
+    params = {
+        "model": "gpt-4-vision-preview",
+        "messages": PROMPT_MESSAGES,
+        "max_tokens": 200,
+    }
+
+    result = client.chat.completions.create(**params)
+    print(result.choices[0].message.content)
+
+
+def narrate_frames(base64Frames):
+    PROMPT_MESSAGES = [
+        {
+            "role": "user",
+            "content": [
+                "These are frames of a video. Create a short voiceover. The video shows my screen as I work as I work on my Augmented Intelligence Toolkit. Here I am using openai GPT-4-Vision to my list of blocked domains in my kagi account and translate the image into structured output. Here I am simply requesting the domain names be printed line by line. The output is then automatically entered into the azure custom search page using a xdotool in a shell script. Only include the narration.",
+                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::200]), 
+            ],
+        },
+    ]
+    params = {
+        "model": "gpt-4-vision-preview",
+        "messages": PROMPT_MESSAGES,
+        "max_tokens": 500,
+    }
+
+    result = client.chat.completions.create(**params)
+    print(result.choices[0].message.content)
+    return result
+
+
+def tts(text):
+    response = requests.post(
+        "https://api.openai.com/v1/audio/speech",
+        headers={
+            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
+        },
+        json={
+            "model": "tts-1-1106",
+            "input": text,
+            "voice": "fable",
+        },
+    )
+
+    audio = b""
+    for chunk in response.iter_content(chunk_size=1024 * 1024):
+        audio += chunk
+    Audio(audio)
+
+frames = extract_frames()
+# description = describe_frame_by_second(frames)
+narration = narrate_frames(frames)
+tts(narration.choices[0].message.content)
+
diff --git a/agents/vision/screenshot-to-data-entry.sh b/agents/vision/screenshot-to-data-entry.sh
new file mode 100644
index 0000000..324d1b8
--- /dev/null
+++ b/agents/vision/screenshot-to-data-entry.sh
@@ -0,0 +1,64 @@
+#!/bin/bash
+# screenshot-to-data-entry.sh
+
+# target_file should be the file that is being edited
+# target_file="$1:-/home/thomas/undecidability/.scratchpad/blocked_urls_list_2.txt"
+source /home/thomas/Development/Projects/llm/.venv/bin/activate
+
+if [ -z "$1" ]; then
+    target_file="/home/thomas/undecidability/.scratchpad/blocked_urls_list_2.txt"
+else
+    target_file="$1"
+fi
+# remove target_file if it exists
+if [ -f "$target_file" ]; then
+    rm "$target_file"
+fi
+
+screenshot_path="/home/thomas/undecidability/.scratchpad/screenshot.png"
+# kdialog --passivepopup "$i" 1 # 
+# notify-send -t 3000 "Augmented Intelligence system is taking over in 5 seconds. 
+# Activate the window with the data you want me to read."
+kdialog --passivepopup "Augmented Intelligence system is taking over in 5 seconds.Activate the window with the data you want me to read." 5
+sleep 5
+for i in 5 4 3 2 1;
+do
+  kdialog --passivepopup "$i" 1
+  sleep 1
+done
+spectacle -a -b -n -r -o "$screenshot_path"
+# send screen shot for processing
+work_request="read the image and tell me the domains listed. 
+Just write one url per line and SAY NOTHING ELSE. 
+Write no text at all before or after."
+python "/home/thomas/undecidability/agents/vision/GPT4-vision-toolkit.py" describe "$screenshot_path" "$work_request" --output md --stream > "$target_file" &
+# wait for the file to be created
+
+while [ ! -f "$target_file" ]; do # 
+    sleep 1
+done
+notify-send -t 3000 "Reading complete. Move the cursor to the window you want me to type into."
+for i in {3..1}; do
+    notify-send -t 1000 "Typing output in $i seconds"
+    sleep 1
+done
+sleep 5
+split_token=":"
+while IFS= read -r line; do
+    # if we are on the first line, check if it contains a colon
+    if [ "$line" == "$(head -n 1 "$target_file")" ]; then
+        if [[ "$line" == *"$split_token"* ]]; then
+            # remove everything before the colon
+            line="$(echo "$line" | cut -d "$split_token" -f2-)"
+        fi
+    fi
+    xdotool type --delay 100 "$line"
+    xdotool key Return
+done < "$target_file"
+
+# when complete, delete the file
+# rm "$target_file"
+
+
+
+


**Response:**
Added new script for monitoring screenshots, capturing, comparing, and describing differences using GPT-4-Vision API. Also added scripts for extracting frames from a video and generating descriptions and voiceovers using GPT-4-Vision API. Included a shell script for automating the process of taking screenshots, processing them, and typing the output into a specified file.

<details><summary>Metadata</summary>

- Duration: 1963 ms
- Datetime: 2024-01-13T22:17:18.557470
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

**Prompt:**
base64 does not exist in the image_to_base64 func.

**Response:**
Refactored the `image_to_base64` function to use the `base64` module instead of the non-existent `base64` module.

<details><summary>Metadata</summary>

- Duration: 1292 ms
- Datetime: 2024-01-13T22:27:57.560403
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
Error: the base64.b64encode, pylance says base64 does not exist in the image_to_base64 func.

**Response:**
Refactored the `image_to_base64` function to import the `base64` module and use the `b64encode` function correctly.

<details><summary>Metadata</summary>

- Duration: 869 ms
- Datetime: 2024-01-13T22:28:36.529717
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

