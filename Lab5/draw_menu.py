
def app_started(app):
    app.scale = 10

def draw_menu(canvas, list,width,height):
    '''draws the main menu of snakegame, provide a list of button names to make and the width and height of the window'''
    mainmenu = list #buttons
    #canvas.create_rectangle(0,0,app.width,app.height, Fill='beige') #background
    button_size= height/16
    startY = height/4
    canvas.create_rectangle(0,0,width,height, fill='orange')
    for button in range(len(mainmenu)):
        draw_button(canvas,width/2,startY+(button_size+5)*button,button_size,mainmenu[button],'white')
        

def draw_settings(app, canvas):
    settings = ['Game speed', 'Board Size', 'Game Mode', 'Keybinds', 'Reset Settings']#buttons
    button_size= app.height/16
    startY = app.height/4
    for button in range(len(settings)):
        draw_button(canvas,app.width/2,startY+(button_size+5)*button,button_size,settings[button],'white')



def draw_button(canvas, posX,posY,size,text='NaN',color='white'):
    '''draws each individual button'''
    x1= posX-size*2
    x2= posX+size*2
    y1= posY-size/2
    y2= posY+size/2
    canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline='black')
    canvas.create_text(x1+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=text)

def redraw_all(app, canvas):
    draw_menu(app,canvas)

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=400, title='Snake')
