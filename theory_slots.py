# When we know that attriubetes won't change, we can use slots to save memory

class Dots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x, self.y = x, y


class Dots2(Dots):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __dict__(self):
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.z}'


x = Dots(1, 2)
y = Dots2(1, 2, 3)

print(dir(y))
print(y.__dict__())     # {'x': 1, 'y': 2, 'z': 3}


# https://medium.com/@stephenjayakar/a-quick-dive-into-pythons-slots-72cdc2d334e
# https://stackoverflow.com/questions/472000/usage-of-slots
