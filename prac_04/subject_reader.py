"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)


def print_data(data_lists):
    """Print the acquired data"""
    for data_list in data_lists:
        subject_name = data_list[0]
        lecturer_name = data_list[1]
        number_of_students = data_list[2]
        print("{} is taught by {} and has {} students".format(subject_name, lecturer_name, number_of_students))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_lists = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data_lists.append(parts)
        print("----------")
    input_file.close()
    return data_lists


main()
