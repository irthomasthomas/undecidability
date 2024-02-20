import click
import logging
import os
import sys
import io
import base64
from PIL import Image
from openai import OpenAI

# Define some global variables so I can use them in the functions below
STREAM = False
devtty = "/dev/tty"
if os.path.exists(devtty):
    logging.basicConfig(filename=devtty, level=logging.ERROR)

# Client instantiation, moved from individual functions to reduce duplication
client = OpenAI()

def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
    """Generate a completion from OpenAI's API."""
    
    #Todo: refactor to use streaming completion.
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        max_tokens=max_tokens,
        stream=STREAM,
    )
    if not STREAM:
        result = response.choices[0].message.content
        return result
    else:
        for chunk in response:
            if len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta.role:
                    print(delta.role + ": ", end="", flush=True)
                if delta.content:
                    print(delta.content, end="", flush=True)

def convert_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def generate_output(image, prompt, output_type):
    base64_image = convert_image_to_base64(image)
    system_prompts = {
        'describe': "You are GPT-4-Vision. Describe the image.",
        'json': "**IMPORTANT**: Only write output in valid JSON format. Say nothing else. Notes and comments are not allowed, except in the form of valid JSON.",
        'md': "Write a Markdown representation of the data in the image below. Say nothing else. Only reply in the form of valid Markdown."
    }
    system_prompt = system_prompts[output_type]
    try:
        result = openai_completion(prompt, system_prompt, base64_image=base64_image, model="gpt-4-vision-preview")
        return result
    except Exception as e:
        logging.error(e)
        return "Error: " + str(e)

@click.group()
def cli():
    pass

# add a streaming option.
@cli.command()
@click.argument('image_path', type=click.Path(exists=True), required=False)
@click.argument('prompt', required=False)
@click.option('--output', type=click.Choice(['text', 'json', 'md'], case_sensitive=False), default='describe')
@click.option('--stream', is_flag=True, default=False) # use this like: cat image.png | python3 GPT4-vision-toolkit.py --stream
# Todo:
    # add --screen, screenshot option.
    # add --interval, --similarity-threshold options.
    # add --monitor option.
    # add --help option.

def describe(image_path, prompt, output, stream):
    """Describe an image."""
    global STREAM # I'm sure there's a better way to do this, but I'm not sure what it is. < copilot generated this comment for me.
    STREAM = stream
    if not image_path:
        if sys.stdin.isatty():
            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
        try:
            image = Image.open(sys.stdin.buffer)
        except Exception as e:
            logging.error(f"Error reading image from stdin: {e}")
            sys.exit(1)
    else:
        try:
            image = Image.open(image_path)
        except Exception as e:
            logging.error(f"Error opening image '{image_path}': {e}")
            sys.exit(1)
    
    result = generate_output(image, prompt, output)
    click.echo(result)

if __name__ == '__main__':
    cli()