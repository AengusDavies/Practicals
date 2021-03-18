"""
CP1404 - Practical
Program that asks user for password & prints as asterisks once it has met
length requirements
"""


def main():
    minimum_length = 5
    password = str(input("Enter password: "))
    password = get_password(minimum_length, password)
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end='')


def get_password(minimum_length, password):
    while len(password) < minimum_length:
        print("Invalid password")
        password = str(input("Enter password: "))
    return password


main()
