"""
The two functions we’ll be talking about are very straightforward, but in some cases can be really useful.

The `any()` function takes an iterable and returns `True` if any of the elements in it evaluate to `True`

The `all()` function returns `True` if all the elements evaluate to `True`.

Here’s an example of when it might be useful.
"""

friends = [
    {"name": "Rolf", "location": "Washington, D.C."},
    {"name": "Anna", "location": "San Francisco"},
    {"name": "Charlie", "location": "San Francisco"},
    {"name": "Jose", "location": "San Francisco"},
]

your_location = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if friend["location"] == your_location]

if any(friends_nearby):
    print("You are not alone!")

"""
Here the contents of `friends_nearby` is a list of dictionaries—not `True` or `False`.

However, all values in Python can evaluate to either `True` or `False` if forced to.

Some values always evaluate to `False`:

* `0`
* `None`
* `[]`
* `()`
* `{}`
* `False`

All other values evaluate to `True`—so if we have a dictionary with values in it, that evaluates to `True` and the `any()` function will then return `True`.

However, if we pass it an empty list, we get `False`.
"""
