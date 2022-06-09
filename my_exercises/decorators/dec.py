import functools


def decorator(func):
    @functools.wraps(func)
    def say_goodbye():
        func()
        print("Goodbye!")

    return say_goodbye


@decorator
def say_hello():
    print("Hello!")


say_hello()