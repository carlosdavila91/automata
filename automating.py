#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:41:09 2019

@author: carlosdavila
"""


import pyautogui

print(pyautogui.size())

# La resolución es de 1279 x 799

width = pyautogui.size()[0]
height = pyautogui.size()[1]

pos1 = Point(x=355, y=403)