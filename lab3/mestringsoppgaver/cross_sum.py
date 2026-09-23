def cross_sum(x):
    siffer = len(str(x))
    summen = 0
    for i in range(siffer):
        tall = str(x)[i]
        summen += int(tall)
    return summen

def nth_cross_sum(n,x):
    counter = 0
    number = 0
    while counter < n:
        if cross_sum(number)==x:
            counter +=1
        number +=1
    return number-1


def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print('OK')

test_nth_cross_sum()