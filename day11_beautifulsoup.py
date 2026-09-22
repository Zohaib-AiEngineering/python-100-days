from bs4 import BeautifulSoup
html = """
<html>
    <div>
        <h1>My Skills</h1>
        <p>Python</p>
        <p>Pandas</p>
        <p>APIs</p>
        <p>Web Scraping</p>
    </div>
</html>
"""
soup = BeautifulSoup(html,"html.parser")
print(soup.h1.text)
print(soup.find_all("p"))

for skill in soup.find_all("p"):
    print(skill.text)


