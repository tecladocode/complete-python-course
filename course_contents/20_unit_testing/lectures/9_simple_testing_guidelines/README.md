# Simple Testing Guidelines

Testing is a bit of an art. Identifying boundaries and equivalence classes, knowing what to look for when thinking about how to test something, to even looking at things in a different light just to break things (which then helps you fix them!).

The Simplest Test Guideline I can give you is: simple code is simpler to test. The more difficult testing becomes, the more it should tell you that the code is getting more complicated.

This is why you should favour functions over methods, and stateless over stateful, where possible.

## Limiting state

Functions are simpler to test than methods because for identical inputs, you get identical outputs.

Let's take a look at this (admittedly convoluted) example:

```python
def greet(name):
    return f"Hello, {name}"


class Greeter:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<Greeter '{self.name}'>"
    
    def greet(self):
        return f"Hello, {name}"
```

To use these two, you could do this:

```python
print(greet("Bob"))  # Hello, Bob

greeter = Greeter("Bob")
print(greeter.greet())
```

The class-based approach offers more extensibility down the line (for example, different types of greetings, or maybe even adding a `.goodbye()` method). However, it is substantially more complicated, more difficult to run, slower, and needs more tests.

The class-based approach has local state (the `self.name` property). In addition, creating an object is necessary to use the module, which means you might be creating objects all over your application if you were to use this in multiple places.

Always opt for the functional approach, unless you really need otherwise.

Here's tests for the above.

### Functional

```python
from unittest import TestCase
from greet import greet

class TestGreet(TestCase):
    def test_greets(self):
        name = "Bob"
        expected = "Hello, Bob"
        self.assertEqual(greet(name), expected)
    
    def test_greet_empty(self):
        name = ""
        expected = "Hello, "
        self.assertEqual(greet(name), expected)
    
    def test_greet_numerical(self):
        name = 25
        expected = "Hello, 25"
        self.assertEqual(greet(name), expected)
```

### Class-based

```python
from unittest import TestCase
from greet import Greeter

class TestGreet(TestCase):
    def test_greets(self):
        greeter = Greeter("Bob")
        expected = "Hello, Bob"
        self.assertEqual(greeter.greet(), expected)
    
    def test_greet_empty(self):
        greeter = Greeter("")
        expected = "Hello, "
        self.assertEqual(greeter.greet(), expected)
    
    def test_greet_numerical(self):
        greeter = Greeter(25)
        expected = "Hello, 25"
        self.assertEqual(greeter.greet(), expected)
    
    def test_greets_changing_property(self):
        greeter = Greeter("Bob")
        greeter.name = "Rolf"
        expected = "Hello, Rolf"
        self.assertEqual(greeter.greet(), expected)
    
    def test_greeter_repr(self):
        greeter = Greeter("Bob")
        expected_repr = "<Greeter 'Bob'>
        self.assertEqual(greeter.__repr__(), expected_repr)
```

This was not a particularly good example, but you'll notice this when you're working as a software developer or writing your own code. Sometimes (often!), you can do the simpler thing.

You can always re-write it later to the class-based approach when you need to. Code isn't like a building that you can't tear down. Plus, simple code is much easier to refactor and rewrite later.

Do the simple thing!