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
        extension = filename.split(".")[-1]
        if extension not in category_extension:
            new_category = str(input(f"What category would you like to sort {extension} files into? "))
            category_extension[extension] = new_category
            try:
                os.mkdir(new_category)
            except FileExistsError:
                pass


main()
