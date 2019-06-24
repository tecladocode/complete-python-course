numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# -- List comprehension --

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]
# [num * 2 for num in range(5)] would be even better.

print(doubled_numbers)

# -- You can add anything to the new list --

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)


# -- This includes things like --
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]

# That is particularly useful for working with user input.
# By turning everything to lowercase, it's less likely we'll miss a match.

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"I know {friend}!")
