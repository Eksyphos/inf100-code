def app_started(app):
    app.direction = 'east'
    app.info_mode = True
    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.snake_size = 3
    app.head_pos = (4, 3)
    app.state = 'active'

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...

def key_pressed(app, event):
    if event.key == 'i':
        app.info_mode = not app.info_mode
    if app.state == 'active':
        if event.key == 'Space':
            move_snake(app)

        if event.key == 'Up':
            app.direction = 'north'
        elif event.key == 'Down':
            app.direction = 'south'
        elif event.key == 'Right':
            app.direction = 'east'
        elif event.key == 'Left':
            app.direction = 'west'

def redraw_all(app, canvas):
    if app.state == 'active':
        draw_board(canvas,25,25,app.width-25,app.height-25,app.board,app.info_mode)
        if app.info_mode:
            canvas.create_text(
                app.width/2, 15, 
                text=f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction = \'{app.direction}\'', 
                font="arial 10")
    elif app.state == 'gameover':
        canvas.create_text(app.width/2,app.height/2, text="GAME OVER", font='arial 50')

def move_snake(app):
    head_move(app)
    if not is_legal_move(app.head_pos,app.board):
        app.state = 'gameover'
    board_update(app)
    x,y = app.head_pos
    app.board[y][x] = app.snake_size

def is_legal_move(pos, board):
    x,y = pos
    try:
        if x>len(board[0] or y>len(board)) or board[y][x]>0:
            return False
        else:
            return True
    except:
        return False


def board_update(app):
    was_apple_eaten = eat_apple(app)
    if not was_apple_eaten:
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                if app.board[row][col] >0:
                    app.board[row][col] -=1

def eat_apple(app):
    from random import randrange
    x,y = app.head_pos
    if app.board[y][x] <0:
        app.snake_size +=1
        while True:
            x = randrange(len(app.board[0]))
            y = randrange(len(app.board))
            if app.board[y][x] ==0:
                app.board[y][x] = -1
                break
            else:
                continue
        return True
    return False

def head_move(app):
    x,y = app.head_pos
    if app.direction == 'north':
        y-=1
    elif app.direction == 'south':
        y+=1
    elif app.direction == 'east':
        x +=1
    elif app.direction == 'west':
        x-=1
    #app.head_pos = x%len(app.board[0]),y%len(app.board)
    app.head_pos = x,y

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    run_app(width=500, height=400, title='Snake')
