"""
The `map()` function is used to take an iterable and output a new iterable where each element has been modified according to some function.

For example, this `map()`:
"""

friends = ["Rolf", "Charlie", "Anna"]
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)

print(list(friends_lower))

"""
This of course could be written (arguably better / more pythonically) as a list or generator comprehension:
"""

friends_lower = [friend.lower() for friend in friends]

friends_lower = (friend.lower() for friend in friends)

"""
However there is something to be said for using `map()` and *not* creating the useless `friend` variable that you need to create for list comprehension.

I still think list comprehension is more pythonic and more readable.

However, if you already have the function you’re going to use defined, `map()` may not be such bad a choice. Here’s an example:
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])


# imagine these users are coming from a database...

users = [
    {"username": "rolf", "password": "123"},
    {"username": "tecladoisawesome", "password": "youaretoo"},
]

user_objects = map(User.from_dict, users)

"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]

"""
Although of course, using dictionary unpacking everything would be made much simpler… More on that in a coming section!
"""
