def add_asterisks(string):
    wordlist = string.split(';')
    nystreng = ''
    for word in wordlist:
        word = f'*{word}*;'
        nystreng += word
    nystreng = nystreng[0:(len(nystreng)-1)]
    return nystreng

def test_add_asterisks():
    print('Testing add_asterisks...', end='')

    # Test 1
    arg = 'foo;bar;qux'
    actual = add_asterisks(arg)
    expected = '*foo*;*bar*;*qux*'
    assert expected == actual

    # Test 2
    arg = 'honey;mustard'
    actual = add_asterisks(arg)
    expected = '*honey*;*mustard*'
    assert expected == actual

    print('OK')
test_add_asterisks()