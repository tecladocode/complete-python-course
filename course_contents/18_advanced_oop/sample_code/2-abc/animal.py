from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')
    
    def eat(self):
        print('Eating...')
    
    @abstractmethod
    def num_legs():
        pass