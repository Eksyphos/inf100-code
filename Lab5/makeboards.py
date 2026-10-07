
################### BOARD MAKING FUNCTIONS ##################
def makeboards(canvas,x1,y1,x2,y2,boardsize,info_mode):
    #sorts out positions for potentially multiple boards within given boundary

def makeboard():
    #makes a singular board

#################### HELPING FUNCTIONS #####################

def makerow():
    #helping function making a single row of the board

def get_colors(val):
    '''selects the color of the square based on its value'''
    if val==0:
        clr='lightgray'
    elif val>0:
        clr='orange'
    else:
        clr ='cyan'
    return clr