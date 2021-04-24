"""CP1404/CP5632 Practical - Guitar Class."""

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
