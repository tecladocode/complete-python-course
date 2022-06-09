import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            """
            Hey
            """
            if user.get('access_level') == access_level:
                return func(*args, *kwargs)

        return secure_func

    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234'


@user_has_permission('user')
def another():
    pass


# my_secure_function = user_has_permission(my_function)
print(my_function.__name__)

print(my_function('movies'))
print(another())
