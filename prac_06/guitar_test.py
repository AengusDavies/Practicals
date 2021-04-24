"""CP1404/CP5632 Practical - Guitar Testing Program."""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1050.60)

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 95, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 8, other.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


main()
