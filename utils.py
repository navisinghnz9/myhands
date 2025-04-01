import sys
import os

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:  # for macos and linux
        os.system("clear")
