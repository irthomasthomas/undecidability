import click
import logging
import os
import sys
import io
import base64
from PIL import Image
from openai import OpenAI

devtty = "/dev/tty"
if os.path.exists(devtty):
    logging.basicConfig(filename=devtty, level=logging.DEBUG)

# Client instantiation, moved from individual functions to reduce duplication
client = OpenAI()

def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
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
    )
    result = response.choices[0].message.content
    return result

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

@cli.command()
@click.argument('image_path', type=click.Path(exists=True), required=False)
@click.argument('prompt', required=False)
@click.option('--output', type=click.Choice(['text', 'json', 'md'], case_sensitive=False), default='describe')
def describe(image_path, prompt, output):
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