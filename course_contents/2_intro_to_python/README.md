# Python functions

Defining a function:

```python
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
```

To call a function use the function's name followed by parentheses:

```python
# defining the function
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


# calling the function
greet()
```

## The `def` keyword

A function is defined by 4 elements:
- the `def` keyword
- the name of the function
- parentheses and
- colon

Syntax: `def name():`

## Indentation

- To write code inside the function, you must increase the indentation level with one
- When you reduce the indentation level, you exit the function

Example:

```python
def greet():
    name = input("Enter your name: ")  # inside the function
    print(f"Hello, {name}!")  # inside the function

print("Outside the function")

greet()
```

## The `return` keyword

By default, functions return `None`.

Example:

```python
def greet():
    pass  # Do nothing


# print the function's return
print(greet())  # None
```

- `pass` it's a keyword, and it means "do nothing"
- you can control what a function returns using the `return` keyword.

Example:

```python
def greet():
    name = "John Doe"
    return f"Hello, {name}!"

# printing the function
print(greet())  # John Doe
```

A function can return anything.

## Parameters

A parameter is the variable defined inside the function's definition parentheses.

Example:

```python
def greet(name):
    return f"Hello, {name}!"
```

You can have any number of parameters in a function.


## Arguments

- When a function is called, an argument is the value that is passed to it
- To call a function that has a parameter, you have to provide an argument

Example:

```python
def greet(name):
    return f"Hello, {name}!"


print(greet("John Doe"))  # Hello, John Doe!
```

The variable `name` will hold whatever it was passed inside the function's parentheses upon function call.

## Number of parameters

A function can have any number of parameters.

For example:

```python
def greet(name, age):
    return f"{name} is {age} years old!"
```

## Named arguments

If you want to be specific about what arguments you pass to parameters, use named arguments.

Example:

```python
def greet(name, age):
    return f"{name} is {age} years old!"

print(greet(name="John Doe", age=31))
```

## Default parameter values

Parameters can have default values:

```python
def greet(name="John Doe"):
    return f"Hello, {name}!"


print(greet())  # Hello, John Doe!
```

When passing an argument to the function, the default parameter value will be overwritten by the given argument.

For example:

```python
def greet(name="John Doe"):
    return f"Hello, {name}!"


print(greet("Jimmy Boy"))  # Hello, Jimmy Boy!
```

If the function has a mix of normal and default parameters, the default parameters have to be passed last.

Correct:

```python
def greet(age, name="John Doe"):
    return f"{name} is {age} years old!"


print(greet(32))
```

Incorrect:

```python
def greet(name="John Doe", age):
    return f"{name} is {age} years old!"


print(greet(32))
```

Read more about Python functions [here](https://www.teclado.com/30-days-of-python/python-30-day-12-functions).

# Python Lambda Expressions

- Lambda expressions are an alternative syntax for defining simple functions.

Syntax: `lambda arguments: expression`

- they don't have a name
- they can be given a name by assigning them to a variable name
- they're not so easy to read

Example:

```python
result = (lambda x, y: x + y)(15, 3)
```

Read more about lambda expressions and first-class functions [here](https://www.teclado.com/30-days-of-python/python-30-day-16-lambda-expressions).
