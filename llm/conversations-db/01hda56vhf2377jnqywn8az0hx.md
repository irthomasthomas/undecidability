**Prompt:**
Make the motion and brightness detections seperate and optional, so that I can choose to run brightness detection, or motion detection, or both.

import cv2
import numpy as np
import click


class LightningDetector:
    def __init__(self, video_file, brightness_threshold=80, motion_threshold=10000):
        self.video_file = video_file
        self.brightness_threshold = brightness_threshold
        self.motion_threshold = motion_threshold

    def calculate_brightness(self, current_frame, previous_frame):
        difference = cv2.absdiff(current_frame, previous_frame)
        brightness_diff = np.sum(difference)
        return brightness_diff

    def calculate_motion(self, prvs, next, show_motion=False):
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

        if show_motion:
            hsv = np.zeros_like(prvs)
            hsv[..., 1] = 255
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            cv2.imshow('Motion Vis', rgb)
            cv2.waitKey(1)  # Adds a small delay and also allows input, use it to quit the window
        return np.sum(mag)

    def detect_lightning(self, show_motion=False):
        cap = cv2.VideoCapture(self.video_file)

        frame_rate = cap.get(5)  # get frame rate
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Prepare video writer
        # fourcc = 'MP4V'  # This could make the system request the specific codec
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        params = [
            cv2.VIDEOWRITER_PROP_HW_ACCELERATION,
            cv2.VIDEOWRITER_PROP_HW_DEVICE,
            0,  # Change it according to your preferred device
        ]
        # out = cv2.VideoWriter('/home/thomas/Development/Projects/cv-find/tests/lightning_output.avi', -1, frame_rate, (frame_width, frame_height))

        num_frames = 0
        previous_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            num_frames += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if num_frames == 1:
                previous_frame = gray.copy()
                continue

            brightness_diff = self.calculate_brightness(gray, previous_frame)
            motion = self.calculate_motion(previous_frame, gray, show_motion)
            lightning_frames = []
            if brightness_diff > self.brightness_threshold:
                filename = "flash_detected"
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                # lightning_frames.append(timestamp)
                cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)
            elif motion > self.motion_threshold:
                filename = "motion_detected"
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                # lightning_frames.append(timestamp)
                cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)

            previous_frame = gray.copy()

        cap.release()
        # out.release()
        cv2.destroyAllWindows()

@click.command()
@click.option('--video_file', type=click.Path(exists=True), required=True, help='Path to your video file.')
@click.option('--brightness_threshold', type=int, default=80, help='Brightness threshold value.')
@click.option('--motion_threshold', type=int, default=10000, help='Motion threshold value.')
@click.option('--show_motion', is_flag=True, default=False, help='Show motion or not.')

def main(video_file, brightness_threshold, motion_threshold, show_motion):
    ld = LightningDetector(video_file, brightness_threshold, motion_threshold)
    ld.detect_lightning(show_motion)


if __name__ == "__main__":
    main()

**Response:**
Here's how you can make both functions optional:

```python
class LightningDetector:
    def __init__(self, video_file, brightness_threshold=80, motion_threshold=10000, detect_brightness=True, detect_motion=True):
        self.video_file = video_file
        self.brightness_threshold = brightness_threshold
        self.motion_threshold = motion_threshold
        self.detect_brightness = detect_brightness
        self.detect_motion = detect_motion

    # ... rest of your class methods remain the same

    def detect_lightning(self, show_motion=False):
        # ... starting of your method remains the same

            if self.detect_brightness:
                brightness_diff = self.calculate_brightness(gray, previous_frame)
                if brightness_diff > self.brightness_threshold:
                    filename = "flash_detected"
                    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                    cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)

            if self.detect_motion:
                motion = self.calculate_motion(previous_frame, gray, show_motion)
                if motion > self.motion_threshold:
                    filename = "motion_detected"
                    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                    cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)

    # ... end of your method remains the same

@click.command()
@click.option('--video_file', type=click.Path(exists=True), required=True, help='Path to your video file.')
@click.option('--brightness_threshold', type=int, default=80, help='Brightness threshold value.')
@click.option('--motion_threshold', type=int, default=10000, help='Motion threshold value.')
@click.option('--detect_brightness', is_flag=True, default=True, help='Detect brightness flag.')
@click.option('--detect_motion', is_flag=True, default=True, help='Detect motion flag.')
@click.option('--show_motion', is_flag=True, default=False, help='Show motion or not.')

def main(video_file, brightness_threshold, motion_threshold, detect_brightness, detect_motion, show_motion):
    ld = LightningDetector(video_file, brightness_threshold, motion_threshold, detect_brightness, detect_motion)
    ld.detect_lightning(show_motion)

if __name__ == "__main__":
    main()
```

A couple of things to note here:
- I've added `detect_brightness` and `detect_motion` attributes to the `LightningDetector` class as well as the `click.command()` function. These can be used to turn on/off brightness and motion detection.
- Inside the `detect_lightning()` function, I've wrapped the detection and writing image part inside conditional statements checking whether we want to detect brightness and motion or not.
- In the `click.command()` function, I've added `--detect_brightness` and `--detect_motion` options to control whether to run brightness or motion detection or both.

<details><summary>Metadata</summary>

- Duration: 33060 ms
- Datetime: 2023-10-21T22:20:02.698478
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
Write the whole detect_lightning function please

**Response:**
Sure, here is your function with the modifications included:

```python
    def detect_lightning(self, show_motion=False):
        cap = cv2.VideoCapture(self.video_file)

        frame_rate = cap.get(5)  # get frame rate
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Prepare video writer
        # fourcc = 'MP4V'  # This could make the system request the specific codec
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        params = [
            cv2.VIDEOWRITER_PROP_HW_ACCELERATION,
            cv2.VIDEOWRITER_PROP_HW_DEVICE,
            0,  # Change it according to your preferred device
        ]
        # out = cv2.VideoWriter('/home/thomas/Development/Projects/cv-find/tests/lightning_output.avi', -1, frame_rate, (frame_width, frame_height))

        num_frames = 0
        previous_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            num_frames += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if num_frames == 1:
                previous_frame = gray.copy()
                continue

            if self.detect_brightness:
                brightness_diff = self.calculate_brightness(gray, previous_frame)
                if brightness_diff > self.brightness_threshold:
                    filename = "flash_detected"
                    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                    cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)

            if self.detect_motion:
                motion = self.calculate_motion(previous_frame, gray, show_motion)
                if motion > self.motion_threshold:
                    filename = "motion_detected"
                    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                    cv2.imwrite(f"/home/thomas/Development/Projects/cv-find/tests/output/{filename}_{timestamp}.png", frame)

            previous_frame = gray.copy()

        cap.release()
        cv2.destroyAllWindows()
```

<details><summary>Metadata</summary>

- Duration: 28007 ms
- Datetime: 2023-10-21T22:25:55.320704
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

