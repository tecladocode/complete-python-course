import functools

user = {'username': 'jose123', 'access_level': 'guest'}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def user_has_permission(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return user_has_permission
    return decorator


@make_secure("admin")
def get_password():
        return 'admin: 1234'


@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"


# get_admin_password = make_secure(get_admin_password)

print(get_password())
print(get_dashboard_password())

user = {'username': 'anna', 'access_level': 'admin'}
print(get_password())
print(get_dashboard_password())
