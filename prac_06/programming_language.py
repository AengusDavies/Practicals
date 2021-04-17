"""CP1404/CP5632 Practical - Programming Language."""


class ProgrammingLanguage:
    """Represent programming language information"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.year = year
        self.reflection = reflection

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"


def print_dynamic_languages():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    print_dynamic_languages()
