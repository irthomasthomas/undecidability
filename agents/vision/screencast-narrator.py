import os
import time
import subprocess
import logging
import numpy as np
import requests
from datetime import datetime
from PIL import Image, ImageChops
from openai import OpenAI
import base64

# Initialize logging
logging.basicConfig(level=logging.INFO)

def take_screenshot(output_directory='/tmp'):
    """
    Takes a screenshot of the screen and saves it to the specified output directory.

    Args:
        output_directory (str): The directory where the screenshot will be saved. Defaults to '/tmp'.

    Returns:
        str: The path of the saved screenshot file, or None if the screenshot capture failed.
    """

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
    """
    Calculates the similarity between two images.

    Args:
        image1_path (str): The file path of the first image.
        image2_path (str): The file path of the second image.

    Returns:
        float: The similarity between the two images as a percentage, or None if there was an error.
    """
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

def gptv_describe(base64_image1, base64_image2):
    """
    Generates a description of two images using the GPT-4 Vision model.

    Args:
        base64_image1 (str): The base64-encoded image data of the first image.
        base64_image2 (str): The base64-encoded image data of the second image.

    Returns:
        str: The generated description of the images.
    """
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
    """
    Convert an image file to base64 encoding.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64 encoded string representation of the image.

    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def monitor_screenshots(interval=1, similarity_threshold=99):
    """
    Monitors screenshots taken at regular intervals and detects significant changes between consecutive screenshots.

    Args:
        interval (int, optional): The time interval between consecutive screenshots in seconds. Defaults to 10.
        similarity_threshold (float, optional): The minimum similarity threshold (in percentage) below which a change is considered significant. Defaults to 99.5.

    Yields:
        str: A description of the significant change detected between consecutive screenshots.
    """
    base_image_path = take_screenshot()
    if base_image_path is None:
        return
    image1_base64 = image_to_base64(base_image_path)

    try:
        while True:
            new_screenshot_path = take_screenshot()
            if new_screenshot_path is None:
                continue

            similarity = calculate_similarity(base_image_path, new_screenshot_path)
            print(f"Similarity: {similarity}")

            # Check if there's a substantial difference between screenshots.
            if similarity is not None and similarity < similarity_threshold:
                image2_base64 = image_to_base64(new_screenshot_path)
                description = gptv_describe(image1_base64, image2_base64)
                if description:
                    yield description

                # Manage old screenshot
                if base_image_path != new_screenshot_path:
                    os.remove(base_image_path)

                # Update base_image_path for the next iteration
                base_image_path = new_screenshot_path
                image1_base64 = image2_base64

            elif similarity is None:
                logging.warning("Error in similarity calculation.")
                
            else:
                logging.info("No significant changes detected.")
                # Delete new screenshot if not substantially different
                if base_image_path != new_screenshot_path:
                    os.remove(new_screenshot_path)

            time.sleep(interval)

    finally:
        # Clean up remaining screenshot file at the end
        if os.path.isfile(base_image_path):
            os.remove(base_image_path)

# TTS function adapted from narrator.py
def tts(text, output_file='/tmp/tts_output.mp3'):
    client = OpenAI()
    response = client.audio.speech.create(
        model="tts-1-1106",
        input=text,
        voice="fable",
    )
    response.stream_to_file(output_file)
    return output_file

# Play TTS function
def play_sound(file_path):
    play_command = f'aplay {file_path}'
    subprocess.run(play_command, shell=True)


if __name__ == "__main__":
    print("Starting screenshot monitoring...")
    for description in monitor_screenshots():
        if description:
            print(f"Description: {description}")
            mp3_file = tts(description)  # Generate speech from description
            if mp3_file:
                play_sound(mp3_file)  # Play the generated speech