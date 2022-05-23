class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("Anna", "Oxford")

"""
Imagine you’ve got a class like the above, and you want to create a similar class with some extra functionality. For example, a student that not only has marks but also a salary—a `WorkingStudent`:
"""


# class WorkingStudent:
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.marks = []
#         self.salary = salary

#     def average(self):
#         return sum(self.marks) / len(self.marks)


# rolf = WorkingStudent("Rolf", "MIT", 15.50)

"""
However you can see there’s a lot of duplication between our `Student` and `WorkingStudent` classes. Instead, we may choose to make our `WorkingStudent` extend the `Student`. It keeps all the same functionality, but we can add more.
"""


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


rolf = WorkingStudent("Rolf", "MIT", 15.50)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())

# """
# By the way, notice how the `average()` function doesn’t take any inputs other than `self`. There’s nothing in the brackets.

# In those cases, and if you think it makes sense, we can make it into a property, just like `marks` and `salary`.

# All we have to do is:
# """


# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []

#     @property
#     def average(self):
#         return sum(self.marks) / len(self.marks)


# """
# Now the `average()` function can be used as if it were a property instead of a method; like so:
# """

# jose = Student("Jose", "Stanford")
# jose.marks.append(80)
# jose.marks.append(90)
# print(jose.average)

# """
# You can do that with any method that doesn’t take any arguments. But remember, this method only returns a value calculated from the object’s properties. If you have a method that does things (e.g. save to a database or interact with other things), it can be better to stay with the brackets.

# Normally:

# * Brackets: this method does things, performs actions.
# * No brackets: this is a value (or a value calculated from existing values, in the case of `@property`).
# """
