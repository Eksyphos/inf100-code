def count_xs(s):
    count = str(s).count("x")
    return count

def count_sxs(s):
    count = 0
    for i in s:
        if i == "x":
            count +=1
    return count

def test_count_xs():
    print('Tester count_xs... ', end='')
    assert 0 == count_xs('foo bar hei')
    assert 1 == count_xs('x')
    assert 4 == count_xs('xxCoolDragonSlayer99xx')
    print('OK')

test_count_xs()

