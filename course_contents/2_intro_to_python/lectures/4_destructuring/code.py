# Given a tuple or list:
currencies = 0.8, 1.2
usd, eur = currencies

# -- Destructuring in a loop --
# If you've got a list of lists, such as friend names and ages, you can destructure
# in a loop like this:

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:  # for friend in friends first
    print(f"{name} is {age} years old.")
