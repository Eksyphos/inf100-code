from bs4 import BeautifulSoup
import requests
from pathlib import Path
from datetime import datetime

def getdata(url):
    '''Henter nettside og returnerer data i lesbart format'''
    response = requests.get(url)
    data = BeautifulSoup(response.content, "html.parser")
    return data

def make_url_list():
    '''Lager en liste med to lister i seg for url ene som ser etter index.html, andre som ser etter about.html'''
    urlLists = [[],[]]
    for i in range(150):
        url = f"http://h26-{i-1}.inf105.org/"
        url2 = f"http://h26-{i-1}.inf105.org/about.html"
        urlLists[0].append(url)
        urlLists[1].append(url2)
    return urlLists

def make_archive():
    '''Lager og returnerer en mappe til å lagre data i'''
    date = datetime.date(datetime.now())
    foldername = f"Arkiv {date}"
    directory = "C:\\Users\\Bjarn\\Documents\\Inf105-Archive"
    dirpath = f"{directory}\\{foldername}"
    if not Path(dirpath).exists():
        Path(dirpath).mkdir()
    return dirpath
    
def save_data(data,dirpath,url):
    '''Lagrer data fra nettsted til fil i arkiv'''
    #filename = url
    try:
        title = data.title.string
    except:
        title = "No Title Found"
    if "\\" in str(title) or "/" in str(title):
        title = str(title).replace("\\"," ")
        title = str(title).replace("/"," ")
    filename = f"{url},{title}"
    Path(f"{dirpath}\\{filename}").write_text(str(data), encoding="utf-8")

def main():
    '''Skraper info fra alle domenene under inf105 og lagrer det i arkivet'''
    urlliste = make_url_list()
    # urlIndex = urlliste[0]
    # urlAbout = urlliste[1]
    dirpath = make_archive()
    count = 0
    for urllist in urlliste:
        for url in urllist:
            try:
                data = getdata(url)
            except:
                print(f"{url} failed!")
                continue

            if count == 0:
                urlID = url[7:]
                urlID = urlID[:-12]
            else:
                urlID = url[7:]
                urlID = urlID[:-22]
                urlID = f"{urlID},About"
            
            save_data(data,dirpath,urlID)
        count +=1

main()