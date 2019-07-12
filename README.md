# Automation

Here you'll be able to find some automation programs written as a didactic way of learning python.

The code from this project has been reproduced from http://automatetheboringstuff.com/

## Get the current position of the mouse in the screen and the correspondant RGB color

This tool is coded in `mouseNow.py`.

This will give you the current position of your mouse and the RGB color of the pixel itself.

### pyautogui

`pyautogui` is the main library used for this purpouse. The functions and methods used are listed bellow:

* `position`: returns the position of the mouse given a certain x,y coordinates
* `screenshot`: produces a screenshot
* `getpixel`: get an RGB tuple for the color of a pixel at specific coordinates
