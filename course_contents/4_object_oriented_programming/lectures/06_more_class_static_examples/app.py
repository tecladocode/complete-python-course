"""
Those were some terrible examples in the last section, but I just wanted to show you the syntax for these two types of method.

The `@...` is called a decorator. Those are important in Python, and we’ll be looking at creating our own later on. They are used to modify the function directly below them.
"""


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"


number = FixedFloat(18.5746)
print(number)  # 18.57

"""
We have this `FixedFloat` class that is really basic—doesn’t really do anything other than print the number out to two decimal places with the class name.

Imagine we wanted to get a new `FixedFloat` object which is a result of summing two numbers together:
"""


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)


number = FixedFloat(18.5746)
new_number = number.from_sum(19.575, 0.789)
print(new_number)

"""
This doesn’t make any sense, because we created a `FixedFloat` object (`number`), and then proceeded to call an instance method to create a new object. But that instance method didn’t use `self` at all—so really the fact that it’s a method inside a class is not very useful.

Instead, we could make it a `@staticmethod`. That way, we’re not getting `self` but we can still put the method in the class, since it is _related_ to the class:
"""


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)


static_number = FixedFloat.from_sum(19.575, 0.789)
print(static_number)

"""
That looks a bit better! Now we don’t have the useless parameter AND we don’t need to create an object before we can call the method. Win-win!

However, let’s now include some inheritance. We’ll create a `Currency` class that extends this `Float` class.
"""


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"

    # Skip defining from_sum as that's inherited


"""
We’ve defined this new class that extends the `FixedFloat ` class. It’s got an `__init__` method that calls the parent’s `__init__`, and a `__repr__` method that overrides the parents’. It doesn’t have a `from_sum` method as that’s inherited and we’ll just use the one the parent defined.
"""

euros = Euro(18.5963)
print(euros)  # <Euro €18.59>

result = Euro.from_sum(15.76, 19.905)
print(result)  # <FixedFloat 35.66>

"""
Oops! When we called the `Euro` constructor directly, we got a `Euro ` object with the symbol. But when we call `from_sum`, we got a `FixedFloat ` object. Not what we wanted!

In order to fix this, we must make the `from_sum` method return an object of the class that called it—so that:

* `FixedFloat.from_sum()` returns a `FixedFloat ` object; and
* `Euro.from_sum()` returns an `Euro` object.

`@classmethod` to the rescue! If we modify the `FixedFloat` class:
"""


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


"""
When we now call:

* `Euro.from_sum()`, `cls` is the `Euro` class.
* `FixedFloat.from_sum()`, `cls` is the `FixedFloat` class.
"""

print(Euro.from_sum(16.7565, 90))  # <Euro €106.75>
