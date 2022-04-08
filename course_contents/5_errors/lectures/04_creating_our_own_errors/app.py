"""
Sometimes it can be useful to create and raise errors with names we define, as opposed to only using the built-in errors.

If we want to create a custom error, we can do so very easily by subclassing the `Exception` class:
"""


class MyCustomError(Exception):
    pass


"""
The `pass` keyword just means “nothing here”. It is required because Python expects there to be an indented block after a colon, so we must at least have _something_ so Python can see the indentation.

This `MyCustomError` class just inherits everything from `Exception`, which means it behaves just like any other error.
"""

raise MyCustomError("A message describing the error")

"""
You can of course also create custom errors that have more than just the base `Exception` functionality. For example if you wanted to include an error code in your errors, you could do this:
"""


class MyErrorWithCode(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


## Docstrings
"""
Docstrings in Python are just strings that are commonly used to describe what a class or function does or when it should be used.

A docstring has this format:
"""

"""
Your docstring goes here.
"""

"""
It so happens that in Python the triple-quotation mark is a *multi-line string*. You can use it instead of a normal string anywhere, if you want multiple lines.

But back to docstrings! We can add a docstring to our exception to explain when it should be used:
"""


class MyErrorWithCode(Exception):
    """Exception raised when a specific error code is needed."""

    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


"""
Notice how here the multi-line string is in one line; and that’s OK. We could put it into multiple lines if we want to.
"""
