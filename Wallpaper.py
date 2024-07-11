#!usr/bin/env/ python3

# import all the packages
# https://docs.python.org/3/library/ctypes.html
import ctypes
import os

try:
    # https://docs.python.org/3/library/os.html
    images = (os.listdir(r"C:\Users\User\Downloads\Images"))
    image = "C:\\Users\\User\\Downloads\\Images\\testimg.png"
    print(images)

    print(f"Number of items found in directory - {len(images)}")
    print(f"Image used - {image}")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, (image), 0)
except:
    ctypes.windll.user32.SystemParametersInfoA(20, 0, r"", 0)
