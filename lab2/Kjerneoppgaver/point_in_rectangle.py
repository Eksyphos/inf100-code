def point_in_rectangle(x1,y1,x2,y2,xp,yp):
    if (x1<=xp<=x2 or x2<=xp<=x1) and (y1<=yp<=y2 or y2<=yp<=y1):
        return True
    else:
        return False

def test_point_in_rectangle():
    print('Tester point_in_rectangle... ', end='')
    assert point_in_rectangle(0, 0, 5, 5, 3, 3) is True # Midt i
    assert point_in_rectangle(0, 5, 5, 0, 5, 3) is True # På kanten
    assert point_in_rectangle(0, 0, 5, 5, 6, 3) is False # Utenfor
    print('OK')
test_point_in_rectangle()
