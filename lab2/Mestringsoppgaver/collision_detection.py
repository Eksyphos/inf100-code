def rectangles_overlap(x1,y1,x2,y2, x3,y3,x4,y4):
    #regner ut nyttige variabler
    #rektangel A
    Ax1 = min(x1,x2)
    Ay1 = min(y1,y2)
    Ax2 = max(x1,x2)
    Ay2 = max(y1,y2)
    #rektangel B
    Bx1 = min(x3,x4)
    By1 = min(y3,y4)
    Bx2 = max(x3,x4)
    By2 = max(y3,y4)
    #sjekker om rektanglene er helt til venstre/høyre/over/under hverandre, fordi hvis ikke må det være overlapp.
    if Ax1<=Bx2 and Ax2>=Bx1 and Ay2<By1 and Ay1<By2:
        return False
    else:
        return True

#def test_rectangles_overlap():
    print('Tester rectangles_overlap... ', end='')
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
    print('OK')
#test_rectangles_overlap()

def circle_overlaps_rectangle(x1,y1,x2,y2,xc,yc,xr):
    #regner ut brukbare variabler for å spare hodebry senere.
    bredde = abs(x1-x2)#bruker absoluttverdi for og slippe å regne ut for hver kvadrant.
    høyde = abs(y1-y2)
    #absolutt avstand mellom midt av rektangel of midt av sirkel
    xdistance = abs((x1+x2)/2-xc)
    ydistance = abs((y1+y2)/2-yc)
    if xdistance>bredde/2+xr or ydistance>høyde/2+xr:#sjekker om sirkelen er helt utenfor
        return False
    if xdistance<=bredde/2 or ydistance<=høyde/2: #sjekker om sirkelen er innenfor rektangel+radius
        return True
    if ((xdistance-bredde/2)**2+(ydistance-høyde/2)**2)<=xr**2: #sjekker om radius av sirkelen treffer hjørnet av rektangel
        return True
    else:
        return False
    

#def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten
    print('OK')
#test_circle_overlaps_rectangle()