def rotate(grid,clockwise):
    newwidth = len(grid[0])
    newheight = len(grid)
    newgrid = []
    Wrange = range(newwidth)
    Hrange = range(newheight)[::-1]

    if not clockwise:
        Wrange = range(newwidth)[::-1]
        Hrange = range(newheight)

    for width in Wrange:
        newrow = []
        for height in Hrange:
            newrow.append(grid[height][width])
        newgrid.append(newrow)
    return newgrid
            
