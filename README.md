# QR Code Scanner and Link Opener

This Python script captures video from your webcam, detects QR codes in the video frames, and opens the decoded URLs in a web browser. It utilizes the OpenCV library for video capture and processing, as well as the psutil library for process management.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python
- OpenCV (`cv2` module)
- psutil

You can install these dependencies using the following commands:

```
pip install opencv-python
pip install psutil
```


## How the Script Works

1. The script initializes by capturing video from the default webcam (camera index 0) and setting the frame width and height to 1280x720 pixels.

2. It creates a QR code detector using the `cv2.QRCodeDetector()` class and initializes variables to track the last decoded text, whether a link has been opened, and the time when a link was last opened.

3. The script enters a loop where it continuously captures frames from the webcam using `cap.read()`. It then detects and decodes QR codes present in the captured frame using the QR code detector.

4. If a QR code is detected, the script draws a bounding rectangle around it and marks the center with a circle on the captured frame.

5. If the decoded text from the QR code changes, the script resets the link_opened variable to `False` to allow opening new links.

6. If a decoded URL is present and a link hasn't been opened recently, the script checks if a browser process (e.g., Chrome) is running using psutil. If a browser process is found, it opens the decoded URL in the browser, sets link_opened to `True`, and records the time the link was opened.

7. The script calculates the frames per second (FPS) of the video capture process and displays it on the frame.

8. The captured frame is displayed using `cv2.imshow()`.

9. The script listens for the 'Esc' key (key code 27) and terminates the loop when it is pressed, releasing the camera capture and closing the OpenCV windows.

## Customization

- You can adjust the `delay_between_links` variable to control the time interval (in seconds) between opening consecutive links.
- Modify the `browser_name` variable to match the name of the browser process on your system.

## Running the Script

1. Save the code in a `.py` file (e.g., `qr_code_scanner.py`).
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the command:

```python qr_code_scanner.py```

4. The webcam video stream will be displayed, and the script will attempt to detect and open QR code URLs.
5. Press the 'Esc' key to exit the script.

Please note that this script assumes that the QR codes contain valid URLs, and it relies on the proper functioning of the camera and browser processes on your system.

