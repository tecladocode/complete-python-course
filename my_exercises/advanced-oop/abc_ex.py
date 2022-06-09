from abc import ABCMeta, abstractmethod
"""
modify the Animal class so that:
- The `Animal` class can no longer be instantiated.
- Any subclass of `Animal` class must have a `get_favourite_food()` method
    so that the `hungry()` method can remain consistent.
remember to import proper packages here
"""


# modify the Animal class
class Animal(metaclass=ABCMeta):
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))

    @abstractmethod
    def get_favourite_food(self):
        pass