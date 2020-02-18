"""
Whenever we call a function that has parameters, we are expect to give it an equal number of arguments. We already know this:
"""

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

add_balance(500.00, 'savings')

print(accounts['savings'])  # remember, this has changed because the function mutated the dictionary!

"""
However, what you didn’t know is that you can also have default values for arguments. For example, if you wanted the account name to always be `'checking'` unless otherwise specified, you could do so.
"""

def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

"""
Then you could call the function only with an amount:
"""

add_balance(500.00)  # goes into `'checking'` by default

"""
*Important*: arguments with default values must go after arguments without default values. This would be incorrect in Python (type hinting removed to make the point):
"""

# def add_balance(name = 'checking', amount)

