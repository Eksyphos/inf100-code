def get_geometric_quotient(a):
    if 0 in a:
        return None
    if len(a) < 2:
        return 1
    k = a[1] / a[0]
    for i in range(len(a) - 1):
        if not almost_equals(a[i + 1]/a[i], k):
            return None
    return k

actual = get_geometric_quotient([3, 6, 12])