"""
CP1404/CP5632 Practical
Unreliable Car Test Program
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    great_car = UnreliableCar("Very Good", 100, 96)
    good_car = UnreliableCar("Somewhat Good", 100, 69)
    terrible_car = UnreliableCar("Trash", 100, 5)

    for i in range(1, 20):
        print("Will attempt to drive {}km: ".format(i))
        print("{:14} drove {:3}km.".format(great_car.name, great_car.drive(i)))
        print("{:14} drove {:3}km.".format(good_car.name, good_car.drive(i)))
        print("{:14} drove {:3}km.".format(terrible_car.name, terrible_car.drive(i)))
    print(great_car)
    print(good_car)
    print(terrible_car)


main()
