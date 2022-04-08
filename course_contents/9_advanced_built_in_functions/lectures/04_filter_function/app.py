"""
Now that we’ve got our generators, iterators, and iterables out of the way, we can start with some fun built-in functions.

Let’s start with `filter()`.

The `filter()` function is a built-in function in Python that you can call from any file or program.

It takes two arguments:

* A function; and
* An iterable (now we know what these are!)

It goes like this:
"""

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]
start_with_r = filter(lambda x: x.startswith("R"), friends)
print(start_with_r)  # generator!

print(list(start_with_r))
print(
    list(start_with_r)
)  # won't work, the generator has already gone through all its elements

"""
The function, which is the first argument, must return `True` or `False`. It must also have one parameter which is the current element of the list we’re working with.

The list we’re working with is the second argument to the `filter()` function.

The `filter()` function then returns a generator of the elements for which the first argument returns `True`.

Basically, using the `filter()` function is identical to this generator expression:
"""

(friend for friend in friends if friend.startswith("R"))

"""
Which is pretty much identical to this function:
"""


def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


"""
> Why would you use `filter()`?

If you are only working in Python and with Python developers: you wouldn’t.

However, few languages have list and generator comprehensions like the expression above. If you are working with developers familiar with constructs like `filter()`, `map()`, and `reduce()`, which are popular in other languages, it could be beneficial to use them instead.

In the further reading section of this lecture I link you to a StackOverflow answer that has a lot more reading on when you could use which.
"""
