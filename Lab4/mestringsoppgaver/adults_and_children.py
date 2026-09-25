def remove_children(people):
    removed = 0
    for i in range(len(people)):
        i-=removed
        if people[i]["age"]<18:
            people.remove(people[i])
            removed+=1

def get_adults(people):
    adults = []
    for i in people:
        if i["age"]>=18:
            adults.append(i)
    return adults





def test_remove_children():
    print('Testing remove_children...', end=' ', flush=True)

    # Test 1
    arg = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]
    return_val = remove_children(arg)
    expected = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Liv', 'age': 37}
    ]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [
        {'name': 'Per', 'age': 8},
        {'name': 'Pål', 'age': 6},
        {'name': 'Espen', 'age': 3}
    ]
    remove_children(arg)
    expected = []
    assert expected == arg

    print('OK')

def test_get_adults():
    print('Testing get_adults...', end=' ', flush=True)

    # Test 1
    arg = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]
    return_val = get_adults(arg)
    expected = [
        {'name': 'Ole', 'age': 18},
        {'name': 'Liv', 'age': 37}
    ]
    assert return_val == expected
    assert arg == [
        {'name': 'Ole', 'age': 18},
        {'name': 'Ida', 'age': 12},
        {'name': 'Eva', 'age': 13},
        {'name': 'Liv', 'age': 37},
        {'name': 'Adam', 'age': 8}
    ]

    # Test 2
    arg = [
        {'name': 'Per', 'age': 8},
        {'name': 'Pål', 'age': 6},
        {'name': 'Espen', 'age': 3}
    ]
    actual = get_adults(arg)
    expected = []
    assert expected == actual

    print('OK')

test_remove_children()
test_get_adults()