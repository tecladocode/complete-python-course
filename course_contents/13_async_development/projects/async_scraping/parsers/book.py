import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} {self.price}, {self.rating} stars>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.info(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book page link...')
        locator = BookLocators.LINK_LOCATOR
        item_url = self.parent.select_one(locator).attrs['href']
        logger.info(f'Found book page link, `{item_url}`.')
        return item_url

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        logger.debug(f'Item price element found, `{item_price}`')

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))
        logger.info(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_class = next(rating_classes)

        logger.debug(f'Found rating class, `{rating_class}`.')
        logger.debug('Converting to integer for sorting.')
        rating = BookParser.RATINGS.get(rating_class)
        logger.info(f'Found book rating, `{rating}`.')
        return rating
