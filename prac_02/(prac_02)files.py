"""
CP1404/CP5632 - Practical
Separate lines of code that opens, writes, reads and interacts with files
"""

# 1.
# name = str(input("Name: "))
# out_file = open(f"{name}.txt", 'w')
# print(name, file=out_file)
# out_file.close()
# 2.
# name = str(input("Name: "))
# in_file = open(f"{name}.txt", 'r')
# line = in_file.read()
# in_file.close()
# print(f"Your name is", line)
# 3.
# in_file = open("numbers.txt", 'r')
# first_line = int(in_file.readline())
# second_line = int(in_file.readline())
# in_file.close()
# print(first_line + second_line)
# 4.
# total = 0
# in_file = open("numbers.txt", 'r')
# for line in in_file:
#     number = int(line)
#     total += number
# in_file.close()
# print(total)
