
######################## PAGES #######################
def draw_main_menu(canvas,width,height,buttons,info_mode):
    '''draws the main menu of the game, returns position data for buttons on main page'''
    button_size= height/16
    startY = height/4
    canvas.create_rectangle(0,0,width,height, fill='orange')
    position_data=[]
    for i in range(len(buttons)):
        new_position = draw_button(
            canvas, #canvas
            width/2, startY+(button_size+5)*i, #position
            button_size, #size
            buttons[i], 'white', #button name and color
            info_mode,)
        position_data.append(new_position)
    return position_data

def draw_settings_page(canvas,width,height,buttons,settings,info_mode):
    '''draws the settings page of the game, returns position data for buttons on settings page'''
    button_size= height/16
    startY = height/4
    canvas.create_rectangle(0,0,width,height, fill='orange')
    position_data=[]
    for i in range(len(buttons)):
        new_position = draw_button(
            canvas, #canvas
            width/2, startY+(button_size+5)*i, #position X and Y
            button_size, #size
            buttons[i], 'white', #button name and color
            info_mode, settings) #whether we are in info mode or not and current game settings
        position_data.append(new_position)
    return position_data

#################### HELPING FUNCTIONS ##########################

def draw_button(canvas, posX,posY,size,text='NaN',color='white',info_mode=False,settings=''):
    '''draws each individual button and returns its position data'''
    x1= posX-size*2
    x2= posX+size*2
    y1= posY-size/2
    y2= posY+size/2
    canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline='black')
    canvas.create_text(x1+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=text)
    canvas.create_text(x2+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=settings)
    position_data = (x1,y1,x2,y2)
    return position_data
    info_mode 