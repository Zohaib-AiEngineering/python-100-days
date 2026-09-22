from bs4 import BeautifulSoup
html = """
    <div class="product">
        <h2>Laptop</h2>
        <p class="price">$800</p>
    </div>

    <div class="product">
        <h2>Keyboard</h2>
        <p class="price">$50</p>
    </div>

    <div class="product">
        <h2>Mouse</h2>
        <p class="price">$25</p>
    </div>
    """
soup = BeautifulSoup(html,"html.parser")



# 2. Saare product divs find_all() se extract karna
products = soup.find_all("div", class_="product")    
for product in products:

    title = product.h2.text
    price = product.find("p", class_="price").text
    
    # Required output format mein print karna
    print(f"{title} - {price}")


