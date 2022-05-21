movies = []


def print_movies():
    print(movies)


def add_movie():
    movies.append({'name': input('Enter Movie Name: '),
                   'director': input('Enter Director Name: '),
                   'year': input('Enter Movie Year: ')})


def by_name():
    name = input('Movie Name: ')
    print([item for item in movies if item['name'] == name])


def by_director():
    name = input('Movie Director: ')
    print([item for item in movies if item['director'] == name])


def by_year():
    name = input('Movie Year: ')
    print([item for item in movies if item['year'] == name])


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


choice = True
while choice:
    option = input("""Please Select:
    (v)iew Movies
    (a)dd Movie
    (f)ind Movie
    (q)uit
    Your Choice: """)

    choose = {
        'v': print_movies,
        'a': add_movie,
        'f': find_movie,
        'q': quit
    }

    choice = choose.get(option)

    if choice:
        choice()
    else:
        print("invalid Choice")
