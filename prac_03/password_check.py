"""
CP1404 - Practical
Program that asks user for password & prints as asterisks once it has met
length requirements
"""


def main():
    minimum_length = 5
    password = str(input("Enter password: "))
    password = validate_password(minimum_length, password)
    print_asterisks(password)


def print_asterisks(password):
    """Prints asterisks based on password length"""
    for i in range(len(password)):
        print("*", end='')


def validate_password(minimum_length, password):
    """Validates given password"""
    while len(password) < minimum_length:
        print("Invalid password")
        password = str(input("Enter password: "))
    return password


main()
