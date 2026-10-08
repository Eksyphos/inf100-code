
def draw_menu(canvas, liste,width,height,settings=''):
    '''draws the pages of snakegame, provide a list of button names to make and the width and height of the window'''
    mainmenu = liste #buttons
    if settings != '':
        settingvalue = list(settings.values())
    settinglist = [
    ['Slow','Normal','Fast'],#gamespeed
    ['Small','Medium','Large'],#boardsize
    ['Normal','WiP','WiP'], #gamemode
    ]
    button_size= height/16
    startY = height/4
    canvas.create_rectangle(0,0,width,height, fill='orange')
    buttonpositions = []
    for button in range(len(mainmenu)):
        try:
            val = settingvalue[button]
            newsetting = settinglist[button][val] #current game settings
        except:
            newsetting = ''
        pos =(draw_button(
            canvas, #canvas
            width/2, startY+(button_size+5)*button, #position
            button_size, #size
            newsetting,
            mainmenu[button], 'white')) #button name and color
        
        buttonpositions.append(pos)



def draw_button(canvas, posX,posY,size,settings='',text='NaN',color='white'):
    '''draws each individual button'''
    x1= posX-size*2
    x2= posX+size*2
    y1= posY-size/2
    y2= posY+size/2
    canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline='black')
    canvas.create_text(x1+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=text)
    canvas.create_text(x2+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=settings)

    pos = (y1,y2)
    return pos

