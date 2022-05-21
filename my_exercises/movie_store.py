movies = []


def view_movies():
    for movie in movies:
        print_movie(movie)


def add_movie():
    movies.append({'title': input('Enter Movie Title: '),
                   'director': input('Enter Director Name: '),
                   'year': input('Enter Movie Year: ')})


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def by_name():
    title = input('Movie Title: ')
    for movie in movies:
        if movie['title'] == title:
            print_movie(movie)


def by_director():
    director = input('Movie Director: ')
    for movie in movies:
        if movie['director'] == director:
            print_movie(movie)


def by_year():
    year = input('Movie Year: ')
    for movie in movies:
        if movie['year'] == year:
            print_movie(movie)


def find_movie():
    opt = input("""By:
    (n)ame
    (d)irector
    (y)ear
    Please Select: """)

    choose = {
        'n': by_name,
        'd': by_director,
        'y': by_year
    }

    choice = choose.get(opt)
    if choice:
        choice()
    else:
        print("Invalid Choice")


def menu():
    while True:
        option = input("""Please Select:
            (v)iew Movies
            (a)dd Movie
            (f)ind Movie
            (q)uit
            Your Choice: """)

        choose = {
            'v': view_movies,
            'a': add_movie,
            'f': find_movie,
            'q': quit
        }

        choice = choose.get(option)

        if choice:
            choice()
        else:
            print("invalid Choice")


menu()
