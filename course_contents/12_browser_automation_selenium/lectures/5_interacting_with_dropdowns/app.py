from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.quotes_page import QuotesPage

service = Service("D:/msedgedriver.exe")
chrome = webdriver.Edge(service=service)
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)
page.sel
