
# Automation

Here you'll be able to find some automation programs written as a didactic way of learning python.

The code for this project has been reproduced from http://automatetheboringstuff.com/

## Get the current position of the mouse in the screen and the correspondent RGB color

This tool is coded in `mouseNow.py`.

This will give you the current position of your mouse and the RGB color of the pixel itself.

### pyautogui

`pyautogui` is the main library used for this purpose. The functions and methods used are listed bellow:

* `position`: returns the position of the mouse given a certain x,y coordinates
* `screenshot`: produces a screenshot
* `getpixel`: get an RGB tuple for the color of a pixel at specific coordinates

## Automatically fill out an online form

Filling forms could get tedious some times. This tool is aimed to ease this repetitive task. As a use case, it is implemented to get an appointment for a EU citizen that wants to get his/her NIE document, although it could serve in other cases by modifying some parameters.

### Requirements

The following are necesary to run this program.

* Download latest executable geckodriver from here to run latest firefox using selenium: https://github.com/mozilla/geckodriver/releases
* On Unix systems you can do the following to append it to your system’s search path, if you’re using a bash-compatible shell:

```
export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
```
* On Windows you will need to update the Path system variable to add the full directory path to the executable geckodriver [manually](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/amp/) or [command line](https://www.windows-commandline.com/set-path-command-line/) (don't forget to restart your system after adding executable geckodriver into system PATH to take effect). The principle is the same as on Unix.

### Variables

It will be necessary to substitute the values of the following variables in the program for the form to be filled out according to the applicant's data:

* `province`
* `certificates`: the current one is set for EU members to get the NIE
* `tramit`: the current one is set for EU members to get the NIE
* `passport_number`
* `name`
