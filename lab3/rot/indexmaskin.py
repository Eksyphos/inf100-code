from bs4 import BeautifulSoup
import requests
from pathlib import Path

url =f"http://h26-1.inf105.org/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.string)
print(soup)
soup=str(soup)
Path("truecheck.txt").write_text(soup, encoding="utf-8")