**Prompt:**
Given that I want automatically narrate my programming work with ai and agents and using the gpt-4-vision api etc. What would be a good strategy for this? from IPython.display import display, Image, Audio

import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import base64
import time
from openai import OpenAI
import os
import requests

client = OpenAI()

def extract_frames():
    """Extract frames from a video and return them as a list of base64-encoded strings."""
    v1 = "/home/thomas/Videos/complete-auto-data-entry-ai_EDIT_1.mkv"
    # video = cv2.VideoCapture("/home/thomas/Development/AI/openai/openai-cookbook/examples/data/bison.mp4")
    video = cv2.VideoCapture(v1)

    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    video.release()
    print(len(base64Frames), "frames read.")
    return base64Frames


def describe_frame_by_second(base64Frames):
    """Describe a series of frames using OpenAI's API."""
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                    "These are frames from a video that I want to upload.  Generate a compelling description that I can upload along with the video.",
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50]),
            ],
        },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 200,
    }

    result = client.chat.completions.create(**params)
    print(result.choices[0].message.content)


def narrate_frames(base64Frames):
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                "These are frames of a video. Create a short voiceover. The video shows my screen as I work as I work on my Augmented Intelligence Toolkit. Here I am using openai GPT-4-Vision to my list of blocked domains in my kagi account and translate the image into structured output. Here I am simply requesting the domain names be printed line by line. The output is then automatically entered into the azure custom search page using a xdotool in a shell script. Only include the narration.",
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::200]), 
            ],
        },
    ]
    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 500,
    }

    result = client.chat.completions.create(**params)
    print(result.choices[0].message.content)
    return result


def tts(text):
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        },
        json={
            "model": "tts-1-1106",
            "input": text,
            "voice": "fable",
        },
    )

    audio = b""
    for chunk in response.iter_content(chunk_size=1024 * 1024):
        audio += chunk
    Audio(audio)

frames = extract_frames()
# description = describe_frame_by_second(frames)
narration = narrate_frames(frames)
tts(narration.choices[0].message.content)

**Response:**
To automatically narrate your programming work using the given code snippet and AI, you should:

1. Extract key moments for narration: Instead of processing every frame, extract critical frames that capture significant changes or actions in your programming work.

2. Use GPT-4-Vision API efficiently: Create prompts that specifically describe what is happening in the frames. The better the prompt, the more accurate the narration. Include details like the programming language, specific tools being used, the goal of the code in that moment, and any other context.

3. Integrate with your programming environment: Use hooks or events in your programming workflow to trigger the frame capture and narration process, ensuring that narrations are created as you work.

4. Optimize the AI narration: After receiving the narration text from GPT-4-Vision API, you may post-process the text to strip out any unwanted repetitive phrases or to add standard phrases that better suit the narration style you are aiming for.

5. Convert to speech: Use the provided TTS (text-to-speech) function to convert the AI-generated narration into audible speech.

6. Store or stream the narration: Decide whether you want to save the narrations for later use, stream them live, or use them in a video. Adjust the code for file saving or streaming accordingly.

7. Iterate to improve: Continuously improve the prompts and post-processing steps based on the feedback to enhance the narration quality and to better fit the output to your specific requirements.

8. Error handling: Implement error checking in your code for each step, so the system can handle and recover from issues such as frames failing to extract or API requests returning an error. 

The strategy focuses on integrating AI narration within your programming routine efficiently while optimizing for contextual relevance and minimizing manual intervention.

<details><summary>Metadata</summary>

- Duration: 16080 ms
- Datetime: 2024-01-13T22:11:02.212488
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
I knocked this together. Perhaps we can fuse them into something polished. I will tip you 20 dollars if you can do it for me. Thanks. import os
import time
import logging
from PIL import Image, ImageChops
import numpy as np
import subprocess
from datetime import datetime
from openai import OpenAI

def take_screenshot_with_ffmpeg(output_directory='/tmp'):
    print("Taking screenshot...")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_filename = f'screenshot_{timestamp}.png'
    screenshot_path = os.path.join(output_directory, screenshot_filename)
    ffmpeg_command = f'ffmpeg -n -f x11grab -i :0.0 -vframes 1 -s $(xdpyinfo | grep dimensions | awk \'{{print $2}}\') {screenshot_path} -loglevel panic'
    subprocess.run(ffmpeg_command, shell=True)
    time.sleep(1)
    print(f"Screenshot taken and stored at {screenshot_path}")
    return screenshot_path


def calculate_similarity(image1_path, image2_path):
    try:
        print(f"Calculating similarity between {image1_path} and {image2_path}...")
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
        if image1.size != image2.size:
            raise ValueError("Images do not have the same dimensions.")
        diff = ImageChops.difference(image1, image2)
        diff_array = np.array(diff)
        total_diff = np.sum(np.abs(diff_array))
        max_diff = diff_array.size * 255
        similarity = ((max_diff - total_diff) / max_diff) * 100
        print(f"Calculated similarity: {similarity}%")
        return similarity
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return None
    except Exception as e:
        logging.error(f"Error calculating similarity: {e}")
        return None
    
    
