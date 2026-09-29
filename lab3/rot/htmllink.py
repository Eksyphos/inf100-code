from bs4 import BeautifulSoup
import requests
from pathlib import Path
def geturls():
    string=""
    results = []
    ineligible_title = ["404 Not Found", "403 Forbidden"]
    default = Path("truecheck.txt").read_text(encoding="utf-8")
    for i in range(150):
        url =f"http://h26-{i}.inf105.org/"
        url2 = f"http://h26-{i}.inf105.org/about.html"
        try:
            response = requests.get(url)
            data = BeautifulSoup(response.content, "html.parser")
            title = data.title.string
        except:
            response = None

        if response == None or str(title) in ineligible_title or str(data) == str(default):
            try:
                url = url2
                response = requests.get(url2)
                data = BeautifulSoup(response.content, "html.parser")
                title = data.title.string
            except:
                continue    

        if str(title) in ineligible_title or str(data) == str(default):
            continue
        
        

        string = f'{string}\n    <li><p><a href="{url}">{title}</a></p>'
        results.append(string)
        
    return string
html = geturls()
streng1 = '<!DOCTYPE html>\n<html lang="nb">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Index</title>\n  </head>\n  <body>\n    <h1>Index av Inf105 nettsider som har blitt jobbet med</h1>\n    <ul>'
streng2 = '    </ul>\n  </body>\n</html>'
index = f'{streng1}{html}{streng2}'
Path("C:\\users\\Bjarn\\.ssh\\ny_index.txt").write_text(index, encoding="utf-8")
