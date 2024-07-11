# import all the packages

# Useful resources at Python Docs
# Explains the libraries

# https://docs.python.org/3/library/ctypes.html
# https://docs.python.org/3/library/os.html

import ctypes
# import os - to access the folder at path
import os
# random to choose a random image 
# from Images folder to set as wallpaper
import random

# if images/directory does not exist
# then we will set the backgroudn to black
# using user32.SystemParametersInfoA

# try except (try catch) block to catch the errors
# just in case
try:
    # access directory, then choose a random image from folder

    # input your own path here
    images = (os.listdir(r"C:\Users\User\Downloads\Images"))
    # choose random image
    randbg = images[random.randint(0, len(images)-1)]


    # then add the path to a variable
    # input your own path here too
    image = "C:\\Users\\User\\Downloads\\Images\\" + randbg
    # for some reason, lowercase down not work, we need to replace
    # the file extension with uppercase characters

    image.replace(".png", ".PNG")
    image.replace(".jpg", ".JPG")
    image.replace(".jpeg", ".JPEG")
    # for debugging purposes, print the path of the image that we chose
    # and also the number of files found in the directory

    print(f"Number of items found in directory - {len(images)}")
    print(f"Image used - {image}")
    # and if we can, set the image to our background with this neat function
    ctypes.windll.user32.SystemParametersInfoW(20, 0, (image), 0)
except:
    # otherwise we can set the background to be black
    ctypes.windll.user32.SystemParametersInfoA(20, 0, r"", 0)
