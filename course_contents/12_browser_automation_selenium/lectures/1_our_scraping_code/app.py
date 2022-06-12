from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    edge = webdriver.Edge(executable_path="D:/msedgedriver")
    edge.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(edge)


    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")

