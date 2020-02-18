def greet():
    print("Hello!")

# `before_and_after` is a higher-order function. That just means it's a function which has another function as a parameter.
def before_and_after(func):  # func is a function passed
    print("Before...")
    func()
    print("After...")


# greet, not greet(). That's because we're passing the function, not the result of calling the function.
before_and_after(greet)


# Another example


movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found


find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movie = find_movie(looking_for, lambda x: x[find_by])
print(movie or 'No movies found.')

