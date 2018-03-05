from animal import Animal


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def num_legs(self):
        return 4