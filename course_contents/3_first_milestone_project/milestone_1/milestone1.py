import random

MOVIES = []


def main_menu():
    loop_condition = True
    while loop_condition:
        user_input = input(print_menu())
        if user_input == '4':
            loop_condition = False
        elif user_input == '3':
            print_movie(locate_movie(input('Enter Attribute'), input('Enter Attribute Value')))
        elif user_input == '2':
            add_movie(input('Enter Movie Name'), input('Enter Movie Director'), input('Enter Movie Year'))
        elif user_input == '1':
            print_movies()
        else:
            print("Bad Input try again")
    else:
        print('Bye!')


def print_menu():
    return """1. Show All Movies\n2. Add Movie\n3. Find Movie by Attribute\n4. Exit\n"""


def create_movie():
    return {'name': random.choice(['Double Impact', 'Infinite Victory', 'Fist of Surrender', 'Battle of Trouble', 'Extreme Revenge']),
            'director': random.choice(['Jordan Ângela McTaggart', 'Laxman Undine Choudhary', 'Padma Carleton Simonsen', 'Cathleen Wanjiku Niles', 'Seija Alivia Pib']),
            'year': str(random.randint(1900,2019))}


def print_movies():
    for m in MOVIES:
        print_movie(m)


def print_movie(m):
    if type(m) is dict:
        for key, value in m.items():
            print('%s: %s  ' % (key,  value), end=' ')
    else:
        print(m)
    print('')
    pass


def add_movie(name, director, year):
    MOVIES.append({'name': name, 'director': director, 'year': year})


def locate_movie(att, m):
    for movie in MOVIES:
        if movie[att] == str(m):
            return movie
    return "Movie Not Found"


def init_MOVIES():
    for i in range(5):
        MOVIES.append(create_movie())


init_MOVIES()
main_menu()
