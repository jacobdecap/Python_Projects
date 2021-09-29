#Data Class introduction

class Investor:

    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    # Instead of printing the memeory location of the object we create we can set what "repressents" or identifies an object.
    # Here we will represent an object by its name. Therefore when we print an object from this class,
    # it prints that objects name instead of its memmory location.
    def __repr__(self) -> str:
        return f"Name:{self.name}"

    # Here we are defining what the ( == ) operator does. Below two investors are the same if their names are equivalent.
    # Obviously this is not a good way but illustrates the idea.
    def __eq__(self, other):
        return self.name == other.name

    # Here we specify what the less than ( < ) does.
    def __lt__(self, other):
        return self.cash < other.cash

i1 = Investor('Jacob',24,6000)
i2 = Investor('Jon', 26, 12000)
i3 = Investor('Brad',32, 40000.32)
i4 = Investor('Jacob',24,6000)

print(i1)