from uib_inf100_graphics.event_app import run_app
from tkinter import simpledialog, messagebox

def app_started(app):
    app.keybinds ={'movedirection':[
            {
        'Up': 'north',
        'Right': 'east',
        'Down':'south',
        'Left':'west',
        },
            {
        'w': 'north',
        'd': 'east',
        's':'south',
        'a':'west',
        }
        ]}
def key_pressed(app,event):
    if event.key == 'g':
        changeup(app)
    



def changekeys(app):
    
    keychoice = simpledialog.askstring('Tast', 'Hvilken tast ønsker du?', parent=app._root)
    if len(keychoice)==1:
        app.keybinds['movedirection'][0].update({keychoice:'north'})
    else:
        app.message = 'ingen endring utført'
            

def changeup(app):
    for key in app.keybinds['movedirection'][0]:
        if app.keybinds['movedirection'][0][key] == 'north':
            del app.keybinds['movedirection'][0][key]
    changekeys(app)

def redraw_all(app,canvas):
    canvas.create_text(app.width/2,app.height/2,text=app.keybinds['movedirection'][0])



run_app(width=800,height=400,title='keybinds')
