# AutoClicker-Image-Detector 🖱️🖼️

A lightweight Python script that uses `pyautogui` and `keyboard` to detect a specific image on the screen and automatically clicks on it. Ideal for automating repetitive tasks involving UI elements, game interactions, or GUI buttons.

## 🚀 Features

- Scans the screen for a specific image
- Automatically clicks on the image when found
- Allows graceful exit by pressing the `q` key
- Includes error handling and detailed debug logs


## 🛠️ Requirements
- target_image.png placed in the same folder as the script.
- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/)
- [keyboard](https://pypi.org/project/keyboard/)
- [pillow](https://pypi.org/project/Pillow/)  *(pyautogui dependency)*


Install the dependencies with:

```bash
pip install pyautogui keyboard pillow
```

Add Your Image
Place the image you want to detect in the same folder and update the image path in the script:
```
IMAGE_PATH = r'target_image.png'
```

## Run the Script
After installing all the library run the script:
```bash
python click.py


