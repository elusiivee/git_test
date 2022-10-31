from dataclasses import dataclass
from dataclasses import make_dataclass
from enum import Enum


class Sex(Enum):
    MALE = "male"
    FEMALE = "female"


@dataclass
class Person:
    name: str
    age: int
    sex: Sex

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


x = Person("Petya", 43, "male")
y = Person("Petya", 43, "male")

print(x, y)
print(x.name, y.name)
print(x == y)
