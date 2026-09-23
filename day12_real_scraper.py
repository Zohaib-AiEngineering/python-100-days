from bs4 import BeautifulSoup
html = """
<div class="product">
    <h2>Laptop</h2>
    <p class="price">$800</p>
    <a href="https://example.com/laptop">View Product</a>
</div>

<div class="product">
    <h2>Keyboard</h2>
    <p class="price">$50</p>
    <a href="https://example.com/keyboard">View Product</a>
</div>

<div class="product">
    <h2>Mouse</h2>
    <p class="price">$25</p>
    <a href="https://example.com/mouse">View Product</a>
</div>
"""
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div",class_="product")
print(products)
for product in products:
    title = product.h2.text
    print(title)
    price = product.find("p", "price").text
    print(price)

    link= product.find ("a")
    print(link)
    url=link.get("href")
    print(url)
