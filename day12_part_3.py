
from bs4 import BeautifulSoup
html = """
<div class="product">
    <h2>Laptop</h2>
    <p class="price">$999</p>
    <a href="/product/laptop">View Product</a>
</div>
"""
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="product")
for product in products:
    title = product.h2.text
    price = product.find("p", class_="price").text
    link = product.find("a")
    url = link.get("href")
    print (f"product: {title}")
    print(f"price: {price}")
    
    
    print(f"Link :{url}")
