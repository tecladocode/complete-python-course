def greet():
    print("Hello")
def before_and_after(func):
    print("Before...")
    print(func())
    print("After...")


before_and_after(greet)
# before_and_after(lambda: 5)
