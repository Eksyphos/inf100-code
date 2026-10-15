from pathlib import Path

def filter_wordlist(path,search_string):
    content = Path(path).read_text(encoding='utf-8')
    data = content.splitlines()
    returnlist = []
    for word in data:
        if search_string in word:
            returnlist.append(word)
    return returnlist
