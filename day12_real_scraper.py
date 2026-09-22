import requests 
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


links = soup.find_all("a")
print(links)
for link in links:
    print("text:", link.text)

    print("Url:",link.get("href"))
    print("-"* 20 )
    