from bs4 import BeautifulSoup
import requests
from pathlib import Path
def geturls():
    string=""
    results = []
    default = Path("truecheck.txt").read_text(encoding="utf-8")
    for i in range(1,150):
        url =f"http://h26-{i}.inf105.org/"
        url2 = f"http://h26-{i}.inf105.org/about.html"
        try:
            response = requests.get(url)
        except:
            continue
        data = BeautifulSoup(response.content, "html.parser")

        if str(data) == str(default):
           url = url2
           response = requests.get(url)
           data = BeautifulSoup(response.content, "html.parser")

        try:
            title = data.title.string
        except:
            continue

        if str(title) == "404 Not Found":
            continue

        string = f'{string}\n    <li><p><a href="http://h26-{i}.inf105.org">{title}</a></p>'
        results.append(string)
        
    return string
html = geturls()
streng1 = '<!DOCTYPE html>\n<html lang="nb">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Index</title>\n  </head>\n  <body>\n    <h1>Index av Inf105 nettsider som har blitt jobbet med</h1>\n    <ul>'
streng2 = '    </ul>\n  </body>\n</html>'
index = f'{streng1}{html}{streng2}'
Path("C:\\users\\Bjarn\\.ssh\\ny_index.txt").write_text(index, encoding="utf-8")
