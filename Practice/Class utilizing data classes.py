from dataclasses import dataclass, field

@dataclass(order = True)#allows for comparison operators
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float = field(repr = False) #This makes it so that their cash is not displayed when printed

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor('Jacob',24,6000)
i2 = Investor('Joba', 36, 340.35)
i3 = Investor('Jacob',24,6000.1)

mylist = [i1,i2,i3]
mylist.sort()
print(mylist)

#Very intresting right! The @dataclass line makes the == operator possible!
#Moreover, if you need to overwrite the operator you can do that as well!