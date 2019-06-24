def add(x, y=3):  # x=2, y is not OK
    total = x + y
    print(total)


add(5)
add(2, 6)
add(x=3)
add(x=5, y=2)

# add(y=2)  # ERROR!
# add(x=2, 5)  # ERROR!


# -- More named arguments --

print(1, 2, 3, 4, 5, sep=" - ")  # default is " "

# You can use almost anything as a default parameter value.
# But using variables as default parameter values is discouraged, as that can introduce difficult to spot bugs

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5

# Be careful when using lists or dictionaries as default parameter values. Unlike integers or strings, these will update if you modify the original list or dictionary.

# This is due to a language feature called mutability. It's not important to understand this now, but just know that they behave differently to integers and strings behind the scenes when you change them.
