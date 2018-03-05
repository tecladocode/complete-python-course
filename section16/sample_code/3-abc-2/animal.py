from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print('Walking...')
    
    def eat(self):
        print('Eating...')
    
    @abstractmethod
    def num_legs():
        pass