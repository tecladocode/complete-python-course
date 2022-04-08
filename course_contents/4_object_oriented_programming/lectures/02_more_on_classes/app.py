"""
Object oriented programming is used to help conceptualise the interactions between objects.

I wanted to give you a couple more examples of classes, and try to answer a few frequent questions.
"""


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year


"""
Parameter names (in `(self, name, year)`) hold the values of the arguments that we were given when the method was called: `Movie(‘The Matrix’, 1994)`.

`self.name` and `self.year` are the names of the properties of the new object we are creating. They only exist within the `self` object, so it’s totally OK to have `self.name = name`.
"""

## `self` ?

"""
It’s common in Python to call the “current object” `self`. But it doesn’t have to be that way!
"""


class Movie:
    def __init__(current_object, name, year):
        current_object.name = name
        current_object.year = year


"""
Don’t do this, for it will look very weird when someone reads your code (e.g. if you work or go to an interview), but just remember that `self` is like any other variable name—it can be anything you want. `self` is just the convention. Many editors will syntax highlight it differently because it is so common.
"""
