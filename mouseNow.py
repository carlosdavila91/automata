#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:49:17 2019

@author: carlosdavila
"""

#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        # Make a screenshot and get the RGB values for the mouse position
        pixelColor = pyautogui.screenshot().getpixel((x, y))

        # Print the current position of the mouse and the RGB color
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print('\b' * len(positionStr), end='', flush=True)
        print(positionStr, end='')

except KeyboardInterrupt:
    print('\nDone.')
