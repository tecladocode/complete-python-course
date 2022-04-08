"""
One of Python’s core tenets is: “ask for forgiveness, not for permission”.

Now, I know how well this works with friends and family (hint: not so well), but it works fantastically in Python. Remember this piece of code?
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
        self.cars.append(car)


"""
We would use these classes in this way:
"""

ford_garage = Garage()
fiesta = Car("Ford", "Fiesta")

ford_garage.add_car(fiesta)

"""
If we wanted to make sure that we’re only adding `Car` objects to the `Garage`, we could do this:
"""

car = Car("Ford", "Focus")
if isinstance(car, Car):
    ford_garage.add_car(car)
else:
    print("Your car was not a Car!")

"""
This is a typical structure of calling a function (in this case, the `add_car()` method:

if can_call_function():
  call_function()
else:
  say_error_happened()

What we do there is ask for permission (the `can_call_function()` statement).

Python suggests that, in many cases, our code can be made more readable by asking for forgiveness instead. Doing this (not real Python code):

try to call_function()
if failed:
  say_error_happened

Circling back to raising exceptions, we could modify the `add_car()` method to do this:
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


"""
And then we could call it like so:
"""

car = Car("Ford", "Focus")
try:
    ford_garage.add_car(car)
except TypeError:
    print("Your car was not a Car!")

"""
There are two benefits:

1. Our code reads more nicely: we try to do something that we expect to be able to do, and if we cannot then we say an error happened;
2. Our check for whether it is something we can do is now encapsulated inside the `add_car()` method; we don’t need to have an if statement every time we want to add a car.

The syntax is the `try-catch` syntax.

We try to do whatever is inside the `try` block, and then if an error happens we jump to the `except` block. We only do so for errors that match the one in the block (in this case, `TypeError` would be caught, other errors would not be caught).

We can catch multiple errors (even though our method won’t raise them, just showing you the syntax here):
"""

car = Car("Ford", "Focus")
try:
    ford_garage.add_car(car)
except TypeError:
    print("Your car was not a Car!")
except ValueError:
    print("Something was wrong with your Car...")

"""
Over the next few sections we’ll be making use of this, which is why it’s really useful to know how to use `try` and `catch`.


`try` and `catch` also have a final counterpart: `finally`.

We can use `finally` to run a block of code no matter what happens: whether or not an exception is raised. For example:
"""

car = Car("Ford", "Focus")
try:
    ford_garage.add_car(car)
except TypeError:
    print("Your car was not a Car!")
finally:
    print(f"Your garage has {len(ford_garage)} cars.")
