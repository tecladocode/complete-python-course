from abc import ABCMeta, abstractmethod

from database import Database

class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())
    
    @abstractmethod
    def to_dict():
        pass
