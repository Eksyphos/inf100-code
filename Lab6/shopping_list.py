from pathlib import Path

def shopping_list_to_dict(shopping_list):
    nyliste = shopping_list.splitlines()
    while '' in nyliste:
        nyliste.remove('')
    newdict = {}
    for item in nyliste:
        amount,item = item.split(' ')
        newdict.update({item:int(amount)})
    return newdict

def shopping_list_file_to_dict(path):
    content = Path(path).read_text(encoding='utf-8')
    data = shopping_list_to_dict(content)
    return data

