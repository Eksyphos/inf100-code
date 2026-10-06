from uib_inf100_graphics import run_app
from face import draw_face_at
from random import randrange

def app_started(app):
    app.timer_delay =1000//60 #kjør timer fired 60 ganger i sekundet
    app.player = {
        'x' : app.width/2,
        'y' : app.height-50,
        'radius' : 40
    }
    app.apple = [
        {
        'radius' : randrange(15,25),
        'x' : randrange(0,app.width),
        'y' : randrange(-50,-10),
        'speed' : randrange(1,10)
        },
        {
        'radius' : randrange(15,25),
        'x' : randrange(0,app.width),
        'y' : randrange(-50,-10),
        'speed' : randrange(1,10)
        }
    ]
    app.pressed_keys = []
    app.apples_success = 0
    app.apples_failed = 0

def key_pressed(app,event):
    app.pressed_keys.append(event.key)

def key_released(app,event):
    while event.key in app.pressed_keys:
        app.pressed_keys.remove(event.key)

def timer_fired(app):
    new_apple(app)
    if 'Left' in app.pressed_keys:
        if app.player['x']>0+app.player['radius']:
            app.player['x'] -=10
    if 'Right' in app.pressed_keys:
        if app.player['x']<app.width-app.player['radius']:
            app.player['x'] +=10
    for i in range(len(app.apple)):
        app.apple[i]['y']+=5*(1+app.apple[i]['speed']/10)
    nyliste = []
    for eple in app.apple:
        if caught_apple(app,eple):
            continue
        elif app.height - app.apple[i]['y'] <eple['radius']:
            app.apples_failed += 1
        else:
            nyliste.append(eple)
    app.apple=nyliste

def redraw_all(app, canvas):
    #face
    draw_face_at(canvas, app.player['x'], app.player['y'], app.player['radius'])
    #apple
    for apple in app.apple:
        draw_apple(canvas, apple)
    canvas.create_text(
        app.width/2, 15, 
        text=f'caught apples = {app.apples_success} \nmissed apples = {app.apples_failed}\nexisting apples = {len(app.apple)}', 
        font="arial 10"
        )

def new_apple(app):
    number = randrange(1,50)
    if number == 1 or len(app.apple)<2:
        newapple = {
                'radius' : randrange(15,25),
                'x' : randrange(0,app.width),
                'y' : randrange(-50,-10),
                'speed' : randrange(1,10)
                }
        app.apple.append(newapple)
    
def caught_apple(app,apple):
    if apple['y']>app.height-app.player['radius']*2 and abs(apple['x']-app.player['x'])<app.player['radius']+apple['radius']:
        app.apples_success +=1
        return True
    else:
        return False

def draw_apple(canvas,apple):
    x_lft = apple['x'] - apple['radius']
    x_rgt = apple['x'] + apple['radius']
    y_top = apple['y'] - apple['radius']
    y_bot = apple['y'] + apple['radius']
    canvas.create_oval(x_lft,y_top,x_rgt,y_bot, fill='red')

run_app(width=800,height=800,title='Eplesamleren')