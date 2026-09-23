import requests
from bs4 import BeautifulSoup
response =requests.get("https://quotes.toscrape.com/tag/books/")
html = """
    <div class="quote">
        ...
        <span class="text">...</span>
        <small class="author">...</small>
    
    </div>
    """
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    # 1. Loop ke inside 4 spaces (Tab) dein
    # 2. Correct HTML tags pass karein: span and small
    quote_text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    
    print("Quote:", quote_text)
    print("Author:", author)
    