
#################### MAIN FUNCTIONS ###################

def draw_main_menu(canvas,width,height,buttons,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    for button in buttons:
        draw_button(canvas,button,info_mode)

def draw_settings(canvas,width,height,buttons,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    for key in buttons:
        for button in buttons[key]:
                draw_button(canvas,button,info_mode)

def draw_h2p(canvas,width,height,buttons,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    for button in buttons:
        draw_button(canvas,button,info_mode)

################# HELP FUNCTIONS #####################

def draw_button(canvas,button,info_mode):
    '''draws each individual button and returns its position data'''
    x1,y1,x2,y2,text,func,hover = button
    if not hover:
        color='black'
        thickness = 0
    else:
        color = 'green'
        thickness = 2
    fontsize = round(abs(y2-y1)*0.7)
    fontsize = f'arial {fontsize}'
    canvas.create_rectangle(x1,y1,x2,y2,fill='white',outline=color,width=thickness)
    canvas.create_text(x1+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=text, font=fontsize)

    