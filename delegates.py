# from typing import Callable
#
#
# def print_value(value: int) -> None:
#     print(value)
#
#
# def call_twice(f: Callable) -> None:
#     for i in range(2):
#         f()
#
#
# class Foo:
#     def __init__(self, data):
#         self.data = data
#
#     def print_value(self):
#         print(f"Value is {self.data}")
#
#     # __call__ = print_value
#
#
# foo = Foo(42)
# call_twice(foo.print_value)  # can it work? how?


class Bar:
    def run(self):
        self.go("fast")

    def go(self, msg):
        print(f"Bar.go({msg})")


class Bus:
    def __init__(self, name):
        self.name = name

    def go(self, msg):
        print(f"{self.name} is going {msg}!")


bus = Bus("Yellow bus")
Bar.run(bus)  # prints "Yellow bus is going fast!"

# https://ikriv.com/blog/?p=4790
# + add some examples from your own code
