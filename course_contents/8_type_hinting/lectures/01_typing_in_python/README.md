# Type hinting in Python

In this lecture of the course, we learn about type hinting by applying type hints to the Milestone 2 Project.

## Hinting function parameters

To add type hints to function parameters, we use this syntax:

```py
def function_name(arg1: hint1 = default1, arg2: hint2 = default2):
    pass
```

The hint is optional, and so is the default value. The default value works just as it does without type hints: it gives the parameter a value if a corresponding argument is not passed.

## Hinting function return values

To hint what type of value a function will return, we use this syntax:

```py
def function_name() -> hint:
    pass
```

The `-> hint` should say what type of value the function will return. For example, if it returns an `int`, then it should say `-> int`.

## Valid type hints

You can use any of the built-in types for type hinting, such as:

- `int`
- `float`
- `str`

You can also type hint any class, and Python will know that the return value is an object of that class. For example:

```py
import datetime

def my_function() -> datetime.datetime:
    pass
```

That function should return a `datetime` object.

## Type hinting collections

Collection types such as `list` or `tuple` are also allowed. We can also add extra information, such as the type of data that will be inside the collection.

If you want to hint that a function will return a list without any further information:

```py
def function_name() -> list:
    pass
```

But if you want to specify what type of data will be inside the list:

```py
def function_name() -> list[str]:
    pass
```

## Other type hints

There's a lot more we can do with type hints, such as hint that a function may return one of two (or more!) values:

```py
from typing import Union

def function_name() -> Union[str, int]:  # may return str or int
    pass
```

You can hint the function may return an `int`, or `None`:

```py
from typing import Optional

def function_name() -> Optional[int]: # may return int, or nothing (None)
    pass
```

For more information on type hinting, the [official documentation](https://docs.python.org/3/library/typing.html#special-typing-primitives) is a great source!