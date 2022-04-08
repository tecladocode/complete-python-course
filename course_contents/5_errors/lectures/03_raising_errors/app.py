"""
Let’s say you have the following code:
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        print("This method is a work-in-progress.")


"""
We’re working on a class and we’ve not yet got around to implementing the `add_car` method. Instead of printing something out, we can raise a `NotImplementedError`.
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        raise NotImplementedError("We can't add cars to the garage yet.")


Garage().add_car(
    "Fiesta"
)  # raises error, comment this line out to run the rest of the file.

"""
That way we can’t call the method and assume it works—it will now fail and crash our program. We’ll know that we’re doing something that won’t work (because it’s not implemented yet).

That’s how you `raise` an error: use the keyword and create a new error object from the class you want. All built-in errors (what we looked at in the last video) are available everywhere for you to use.

Let’s say we’re implementing the method and we want to only allow cars of type `Car`:
"""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(
                f"Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects."
            )
        self.cars.append(car)


ford_garage = Garage()
fiesta = Car("Ford", "Fiesta")

ford_garage.add_car(fiesta)  # All good
ford_garage.add_car("Fiesta")  # raises error
