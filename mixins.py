"""Mixins детально описать + крутые примеры"""
import json


# A mixin is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an is-a relationship.

class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


class Employee(JSONMixin, DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents

    def to_dict(self):
        print("Hello from overriden method")


first_employee = Employee('John', ['Python', 'C++'], ['Jane', 'Jack'])
print(first_employee.to_dict())
print(first_employee.to_json())


# https://www.pythontutorial.net/python-oop/python-mixin/
# Найти 2-3 статьи про миксины + больше примеров