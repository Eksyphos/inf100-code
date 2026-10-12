
boardsize = (10,10)

x,y = boardsize
newboard = []
for row in range(y):
    newrow = []
    for col in range(x):
        newrow.append(0)
    newboard.append(newrow)
    print(newrow)

