"""
CP1404 - Practical
Program that validates a password, then prints as asterisks
"""

minimum_length = 5
password = str(input("Enter password: "))
while len(password) < minimum_length:
    print("Invalid password")
    password = str(input("Enter password: "))
for i in range(len(password)):
    print("*", end='')
