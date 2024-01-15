**Prompt:**
diff --git a/agents/vision/gpt4-vision-describe-image.py b/agents/vision/gpt4-vision-describe-image.py
new file mode 100644
index 0000000..c68f993
--- /dev/null
+++ b/agents/vision/gpt4-vision-describe-image.py
@@ -0,0 +1,76 @@
+import click
+import logging
+import os
+import sys
+from PIL import Image
+from openai import OpenAI
+
+# Assuming that OpenAI's GPT has a function named 'create_completion'
+# and API instantiation requires an API key.
+# Replace it with the correct function calls based on the actual library you're using.
+
+@click.group()
+def cli():
+    pass
+
+# Todo: Add a way for the user to include prompt text with the image.
+@cli.command()
+@click.argument('image_path', type=click.Path(exists=True), required=False)
+@click.argument('prompt', required=False)
+
+def describe(image_path, prompt=None):
+    '''Describes the content of an image.'''
+
+    # If no image path is provided, try to read the image from stdin
+    if not image_path:
+        if sys.stdin.isatty():
+            raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
+        image = Image.open(sys.stdin.buffer)
+    else:
+        # Open the image from the provided path
+        image = Image.open(image_path)
+    
+    description = get_image_description(image, prompt)
+    click.echo(description)
+
+def get_image_description(image, prompt=None):
+    # Replace 'OpenAI' instantiation and 'create_completion' as appropriate for your SDK
+    client = OpenAI()
+
+    # Convert image to base64 for sending to the API
+    import io
+    import base64
+    buffered = io.BytesIO()
+    image.save(buffered, format="PNG")
+    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
+    
+    try:
+        # Requesting description from OpenAI (Replace with the proper API call)
+        response = client.chat.completions.create(
+            model="gpt-4-vision-preview",
+            messages=[
+                {
+                    "role": "user",
+                    "content": [
+                        {
+                            "type": "image_url",
+                            "image_url": {
+                                "url": f"data:image/png;base64,{base64_image}"
+                            },
+                        },
+                        {
+                            "type": "text",
+                            "text": prompt or "Describe this image in fine detail. Pay special attention to new or unfamilliar terms and nomenclature. They may be extremely important in delineating what is interesting about the content.",
+                        }
+                    ],
+                },
+            ],
+            max_tokens=2000,
+        )
+        return response.choices[0] if response.choices else "No description found."
+    except Exception as e:
+        logging.error(e)
+        return "Error: " + str(e)
+
+if __name__ == '__main__':
+    cli()
\ No newline at end of file
diff --git a/agents/vision/gpt4-vision-screen-compare.py b/agents/vision/gpt4-vision-screen-compare.py
new file mode 100644
index 0000000..071eab1
--- /dev/null
+++ b/agents/vision/gpt4-vision-screen-compare.py
@@ -0,0 +1,138 @@
+import os
+import time
+import logging
+from PIL import Image, ImageChops
+import numpy as np
+import subprocess
+from datetime import datetime
+from openai import OpenAI
+
+def take_screenshot_with_ffmpeg(output_directory='/tmp'):
+    print("Taking screenshot...")
+    if not os.path.exists(output_directory):
+        os.makedirs(output_directory)
+    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
+    screenshot_filename = f'screenshot_{timestamp}.png'
+    screenshot_path = os.path.join(output_directory, screenshot_filename)
+    ffmpeg_command = f'ffmpeg -n -f x11grab -i :0.0 -vframes 1 -s $(xdpyinfo | grep dimensions | awk \'{{print $2}}\') {screenshot_path} -loglevel panic'
+    subprocess.run(ffmpeg_command, shell=True)
+    time.sleep(1)
+    print(f"Screenshot taken and stored at {screenshot_path}")
+    return screenshot_path
+
+
+def calculate_similarity(image1_path, image2_path):
+    try:
+        print(f"Calculating similarity between {image1_path} and {image2_path}...")
+        image1 = Image.open(image1_path)
+        image2 = Image.open(image2_path)
+        if image1.size != image2.size:
+            raise ValueError("Images do not have the same dimensions.")
+        diff = ImageChops.difference(image1, image2)
+        diff_array = np.array(diff)
+        total_diff = np.sum(np.abs(diff_array))
+        max_diff = diff_array.size * 255
+        similarity = ((max_diff - total_diff) / max_diff) * 100
+        print(f"Calculated similarity: {similarity}%")
+        return similarity
+    except FileNotFoundError as e:
+        logging.error(f"File not found: {e}")
+        return None
+    except Exception as e:
+        logging.error(f"Error calculating similarity: {e}")
+        return None
+    
+    
+def resize_image_for_gptv(image_path, detail='high'):
+    # Open the image
+    with Image.open(image_path) as img:
+        img_width, img_height = img.size
+        print(f"img_width: {img_width}")
+        if detail == 'low':
+            new_img = img.resize((512, 512))
+        elif detail == 'high':
+            new_width = min(768, img_width)
+            new_height = min(2000, img_height)
+            print(f"high detail - new_width: {new_width} new_height: {new_height}")
+    
+        # If the width is smaller, resize height proportionally
+        if img_width < img_height:
+            new_height = int(new_width / img_width * img_height)
+        # Otherwise, resize width proportionally
+        else:
+            new_width = int(new_height / img_height * img_width) 
+        
+        print(f"new_width: {new_width} - new_height: {new_height}")
+        new_img = img.resize((new_width, new_height))
+
+    # Save the image
+    print(image_path)
+    new_img.save(image_path)
+
+
+def gptv_describe(image1_path, image2_path):
+    print(f"Describing differences between {image1_path} and {image2_path}")
+    
+    import base64
+
+    with open(image1_path, "rb") as image_file:
+        base64_image1 = base64.b64encode(image_file.read()).decode('utf-8')
+
+    with open(image2_path, "rb") as image_file:
+        base64_image2 = base64.b64encode(image_file.read()).decode('utf-8')
+        
+    client = OpenAI()
+    response = client.chat.completions.create(
+        model="gpt-4-vision-preview",
+        messages=[
+            {
+                "role": "user",
+                "content": [
+                    {
+                        "type": "text",
+                        "text": "What are in these screenshots? Is there any difference between them?",
+                    },
+                    {
+                        "type": "image_url",
+                        "image_url": {
+                            "url": f"data:image/jpeg;base64,{base64_image1}"
+                        },
+                    },
+                    {
+                        "type": "image_url",
+                        "image_url": {
+                            "url": f"data:image/jpeg;base64,{base64_image1}"
+                        },
+                    },
+                ],
+            }
+        ],
+        max_tokens=300,
+    )
+    print(response.choices[0])
+   
+   
+def monitor_screenshots(base_image_path, interval=10, similarity_threshold=99.5):
+    while True:
+        new_screenshot_path = take_screenshot_with_ffmpeg()
+        similarity = calculate_similarity(base_image_path, new_screenshot_path)
+        if similarity is not None and similarity < similarity_threshold:
+            description = gptv_describe(base_image_path, new_screenshot_path)
+            yield description
+            base_image_path = new_screenshot_path
+        elif similarity is None:
+            logging.warning("Skipping this iteration due to error in similarity calculation.")
+        else:
+            print("No Changes, removing screenshot...")
+            os.remove(new_screenshot_path)
+        for i in range(interval, 0, -1):
+            print(i)
+            time.sleep(1)
+            
+            
+screenshot = take_screenshot_with_ffmpeg()
+print("Starting screenshot monitoring...")
+descriptions = monitor_screenshots(screenshot)
+
+for description in descriptions:
+    print(description)


**Response:**
Add new vision agent scripts for describing images and comparing screenshots

<details><summary>Metadata</summary>

- Duration: 527 ms
- Datetime: 2024-01-11T23:54:29.278062
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

