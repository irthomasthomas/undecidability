from IPython.display import display, Image, Audio

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

