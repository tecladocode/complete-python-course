import logging
from app import books

logger = logging.getLogger('scraping.menu')
USER_CHOICE = '''Enter one of the following


- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


# books_generator = (item for item in books if (lambda x: x(item)))
# books_generator = filter(lambda x: x, books)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))


def menu():
    while user_input := input(USER_CHOICE):
        choice = {'b': print_best_books,
                  'c': print_cheapest_books,
                  'n': get_next_book,
                  }.get(user_input, lambda: print('Invalid Value'))
        if user_input == 'q':
            break
        choice()
    logger.debug('Terminating program...')


menu()
