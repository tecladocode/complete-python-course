# Browser automation with Selenium

The code is very similar to last section, but now we're launching a browser instead of requesting the page with Python. We will be controlling the browser, instead of just getting HTML.

The browser will work like a normal browser: it will run JavaScript, it will have cookies, etc...

## Requirements

- Selenium library
- A webdriver

### Selenium

Install `selenium` using PyCharm's preferences panel or in your virtual environment.

### Webdriver

Each of the major browsers releases a webdriver for their browser. It essentially allows other applications to interact with the browser. In this course we use the Chrome webdriver.

Download it from http://chromedriver.chromium.org/. Make sure to download the version for your browser (e.g. v74 if you're using Chrome v74).

Place the de-compressed executable, `chromedriver`, into a folder. Remember the folder's path, as you'll need it after.

## Recap

