"""
CP1404/CP5632 Practical
Silver Service Taxi Test Program
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi_trip = SilverServiceTaxi("Cab", 100, 2)
    taxi_trip.drive(18)
    print(taxi_trip)
    print(taxi_trip.get_fare())


main()
