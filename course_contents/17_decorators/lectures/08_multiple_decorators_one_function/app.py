"""
Taken from our Complete Python Course: https://go.tecla.do/cpc

Purely as an example, a function can have multiple decorators.

Decorators are applied from bottom to top, which means the top decorator is the first one to be evaluated when the function is executed.

In this example, we have two decorators. One checks the user's access_level, the other checks the user's username (must start with the letter 'j').
"""

import functools

# Try the various combinations below!
user = {"username": "jose123", "access_level": "admin"}
# user = {'username': 'bob', 'access_level': 'admin'}
# user = {'username': 'jose123', 'access_level': 'user'}
user = {"username": "bob", "access_level": "user"}


def user_name_starts_with_j(func):
    """
    This decorator only runs the function passed if the user's username starts with a j.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get("username").startswith("j"):
            return func(*args, **kwargs)
        else:
            print("User's username did not start with 'j'.")

    return secure_func


def user_has_permission(func):
    """
    This decorator only runs the function passed if the user's access_level is admin.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get("access_level") == "admin":
            return func(*args, **kwargs)
        else:
            print("User's access_level was not 'admin'.")

    return secure_func


@user_has_permission
@user_name_starts_with_j
def double_decorator():
    return "I ran."


print(double_decorator())

"""
When `double_decorator()` runs, this chain of "functions" runs:

user_has_permission -> user_name_starts_with_j -> double_decorator

That is because `user_name_starts_with_j` is the first decorator to be applied. It replaces `double_decorator` by the function it returns.

Then, `user_has_permission` is applied—and it replaces the function the other decorator returned by the function it returns.
"""
