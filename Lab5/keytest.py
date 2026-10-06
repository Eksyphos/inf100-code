from uib_inf100_graphics.event_app import run_app

def app_started(app):
    app.message = 'Press any key'

def key_pressed(app, event):
    app.message = f"event.key == '{event.key}'"

def redraw_all(app, canvas):
    canvas.create_text(app.width/2, 40, text=app.message,
                       font='Arial 20 bold')
    
    key_names_text = '''\
        Here are the legal event.key names:
        * Keyboard key labels (letters, digits, punctuation)
        * Arrow directions ('Up', 'Down', 'Left', 'Right')
        * Whitespace ('Space', 'Enter', 'Tab', 'BackSpace')
        * Other commands ('Delete', 'Escape')'''

    canvas.create_text(
        app.width/2, 80,
        text=key_names_text,
        anchor="n",
        font='Arial 16'
    )

run_app(width=500, height=250)
