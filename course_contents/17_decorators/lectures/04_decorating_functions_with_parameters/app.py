import functools

user = {"username": "jose123", "access_level": "admin"}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get("access_level") == "admin":
            return func(panel)

    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f"Password for {panel} panel is 1234."


print(my_function.__name__)

print(my_function("movies"))
