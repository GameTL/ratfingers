__version__ = '2.1.2'
""" 
Date: 19 Jan 2023
"""

def hello_world():
    print("This is my first pip package!")

import os
import platform

colors = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"
}

def clearterm():
    system = platform.system()
    if system == 'Windows': # for Windows
        os.system("cls")
    else: # for Unix (MacOS, Linux)
        os.system("clear")

def printclr(text="enter text", color : str = ''):
    if (color == '') or (color not in colors):
        print("please enter a color from the following list: ")
        print("""
    black:  30
    red:    31
    green:  32
    yellow: 33
    blue:   34
    magenta:35
    cyan:   36
    white:  37""")
    else:
        print("\033[1;{}m{}\033[0m".format(colors[color], text))



