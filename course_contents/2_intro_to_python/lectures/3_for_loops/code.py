# -- Repeat once for each element of an iterable --

friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)


# -- Repeating something 10 times --
# You must create a "list-like" thing containing 10 elements.
# You can do this with a plain list:

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print(index)

# But Python comes with a function for that already, which is even more powerful than just doing that.

for index in range(10):
    print(index)

for index in range(5, 10):
    print(index)

for index in range(2, 20, 3):
    print(index)


# -- Using each value while you iterate --

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:  # student is a variable used for iteration
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")

# When to use?
# When you want to repeat something a defined number of times.
# For example, once for each element of a list, or even just "10 times"
