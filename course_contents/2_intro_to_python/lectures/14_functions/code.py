# So far we've been using functions such as `print`, `len`, and `zip`.
# But we haven't learned how to create our own functions, or even how they really work.

# Let's create our own function. The building blocks are:
# def
# the name
# brackets
# colon
# any code you want, but it must be indented if you want it to run as part of the function.


def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


# Running this does nothing, because although we have defined a function, we haven't executed it.
# We must execute the function in order for its contents to run.

greet()

# You can put as much or as little code as you want inside a function, but prefer shorter functions over longer ones.
# You'll usually be putting code that you want to reuse inside functions.

# Any variables declared inside the function are not accessible outside it.
print(name)  # ERROR!
