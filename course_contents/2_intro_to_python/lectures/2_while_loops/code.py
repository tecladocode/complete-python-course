# -- Infinite loop --

is_learning = True

while is_learning:
    print("You're learning!")


# -- Ending a loop with user input --

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")


# When to use?
# When you want to repeat something an undefined number of times.
# For example, until a user tells you to stop or some other condition becomes False.
