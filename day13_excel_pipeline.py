import pandas as pd
from bs4 import BeautifulSoup
html = """
<div class="product">
    <h2>Laptop</h2>
    <p class="price">$999</p>
    <a href="/product/laptop">View Product</a>
</div>
<div class="product">
    <h2>keyboard</h2>
    <p class="price">$49</p>
    <a href="product/keyboard">View Product</a>
</div>
<div class=" product ">
    <h2> mouse </h2>
    <p class="price"> $25 </p>
    <a href="product/mouse">View Product</a>
</div>
<div class="product">
    <h2>monitor</h2>
    <p class="price">$199</p>
    <a href="product/monitor">View Product</a>
</div>
"""
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="product")
products_data = []
for product in products:
    title = product.h2.text.strip()
    price = product.find("p", class_="price").text.strip()
    link = product.find("a")
    url = link.get("href").strip()
    print (f"product: {title}")
    print(f"price: {price}")
    print(f"Link :{url}")
    # Loop ke andar (indentation ke saath):
    item = {
        "title": title,
        "price": price,
        "link": url
    }

    products_data.append(item)

# Loop ke bahar:
print(products_data)
df = pd.DataFrame(products_data)
df["price"] = df["price"].str.replace ("$", "", regex = False)
df["price"] = df["price"].astype(int)
print(df)
print(df.dtypes)
df.to_excel("products.xlsx", index=False)



    
    
    
