"""
So what in the heck is an iterable?

Funny you’d ask! An iterable is an object that has an `__iter__` method defined. The `__iter__` method *must return an iterator*.

Here’s an example of using our generator to make an iterable.
"""


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


"""
Now we have an iterable which uses the iterator to get the next value of the sequence it generates. We can do this:
"""

print(sum(FirstHundredIterable()))  # gives 4950

for i in FirstHundredIterable():
    print(i)

"""
Wait… I remember something about for loops. We needed an object with `__len__` and `__getitem__` defined!

How come we can use a for loop with this object that doesn’t have either of those?

Here’s something new! You can perform iteration over an iterable. An iterable either has:

* `__len__` and `__getitem__` defined; or
* An `__iter__` method that returns an iterator.

If you have either of those two, you have yourself an iterable.

---

So the `FirstHundredIterable` is returning an object of type `FirstHundredGenerator`. 

Inside `FirstHundredGenerator`, what is `self`?

(Hint: it’s an object, what is it’s type?)

(Hint hint: it’s of type `FirstHundredGenerator`).

Knowing that, we can change the generator to this:
"""


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


"""
And then we don’t need a separate iterable at all—the generator itself is now both an iterator and an iterable.
"""
