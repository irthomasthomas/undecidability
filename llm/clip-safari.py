import tempfile
import os
from threading import Thread
import time
try:
    import pyperclip
except ImportError:
    print("pyperclip module is not installed. Please install it using 'pip install pyperclip'.")
    exit(1)

class ClipboardMonitor:
    def __init__(self):
        self.monitoring = False
        self.output_file = ""
        self.last_clipboard_content = ""

    def toggle_monitoring(self):
        if self.monitoring:
            print("Stopping clipboard monitoring")
            print(f"File path copied to clipboard: {self.output_file}")
            pyperclip.copy(self.output_file)
            self.monitoring = False
        else:
            paper_title = input("Enter the title of the paper you're reading: ")
            if paper_title:
                self.output_file = tempfile.mktemp(suffix=".txt")
                print(f"Monitoring clipboard for paper: {paper_title}")
                print(f"Copied items will be saved to: {self.output_file}")
                with open(self.output_file, 'w') as f:
                    f.write(f"Notes for {paper_title}\n")
                self.monitoring = True
                self._start_clipboard_monitoring()
            else:
                print("No paper title provided. Exiting.")

    def _clipboard_monitoring_task(self):
        while self.monitoring:
            current_clip = pyperclip.paste()
            if current_clip != self.last_clipboard_content:
                with open(self.output_file, 'a') as f:
                    f.write("\n............\n")
                    f.write(current_clip + "\n")
                self.last_clipboard_content = current_clip
            time.sleep(1)  # Adjust based on how responsive you want the monitoring to be.

    def _start_clipboard_monitoring(self):
        thread = Thread(target=self._clipboard_monitoring_task)
        thread.daemon = True
        thread.start()

def main():
    clipboard_monitor = ClipboardMonitor()
    clipboard_monitor.toggle_monitoring()

    try:
        while clipboard_monitor.monitoring:
            input("Press Enter to stop monitoring, or Ctrl+C to exit: ")
            clipboard_monitor.toggle_monitoring()
    except KeyboardInterrupt:
        print("\nExiting.")
        clipboard_monitor.monitoring = False

if __name__ == "__main__":
    main()
