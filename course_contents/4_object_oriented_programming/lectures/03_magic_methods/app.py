"""
In a class, not all methods are the same. Python sometimes makes a distinction depending on the method name. Here’s one of these special methods:
"""


class Student:
    def __init__(self, name):
        self.name = name


"""
This method is different from other methods because it gets called automatically for you when you create a new object. For example:
"""

my_student = Student("Jose")

"""
What happens here is that a new object is created, and then the `__init__` method is called with the new object as `self` and the string you passed as `'name'`.
"""

## Other interesting special methods
### `len()`

"""
Given an *iterable* (generally a list, tuple, set, or dictionary; something you can iterate over), `len()` gives you the number of elements. For example:
"""

movies = ["Matrix", "Finding Nemo"]

print(movies.__class__)  # what's this?

count = len(movies)
print(count)  # 2

"""
We can make `len()` work on our classes too, by adding the `__len__` method:
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)


ford_garage = Garage()
ford_garage.cars.append("Fiesta")
ford_garage.cars.append("Focus")

print(len(ford_garage))

### Getting a specific item (square bracket notation)

"""
We can also use square bracket notation in our `Garage`:
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


ford_garage = Garage()
ford_garage.cars.append("Fiesta")
ford_garage.cars.append("Focus")

print(ford_garage[1])  # Focus

"""
A great thing about this is now you can iterate over the garage using a for loop. To do this you need both `__len__` and `__getitem__`:
"""

for car in ford_garage:
    print(car)

### String representation
"""
If you want to print your objects out (and sometimes during development it can be handy, as we’ll see), we can use `__repr__` and `__str__`:

* `__repr__` should be used to print out a string representing the object such that with that string you can re-create the object fully.
* `__str__` should be used when printing the object out to a user, for example—can be more descriptive or even miss out some details.
"""


class Garage:
    def __init__(self):
        self.cars = []

    def __repr__(self):
        return f"Garage {self.cars}"

    def __str__(self):
        return f"Garage with {len(self.cars)} cars"


"""
You should implement at least `__repr__`.

In order to call these methods, you can:
"""

garage = Garage()
garage.cars.append("Fiesta")
garage.cars.append("Focus")

print(garage)
print(str(garage))
print(repr(garage))


## More
"""
There are many magic “dunder” methods you can implement, including some to overload what mathematical operators do, what boolean operators do, make your objects callable, adding context managers, and more.

We’ll be learning about all this throughout the course!
"""
