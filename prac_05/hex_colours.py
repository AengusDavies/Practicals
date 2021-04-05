"""
CP1404/CP5632 Practical
Program that interacts with a dictionary of hexadecimal
colour codes
"""

COLOUR_CODES = {"black": "#000000", "hotpink": "#ff69b4", "ivory1": "#fffff0", "turquoise": "40e0d0",
                "thistle4": "8b7b8b", "wheat": "#f5deb3", "navyblue": "#000080", "olivedrab2": "b3ee3a",
                "darksalmon": "#e9967a", "darkslategray2": "#8deeee"}

colour_name = str(input("Colour Name: ").lower())
while colour_name != "":
    print("The colour code for {} is {}". format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = str(input("Colour Name: ").lower())
