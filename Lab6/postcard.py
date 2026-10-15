from pathlib import Path

def symbol_count(path):
    mydict = {}
    content = Path(path).read_text(encoding='utf-8')
    data = content.split(None)
    for word in data:
        for letter in word:
            if letter ==' ' or letter=='\n':
                continue
            if letter in mydict:
                mydict[letter]+=1
            else:
                mydict[letter]=1
    return mydict


def test_count_letters():
    print('Tester count_letters... ', end='')
    expected = {
        'K': 2, 'j': 1, 'æ': 1, 'r': 10, 'e': 15, 'v': 3, 'n': 10, ',': 2,
        'S': 2, 'a': 3, 't': 2, 'y': 3, '.': 2, '"': 2, 'F': 2, 'i': 3,
        ':': 1, 'B': 1, 'o': 2, 'd': 2, 'J': 1, 'u': 1, "'": 1, 's': 4,
        'E': 1, 'p': 1, '!': 1, 'l': 2, 'm': 3,
    }
    actual = symbol_count('postcard.txt')
    assert 'æ' in actual, 'æ mangler, har du husket utf-8 encoding?'
    assert expected == actual
    print('OK')
test_count_letters()
