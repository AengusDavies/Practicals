"""
CP1404/CP5632 Practical
Program that stores user emails and names in a dictionary
"""


def main():
    email_and_name = {}
    email = str(input("Email: "))
    while email != "":
        name = get_name_from_email(email)
        verification = str(input("Is your name {}? (Y/n) ".format(name)))
        if verification != "Y" or verification != "n":
            name = str(input("Name: "))
        email_and_name[email] = name
        email = str(input("Email: "))
    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    name_part = email.split("@")
    email_parts = name_part.split(".")
    name = " ".join(email_parts).title()
    return name


main()
