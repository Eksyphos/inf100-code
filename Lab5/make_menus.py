
#################### MAIN FUNCTIONS ###################

def draw_main_menu(canvas,width,height,buttons,background,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    canvas.create_image(width/2,height/2,pil_image=background)
    
    fontsize = round(width*0.1)
    fontsize = f'arial {fontsize}'
    canvas.create_text(width/2,height*0.2,text='SNAKEGAME',font=fontsize)
    for button in buttons:
        draw_button(canvas,button,info_mode)

def draw_settings(canvas,width,height,buttons,background,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    canvas.create_image(width/2,height/2,pil_image=background)
    for key in buttons:
        for button in buttons[key]:
                draw_button(canvas,button,info_mode)

def draw_h2p(canvas,width,height,buttons,background,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    canvas.create_image(width/2,height/2,pil_image=background)
    for button in buttons:
        draw_button(canvas,button,info_mode)

def draw_keys(canvas,width,height,buttons,background,state,info_mode):
    canvas.create_rectangle(0,0,width,height, fill='orange')
    canvas.create_image(width/2,height/2,pil_image=background)
    for button in buttons:
        draw_button(canvas,button,info_mode)

################# HELP FUNCTIONS #####################

def draw_button(canvas,button,info_mode):
    '''draws each individual button and returns its position data'''
    x1,y1,x2,y2,text,func,hover,active = button
    color='black'
    thickness = 1
    fillcolor = 'white'
    if active:
        fillcolor = 'green'
        color = 'red'
    if hover:
        thickness=2

    fontsize = round(abs(y2-y1)*0.7)
    fontsize = f'arial {fontsize}'
    canvas.create_rectangle(x1,y1,x2,y2,fill=fillcolor,outline=color,width=thickness)
    canvas.create_text(x1+(abs(x1-x2)/2),y1+(abs(y1-y2)/2),text=text, font=fontsize)

    