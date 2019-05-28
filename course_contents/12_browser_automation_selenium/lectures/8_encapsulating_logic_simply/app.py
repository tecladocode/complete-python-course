from selenium import webdriver
from pages.quotes_page import QuotesPage

author = input("Enter the author you'd like quotes from: ")
tag = input("Enter your tag: ")

chrome = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

print(page.search_for_quotes(author, tag))
