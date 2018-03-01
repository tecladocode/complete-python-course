import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

print('Loading books list...')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books = []

start = time.time()
logger.info(f'Going through {page.page_count} pages of books...')
for page_num in range(page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    logger.info(f'Requesting {url}')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    print(f'{url} took {time.time() - page_start}')
    _books.extend(page.books)
print(f'Total took {time.time() - start}')

books = _books
