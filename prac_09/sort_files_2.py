"""
CP1404/CP5632 Practical
File Sorting - Second Iteration
"""

import os


def main():
    category_extension = {}
    try:
        os.chdir("FilesToSort")
    except FileExistsError:
        pass
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue


main()
