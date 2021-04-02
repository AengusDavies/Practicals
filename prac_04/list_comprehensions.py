"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)


lowercase_full_names = []
for full_name in full_names:
    lowercase_full_names.append(full_name.lower())
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = []
for almost_number in almost_numbers:
    numbers.append(int(almost_number))
print(numbers)

greater_numbers = []
number_threshold = 9
list_of_numbers = numbers
for list_of_number in list_of_numbers:
    if list_of_number > number_threshold:
        greater_numbers = list_of_numbers.append(list_of_number)
print(greater_numbers)