from uib_inf100_graphics.event_app import run_app

def app_started(app): 
    app.messages = ['app_started']

def app_stopped(app):
    app.messages.append('app_stopped')
    print('app_stopped!')

# def key_pressed(app, event):
#     app.messages.append('key_pressed: ' + event.key)

# def key_released(app, event):
#     app.messages.append('key_released: ' + event.key)

# def mouse_pressed(app, event):
#     app.messages.append(f'mouse_pressed {(event.x, event.y)}')

# def mouse_released(app, event):
#     app.messages.append(f'mouse_released {(event.x, event.y)}')

def mouse_moved(app, event):
    app.messages.append(f'mouse_moved {(event.x, event.y)}')

# def mouse_dragged(app, event):
#     app.messages.append(f'mouse_dragged {(event.x, event.y)}')

def size_changed(app):
    app.messages.append(f'size_changed {(app.width, app.height)}')

def redraw_all(app, canvas):
    font = 'Arial 20 bold'
    canvas.create_text(app.width/2, 30, text='Brukerhendelser', font=font)
    n = min(10, len(app.messages))
    i0 = len(app.messages) - n
    for i in range(i0, len(app.messages)):
        canvas.create_text(
            app.width / 2, 
            100 + 50 * (i - i0),
            text=f'#{i}: {app.messages[i]}',
            font=font
        )

run_app(width=600, height=600)
