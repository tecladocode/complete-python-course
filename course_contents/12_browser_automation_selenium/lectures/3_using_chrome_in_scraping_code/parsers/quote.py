from selenium.webdriver.common.by import By
from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return self.parent.find_elements(By.CSS_SELECTOR, locator)
