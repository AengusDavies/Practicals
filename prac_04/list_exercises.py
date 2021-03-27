"""
CP1404/CP5632 Practical
List Exercises
"""

# 1.
# numbers = []
# for i in range(5):
#     number = int(input("Number: "))
#     numbers.append(number)
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter your username: "))
if username not in usernames:
    print("Access Denied")
    username = str(input("Enter your username: "))
print("Access granted")
