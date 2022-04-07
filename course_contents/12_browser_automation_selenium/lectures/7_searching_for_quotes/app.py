from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.quotes_page import QuotesPage

service = Service("/usr/local/bin/chromedriver")
chrome = webdriver.Chrome(service=service)
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag: ")

page.select_tag(selected_tag)
page.search_button.click()

print(page.quotes)
