import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')



class BookParser:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it.
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent
        # self.i = 0

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, ({self.rating} stars>)'

    # def __next__(self):
    #     if self.i < len(self.parent):
    #         current = self.parent[self.i]
    #         self.i += 1
    #         return current
    #     else:
    #         raise StopIteration()
    #
    # def __iter__(self):
    #     return self

    @property
    def name(self):
        logger.debug('Find book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Find book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Find book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string  # £51.77

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Find book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])  # None if not found
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number
