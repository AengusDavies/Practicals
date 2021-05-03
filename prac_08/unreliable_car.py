"""
CP1404/CP5632 Practical
Unreliable Car Program
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability
