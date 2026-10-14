def shopping_list_to_dict(shopping_list):
    nyliste = shopping_list.splitlines
    newdict = {}
    for item in nyliste:
        key,item = item.split(' ')
