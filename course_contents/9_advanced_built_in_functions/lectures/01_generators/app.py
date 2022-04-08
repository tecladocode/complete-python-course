"""
A generator in Python is a function that remembers the state it’s in, in between executions.

Let’s explain with an example. Imagine you wanted to build a list of 100 numbers, like this one:
"""


def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        nums.append(num)
        i += 1
    return nums


"""
We could use list comprehension for this and the `range()` function, but for now let’s assume that this is a cool way of doing it. We construct a list, fill it with the first 100 numbers, and then return them.

We now have 100 numbers in a list. The entire list is in your computer’s RAM memory, taking up an admittedly small amount of space.

If we wanted 10,000,000 numbers, the list would be substantially bigger. As you grow the number, the amount of memory taken up by the list also grows.

A generator is used to circumvent this problem. Instead of having a list, the first time you run the function you would get the first number (`0`). The second time you run the function you’d get `1`. Then `2`, and so on.

You have to run the function every time you want a new number, that’s why it’s called a “generator”. It generates numbers (or indeed strings, or anything else you want to generate).
"""


def hundred_numbers():
    num = 0
    while num < 100:
        yield num
        num += 1


"""
The `yield` keyword is very much like a `return`, in that it gives the value back to the caller and returns execution control to them (show this with example run). However, the next time you run the function, execution continues from the very next line inside the function, instead of from the top.

We could re-write the function as a list comprehension:
"""

hundred_numbers = [n for n in range(100)]

"""
Or indeed as a generator comprehension. This is essentially the same thing, including the `yield` statement.
"""

hundred_numbers = (n for n in range(100))
print(next(hundred_numbers))
print(next(hundred_numbers))

print(list(hundred_numbers))

"""
Notice that when we do the code snippet above, `next()` runs the function once up until the `yield` (which would give you the first value). The following `next()` runs it again, which gives you the second value. Then, turning it into a list continues and builds a list from the remaining values (that’s only 98 values left).

A few sections ago I printed out `range(10)` and it was a strange `range(0, 10)` thing. That’s a generator object!
"""
