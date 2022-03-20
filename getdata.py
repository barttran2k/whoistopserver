from bs4 import BeautifulSoup

soup = BeautifulSoup(open("dot1.html"), "html.parser")

print(soup.prettify())