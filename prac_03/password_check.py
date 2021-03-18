"""
CP1404 - Practical
Program that asks user for password & prints as asterisks once it has met
length requirements
"""

minimum_length = 5

password = str(input("Enter a password: "))
while len(password) < minimum_length:
    print("Password is not long enough")
    password = str(input("Enter a password: "))
for i in range(len(password)):
    print('*', end='')