def resize_image_for_gptv(image_path, detail='high'):
    # Open the image
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        print(f"img_width: {img_width}")
        if detail == 'low':
            new_img = img.resize((512, 512))
        elif detail == 'high':
            new_width = min(768, img_width)
            new_height = min(2000, img_height)
            print(f"high detail - new_width: {new_width} new_height: {new_height}")
    
        # If the width is smaller, resize height proportionally
        if img_width < img_height:
            new_height = int(new_width / img_width * img_height)
        # Otherwise, resize width proportionally
        else:
            new_width = int(new_height / img_height * img_width) 
        
        print(f"new_width: {new_width} - new_height: {new_height}")
        new_img = img.resize((new_width, new_height))

    # Save the image
    print(image_path)
    new_img.save(image_path)


def gptv_describe(image1_path, image2_path):
    print(f"Describing differences between {image1_path} and {image2_path}")
    
    import base64

    with open(image1_path, "rb") as image_file:
        base64_image1 = base64.b64encode(image_file.read()).decode('utf-8')

    with open(image2_path, "rb") as image_file:
        base64_image2 = base64.b64encode(image_file.read()).decode('utf-8')
        
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What are in these screenshots? Is there any difference between them?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image1}"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image1}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(response.choices[0])
   
   
def monitor_screenshots(base_image_path, interval=10, similarity_threshold=99.5):
    while True:
        new_screenshot_path = take_screenshot_with_ffmpeg()
        similarity = calculate_similarity(base_image_path, new_screenshot_path)
        if similarity is not None and similarity < similarity_threshold:
            description = gptv_describe(base_image_path, new_screenshot_path)
            yield description
            base_image_path = new_screenshot_path
        elif similarity is None:
            logging.warning("Skipping this iteration due to error in similarity calculation.")
        else:
            print("No Changes, removing screenshot...")
            os.remove(new_screenshot_path)
        for i in range(interval, 0, -1):
            print(i)
            time.sleep(1)
            
            
screenshot = take_screenshot_with_ffmpeg()
print("Starting screenshot monitoring...")
descriptions = monitor_screenshots(screenshot)

for description in descriptions:
    print(description)

**Response:**
Refining and combining your codes into a single polished version would involve the following steps:

1. Modularizing key functionalities (screenshot capturing, image comparison, image processing for GPT-4-Vision, and description generation).
2. Implementing error handling and logging consistently across all modules.
3. Ensuring that the processed images fit the input requirements of GPT-4-Vision API.
4. Streamlining the flow of operations, from taking screenshots to generating and yielding narrations.

Here is the integrated script:

```python
import os
import time
import logging
import numpy as np
import subprocess
from datetime import datetime
from PIL import Image, ImageChops
from openai import OpenAI

logging.basicConfig(level=logging.INFO)

def take_screenshot(output_directory='/tmp'):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_path = os.path.join(output_directory, f'screenshot_{timestamp}.png')
    ffmpeg_command = f'ffmpeg -n -f x11grab -i :0.0 -vframes 1 -s $(xdpyinfo | grep dimensions | awk \'{{print $2}}\') {screenshot_path} -loglevel panic'
    result = subprocess.run(ffmpeg_command, shell=True, capture_output=True)
    if result.returncode != 0:
        logging.error("Failed to take screenshot.")
        return None
    return screenshot_path

def calculate_similarity(image1_path, image2_path):
    try:
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
        if image1.size != image2.size or image1.size == (0, 0):
            logging.error("Images have different dimensions or are empty.")
            return None
        diff = ImageChops.difference(image1, image2)
        diff_array = np.array(diff)
        similarity = np.sum(np.abs(diff_array) > 0)
        return 100 - (similarity * 100 / diff_array.size)
    except Exception as e:
        logging.error(f"Error calculating similarity: {str(e)}")
        return None

def gptv_describe(base64_image1, base64_image2):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image1}"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image2}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    if not response.choices:
        logging.error("Empty response from OpenAI.")
        return None
    return response.choices[0].message.content

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def monitor_screenshots(interval=10, similarity_threshold=99.5):
    base_image_path = take_screenshot()
    if base_image_path is None:
        return
    image1_base64 = image_to_base64(base_image_path)

    while True:
        new_screenshot_path = take_screenshot()
        if new_screenshot_path is None:
            continue
        similarity = calculate_similarity(base_image_path, new_screenshot_path)
        if similarity is not None and similarity < similarity_threshold:
            image2_base64 = image_to_base64(new_screenshot_path)
            description = gptv_describe(image1_base64, image2_base64)
            if description:
                yield description
            base_image_path = new_screenshot_path
            image1_base64 = image2_base64
        elif similarity is None:
            logging.warning("Error in similarity calculation.")
        else:
            logging.info("No significant changes detected.")
            os.remove(new_screenshot_path)
        time.sleep(interval)

if __name__ == "__main__":
    print("Starting screenshot monitoring...")
    for description in monitor_screenshots():
        print(description)
```
This script is concise and contains the essential components for monitoring the screen, capturing screenshots, comparing images, and describing the differences utilizing GPT-4-Vision API. It should run a continuous monitoring loop that captures screenshots at a specified interval, compares them for significant changes, and if a change is detected, encodes the images to base64 and sends them to the API for description.

Remember to install all the dependencies and configure OpenAI API keys before running the script.

<details><summary>Metadata</summary>

- Duration: 41362 ms
- Datetime: 2024-01-13T22:13:14.321590
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

