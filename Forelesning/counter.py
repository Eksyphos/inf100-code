from uib_inf100_graphics.event_app import run_app
from face import draw_face_at

def app_started(app):
    #app started kjører en gang når programmet starter
    #hensikten er å opprette variabler
    app.counter = 0

def key_pressed(app, event):
    #key press kalles hver gang en "event", eg. keypress, skjer
    app.counter +=1

def redraw_all(app, canvas):
    draw_face_at(canvas,300,300,50)
    canvas.create_text(300,500, text=app.counter, font="arial 30")




run_app(width=600,height=600)
