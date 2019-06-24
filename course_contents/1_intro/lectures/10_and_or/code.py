# Python has two keywords, `and` and `or`
# Here's how to use them:

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")


# -- or --

age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65

print(f"At {age}, you are usually not working: {usually_not_working}")

# That could be better re-written to:

age = int(input("Enter your age: "))
usually_working = age > 17 and age < 66  # Notice the changes to the numbers!

print(f"At {age}, you are usually working: {usually_not_working}")


# How they work internally
# `and` gives you the first value if it is falsy, otherwise gives you the second value
# `or` gives you the first value if it is truthy, otherwise gives you the second value

# How to tell if a value is "truthy" or "falsy"?
# Pass it through `bool()`.

print(bool(35))
print(bool("Rolf"))
print(bool(0))
print(bool(""))

# More examples linked in the resources section of the lecture

# --

print("" or "Rolf")  # Rolf, because "" is falsy
print("" and "Rolf")  # "", because it is falsy

print("Rolf" or "")  # "Rolf", because it is truthy
print("Rolf" and "")  # "", because "Rolf" is not falsy
