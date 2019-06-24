friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne"

friends = ["Rolf", "Bob", "Anne"]

print(friends[0])  # This is called a subscript
print(friends[1])

# You can put anything you like inside a list, but it's almost always a good idea to keep it homogeneous.

friends = ["Rolf", 2, "Anne"]  # Generally a bad idea

# -- Length of a list --

friends = ["Rolf", "Anne"]
print(len(friends))  # 2

# -- Lists inside lists --
# As mentioned earlier, you can put anything inside a list—and that includes other lists.

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][1])  # 24
print(friends[1][0])  # Bob

# -- Long lists --

friends = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29],
]

# -- Adding to a list --

friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a list --

friends.remove("Bob")

print(friends)  # ["Rolf", "Anne", "Jen"]

# Remember if you have a list of lists, for example, you still need the entire thing you want to remove:

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

friends.remove(["Bob", 30])
