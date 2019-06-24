# Imagine you've got all your friends in a list, and you want to print it out.
friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")

# Not the prettiest, so instead you can join your friends using a ",":
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")

# Want the last one to say ", and" ?
# You'll have to wait until we cover list slicing in the next section!
