
################### BOARD MAKING FUNCTIONS ##################
def makeboards(boardsize,amount,info_mode):
    newboards = []
    for i in range(amount):
        newboards.append(makeboard(boardsize,info_mode))
        newboards[i]
    return newboards

def makeboard(boardsize,info_mode):
    x,y = boardsize
    newboard = []
    for row in range(y):
        newrow = []
        newrow.append(0)*x
        newboard.append(newrow)

#################### HELPING FUNCTIONS #####################

def makerow():
    #helping function making a single row of the board
    a=0
