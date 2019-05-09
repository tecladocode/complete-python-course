import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'
    item_name = soup.select_one(locator).attrs['title']
    return item_name


def find_item_page_link():
    locator = 'article.product_pod h3 a'
    item_url = soup.select_one(locator).attrs['href']
    return item_url


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string

    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    return float(matcher.group(1))


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_element = soup.select_one(locator)
    classes = star_rating_element.attrs['class']
    rating_classes = filter(lambda x: x != 'star-rating', classes)
    return next(rating_classes)


print(find_item_name())
print(find_item_page_link())
print(find_item_price())
print(find_item_rating())

# You can then turn it into a dictionary or whichever
# way is easiest to store and work with:

item = {
    'name': find_item_name(),
    'link': find_item_page_link(),
    'price': find_item_price(),
    'rating': find_item_rating()
}

print(item)

# Of course you could make a class which stores this data and
# has methods to extract it, more on the 'class_html_parsing.py file!
