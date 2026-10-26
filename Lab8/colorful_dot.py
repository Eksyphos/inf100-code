from uib_inf100_graphics import run_app

def app_started(app):
    app.timer_delay =10 #kjør timer fired 60 ganger i sekundet
    app.pressed_keys = []
    app.red = 50
    app.green = 50
    app.blue = 50
    app.pressed_keys = []
    

def redraw_all(app,canvas):
    draw_the_page(canvas,app.width,app.height,app.red,app.green,app.blue)
    canvas.create_text(app.width/2,app.height*0.1,text=f'red = {app.red},green = {}')
def key_pressed(app,event):
    app.pressed_keys.append(event.key)

def key_released(app,event):
    while event.key in app.pressed_keys:
        app.pressed_keys.remove(event.key)

def timer_fired(app):
    if 'a' in app.pressed_keys:
        if app.blue<255:
            app.blue +=1
    elif 'z' in app.pressed_keys:
        if app.blue>0:
            app.blue -=1
    elif 'Up' in app.pressed_keys:
        if app.red<255:
            app.red +=1
    elif 'Down' in app.pressed_keys:
        if app.red>0:
            app.red -=1
    elif 'Left' in app.pressed_keys:
        if app.green<255:
            app.green +=1
    elif 'Right' in app.pressed_keys:
        if app.green>0:
            app.green -=1

def draw_the_page(canvas,width,height,red,green,blue):
    
    color = rgb_to_hex(red,green,blue)
    canvas.create_oval(width*0.4,height*0.4,width*0.6,height*0.6,fill=color)

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

run_app(width=800,height=800,title='fargedott')
