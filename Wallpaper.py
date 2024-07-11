#!usr/bin/env python3

# import stuff
import os
import ctypes

path = "ENTER PATH HERE"
path = "C:\\Users\user\downloads\images"

# random functions; might need later
# useful resource: https://docs.python.org/3/library/os.html
os.fsencode()
os.get_exec_path(None)
ctypes.windll.user32.SystemParametersInfoA(0, 0, "", 0)
# os.copy_file_range(src, dst, count, offset_src=None, offset_dst=None)
