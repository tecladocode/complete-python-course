"""
* What is argument unpacking?
* Unpacking positional arguments
* Unpacking named arguments
* Example (below)

Given a function, like the one we just looked at to add a balance to an account:
"""

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

"""
Imagine we’ve got a list of transactions that we’ve downloaded from our bank page; and they look somewhat like this:
"""

transactions = [
  (-180.67, 'checking'),
  (-220.00, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

"""
If we now wanted to add them all to our accounts, we’d do something like this:
"""

for t in transactions:
    add_balance(t[0], t[1])

"""
What we’re doing here something very specific: *passing all elements of an iterable as arguments, one by one*.

Whenever you need to do this, there’s a shorthand in Python that we can use:
"""

for t in transactions:
    add_balance(*t)  # passes each element of t as an argument in order

"""
In section 9 we looked at this code when we were studying `map()`:
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database...

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]

"""
Instead of having a `from_dict` method in there, we could do this, using named argument unpacking:
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = [User(**data) for data in users]

"""
If our data was not in dictionary format, we could do:
"""

users = [
    ('rolf', '123'),
    ('tecladoisawesome', 'youaretoo')
]

user_objects = [User(*data) for data in users]
