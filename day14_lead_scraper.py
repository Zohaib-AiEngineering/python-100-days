import pandas as pd
def scrape_products():
    from bs4 import BeautifulSoup
    html = """
<div class="product">
    <h2>laptop</h2>
    <p class="price">$999</p>
    <a href="/product/laptop">View Product</a>
</div>
<div class="product">
    <h2>keybord</h2>
    <p class="price">$59</p>
    <a href="/product/keybord">View Product</a>
</div>
<div class="product">
    <h2>mouse</h2>
    <p class="price">$25</p>
    <a href="/product/mouse">View Product</a>
</div>
"""
    
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("div",class_="product")
    products_data = []
    for product in products:
        title =product.h2.text.strip()
        price = product.find("p", class_="price").text.strip()
        link = product.find("a")
        url = link.get("href").strip()

        print(f"product: {title}")

        print(f"price: {price}")

        print(f"link: {url}")
        item = {
        "title": title,
        "price": price,
        "link": url
}
        products_data.append(item)
    return products_data
           
data = scrape_products()
df=pd.DataFrame(data)
df["price"] = df["price"].str.replace ("$", "", regex = False)
df["price"] = df["price"].astype(int)
print(df)
print(df.dtypes)

df.to_excel("products_day14.xlsx",index=False)