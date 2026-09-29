from uib_inf100_graphics.event_app import run_app
from face import draw_face_at
import random
def app_started(app):
    app.xc = 300
    app.yc = 300
    app.radius = 50
    app.score = 0

def mouse_pressed(app, event):
    if click_is_within_face(app, event):
        app.score +=1
    else:
        app.score -=1
    app.xc = random.randrange(app.width)
    app.yc = random.randrange(app.height)

    

def click_is_within_face(app,event):
    mouse_x = event.x
    mouse_y = event.y
    distance_from_center = ((mouse_x - app.xc)**2 + (mouse_y - app.yc)**2)**0.5
    return distance_from_center <= app.radius


def redraw_all(app,canvas):
    draw_face_at(canvas, app.xc, app.yc, app.radius)
    canvas.create_text(app.width/2, app.height -20, text = app.score)
run_app(width=600,height=600)
