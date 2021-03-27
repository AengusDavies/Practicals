"""
CP1404/CP5632 Practical
Quick Picks Program
"""

import random

NUMBER_OF_RANDOM_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Program that creates a table of random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        random_numbers = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while random_number in random_numbers:
                random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            random_numbers.append(random_number)
            random_numbers.sort()
            print(" ".join("{:2}".format(random_number) for random_number in random_numbers))


main()
