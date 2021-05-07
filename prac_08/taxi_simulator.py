"""
CP1404/CP5632 Practical
Taxi Simulator Program
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            print_taxi_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            # better to ask for forgiveness than permission
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi is not None:
                current_taxi.start_fare()
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip will cost you ${trip_cost:.2f}")
                bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").lower()


def print_taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
