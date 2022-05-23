class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def print_info(self):
        print(f'<<{self.name}>> by {self.director}')

        # You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski')
my_movie.print_info()
