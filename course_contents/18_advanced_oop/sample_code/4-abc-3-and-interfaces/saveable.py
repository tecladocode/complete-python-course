from abc import ABCMeta, abstractmethod

from database import Database

class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())
    
    # @classmethod (or @staticmethod, or @property)
    @abstractmethod  # @abstractmethod must always be the innermost decorator if used in conjunction with other decorators.
    def to_dict():
        pass
