from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)
