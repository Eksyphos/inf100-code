from bs4 import BeautifulSoup
import requests
from pathlib import Path



def geturl(url):
    '''Henter nettside og returnerer data i lesbart format'''
    response = requests.get(url)
    data = BeautifulSoup(response.content, "html.parser")
    return data

def check_data(data):
    '''Sjekker om data er brukbar nok til å sette i listen'''
    ineligible_title = ["404 Not Found", "403 Forbidden"]
    default = Path("truecheck.txt").read_text(encoding="utf-8")
    try:
        if str(data)==default or data.title.string in ineligible_title:
            return False
        else:
            return True
    except:
        return False
    
def many_urls(urllistI,urllistA):
    urlstring = ""
    counter = -1
    for url in urllistI:
        counter+=1
        try: #checks for valid url
            data = geturl(url)
        except:
            try:
                url = urllistA[counter]
                data = geturl(url)
            except:
                continue
        
        if check_data(data):
            title = data.title.string
            urlstring = f'{urlstring}\n    <li><p><a href="{url}">{title}</a></p>'

    return urlstring

def make_urls_Index():
    '''lager en urlliste for alle inf105 domenene med index.html'''
    urllist = []
    for i in range(150):
        url = f"http://h26-{i}.inf105.org/"
        urllist.append(url)
    return urllist

def make_urls_About():
    '''lager en urlliste for alle inf105 domenene med about.html'''
    urllist = []
    for i in range(150):
        urllist.append(f"http://h26-{i}.inf105.org/about.html")
    return urllist

def Indexlist_text():
    '''Lager en ny fil "index.txt" som er klar til å bli sett over og lastet opp til nettsiden'''
    urlI = make_urls_Index()
    urlA = make_urls_About()
    html = many_urls(urlI,urlA)
    
    streng1 = '<!DOCTYPE html>\n<html lang="nb">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Index</title>\n  </head>\n  <body>\n    <h1>Index av Inf105 nettsider som har blitt jobbet med</h1>\n    <ul>'
    streng2 = '    </ul>\n  </body>\n</html>'
    index = f'{streng1}{html}{streng2}'
    Path("C:\\users\\Bjarn\\.ssh\\ny_index.txt").write_text(index, encoding="utf-8")

Indexlist_text()
Path().re