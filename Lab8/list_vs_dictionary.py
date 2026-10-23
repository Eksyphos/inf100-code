def key_value_getter(d):
    keylist = list(d.keys())

    print('Dictionary keys:')
    for key in keylist:
        print(key)
    
    print('\nDictionary values:')
    for key in keylist:
        print(d[key])

    print('\nDictionary keys/value:')
    for key in keylist:
        print(f'{key} {d[key]}')

def index_value_getter(a):
    length = len(a)
    
    print('List indices:')
    for i in range(length):
        print(i)
    
    print('\nList values:')
    for i in range(length):
        print(a[i])

    print('\nList indices/value:')
    for i in range(length):
        print(f'{i} {a[i]}')