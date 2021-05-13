"""
CP1404/CP5632 Practical
File Sorting - First Iteration
"""

import os
import shutil


def main():
    try:
        os.mkdir("FilesToSort")
    except FileExistsError:
        pass
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = filename.split(".")[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        file_addition = f"{filename}/{extension}"
        os.rename(filename, file_addition)
        shutil.move(filename, extension)


main()
