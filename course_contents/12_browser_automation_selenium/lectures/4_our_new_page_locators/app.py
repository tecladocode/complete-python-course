from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage

service = Service("/usr/local/bin/chromedriver")
chrome = webdriver.Chrome(service=service)
chrome.get("http://quotes.toscrape.com")
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)
