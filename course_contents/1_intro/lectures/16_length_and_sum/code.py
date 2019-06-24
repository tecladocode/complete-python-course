# Imagine you're wanting a variable that stores the grades attained by a student in their class.
# Which of these is probably not going to be a good data structure?

grades = [80, 75, 90, 100]
grades = (80, 75, 90, 100)
grades = {80, 75, 90, 100}  # This one, because of no duplicates


total = sum(grades)
length = len(grades)

average = total / length
