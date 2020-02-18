"""
Here’s a common pitfall in Python that you definitely want to avoid: mutable default arguments.

Take this function:
"""

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }


a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Anne')

print(a2)

"""
What’s happened? Both Rolf and Anne are named account holders in the savings account!?

The default parameter for the `create_account` function gets evaluated when the function is defined, *not when the function is called*.

Because we’re modifying the parameter inside the function, the next time we call it the parameter is still the list that has been appended to.

There are two ways to solve this problem.

1. Don’t have `account_holders` as a default argument; or
2. Have it as a default argument, but not a mutable one.
"""

## 1: no default argument
"""
In this option we always must pass in an (empty or otherwise) list to the function call. It makes things explicit, but it means we may require a lot of empty lists being passed in there.
"""

def create_account(name: str, holder: str, account_holders: list):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }

a1 = create_account('checking', 'Rolf', [])
a2 = create_account('savings', 'Anne', [])

print(a2)

## 2: non-mutable default argument
"""
In this option we have a default value of `None`, so that we don’t have to pass a list of account holders.

If it is `None`, we initialise a new list.
"""

def create_account(name: str, holder: str, account_holders = None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders,
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Anne')

print(a2)
