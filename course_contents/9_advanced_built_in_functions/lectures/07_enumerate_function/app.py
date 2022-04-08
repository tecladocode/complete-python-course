"""
Let’s say you’ve got some code like this one:
"""

top_friends = ["Jose", "Rolf", "Anna"]

print(f"My top 1 friend is {top_friends[0]}")
print(f"My top 2 friend is {top_friends[1]}")
print(f"My top 3 friend is {top_friends[2]}")

"""
Not so good! You could do this instead:
"""

top_friends = ["Jose", "Rolf", "Anna"]
i = 0

for i in range(3):
    print(f"My top {i+1} friend is {top_friends[i]}")

"""
Or, using the `enumerate()` function, you could do:
"""

top_friends = ["Jose", "Rolf", "Anna"]

for i, friend in enumerate(top_friends):
    print(f"My top {i+1} friend is {friend}")

"""
The `enumerate()` function takes in a list and outputs a generator of `(index, element)` tuples—so that each element of the list is now accompanied by its index in the list.

Indeed, we can do this:
"""

e = enumerate(top_friends)

first_tuple = next(e)
print(first_tuple)  # prints (0, 'Jose')

"""
Remember tuple destructuring, which allows us to do this:
"""

i, friend = first_tuple  # i is 0, friend is 'Jose'

"""
And that’s how the `enumerate()` function works!
"""
