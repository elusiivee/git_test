from enum import Enum


class Color(Enum):
    RED = "RED"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    BLUE = "BLUE"
    VIOLET = "VIOLET"


print(dir(Color))       # ['BLUE', 'GREEN', 'ORANGE', 'RED', 'VIOLET', 'YELLOW', '__class__', '__doc__', '__members__', '__module__']
print(Color.RED)        # Color.RED
print(Color.RED.name)
print(Color.RED.value)



class Delivery(Enum):
    COURIER = 1
    POST = 2


class Order:
    def __init__(self, delivery: Delivery):
        self.delivery = delivery

    def order_delivery(self):
        if self.delivery == Delivery.COURIER:
            print('Courier')
        elif self.delivery == Delivery.POST:
            print('Post')
        else:
            raise ValueError('Unknown delivery type')


print(Color['RED'])

# https://pythonru.com/osnovy/perechisleniya-enum-v-python
# https://docs-python.ru/standart-library/modul-enum-perechislenija-python/
# https://habr.com/ru/company/timeweb/blog/564826/



class Delivery(Enum):
    COURIER = "Courier"
    POST = "Post"


