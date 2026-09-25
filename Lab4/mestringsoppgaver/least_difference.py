def smallest_absolute_difference(a):
    num = len(a)
    difference = 0
    smallestdiff = None
    for i in range(num):
        for x in range(num):
            if x==i:
                continue
            difference = abs(a[i]-a[x])
            if smallestdiff==None or difference<smallestdiff:
                smallestdiff=difference
    return smallestdiff

# def test_smallest_absolute_difference():
#     print('Tester smallest_absolute_difference... ', end='')
#     assert 1 == smallest_absolute_difference([1, 20, 4, 19, -5, 99])  # 20-19
#     assert 6 == smallest_absolute_difference([67, 19, 40, -5, 1])  # 1-(-5)
#     assert 0 == smallest_absolute_difference([2, 1, 4, 1, 5, 6])  #1-1
#     a = [50, 40, 70, 33]
#     assert 7 == smallest_absolute_difference(a)
#     assert [50, 40, 70, 33] == a  # Sjekker at funksjonen ikke er destruktiv
#     print('OK')
# test_smallest_absolute_difference()