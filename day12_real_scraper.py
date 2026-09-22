import requests 
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


print("Heading:", soup.h1.text)
print("paragraph:", soup.p.text)
print("Title:",soup.title.text)