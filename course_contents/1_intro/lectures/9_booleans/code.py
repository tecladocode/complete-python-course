"""
A Boolean is a true/false, yes/no, one/zero value.
We can use it to make decisions.
In Python, True and False are keywords to represent these values.
"""

truthy = True
falsy = False

# ----

age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

"""
Other symbols are > and <=.

We can of course compare two variables, as below. We ask the user for a number, and check that it matches our 'secret number'.
"""

my_number = 5
user_number = int(input("Enter a number: "))

print(my_number == user_number)
print(my_number != user_number)
