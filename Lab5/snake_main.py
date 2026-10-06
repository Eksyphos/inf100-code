
################ STARTUP #################
def app_started(app):
    '''startup variables'''
    app.timer_delay =1000
    app.direction = 'east'
    app.info_mode = False
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
    app.state = 'menu'
    app.pressed_keys = []
    app.last_move = 'east'
    app.buttonpos = {
        'menu':[
            [(87,113),(117,143),(147,173),(177,203),(207,233)],
            ['Start Game', 'Settings', 'How To Play', 'Leaderboard','test']
        ]
        }

def timer_fired(app):
    '''automatic periodic updates'''
    if app.state == 'Start Game':
        move_snake(app)

######################## INPUT ###########################

def key_pressed(app, event):
    '''updates key presses'''
    if event.key == 'i':
        app.info_mode = not app.info_mode
    if app.state == 'gameover':
        if event.key == 'Space':
            app.state = 'menu'
            reset_game()# lag en reset funksjon
    if app.state == 'Start Game':
            
        if event.key == 'Up' and app.last_move != 'south':
            app.direction = 'north'
        elif event.key == 'Down' and app.last_move != 'north':
            app.direction = 'south'
        elif event.key == 'Right' and app.last_move != 'west':
            app.direction = 'east'
        elif event.key == 'Left' and app.last_move != 'east':
            app.direction = 'west'

def mouse_pressed(app, event):
    mouse_x = event.x
    mouse_y = event.y
    if app.state == 'menu':
        x_low = app.width/2-app.height/16*2
        x_high = app.width/2+app.height/16*2
        if mouse_x>x_low and mouse_x<x_high:
            click_button(app,mouse_y)
            


def click_button(app,pos):
    
    for i in range(len(app.buttonpos['menu'][0])):
        start,end = app.buttonpos['menu'][0][i]
        if pos in range(start,end):
            app.state = app.buttonpos['menu'][1][i]
        


################ functions #######################

def redraw_all(app, canvas):
    '''draws all visual elements shown in app depending on game state and other conditions'''
    if app.state == 'menu':
        draw_menu(canvas,app.buttonpos['menu'][1],app.width,app.height)
    elif app.state == 'Start Game':
        draw_board(canvas,25,25,app.width-125,app.height-25,app.board,app.info_mode)
        if app.info_mode:
            canvas.create_text(
                app.width/2, 15, 
                text=f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction = \'{app.direction}\'', 
                font="arial 10")
    elif app.state == 'gameover':
        canvas.create_text(app.width/2,app.height/2, text="GAME OVER", font='arial 50')
        canvas.create_text(app.width/2,app.height/1.5, text="Press <SPACEBAR> to return to menu", font='arial 20')


def move_snake(app):
    '''the main function of the game part,
    moves the snake, checks if the move is legal,
      then either updates the board forward or ends the game depending'''
    head_move(app)
    if not is_legal_move(app.head_pos,app.board):
        app.state = 'gameover'
        return
    board_update(app)
    x,y = app.head_pos
    app.board[y][x] = app.snake_size
    app.last_move = app.direction

def is_legal_move(pos, board):
    '''checks if new head position is a legal place to be, 
    within the borders of the game and not in itself'''
    x,y = pos
    try:
        if x>len(board[0]) or y>len(board) or board[y][x]>0 or x<0 or y<0:
            return False
        else:
            return True
    except:
        return False


def board_update(app):
    '''updates the board state 1 step forward in time by reducing all positive values(where the snake has been) by 1, 
    thus keeping track of how long ago the snake was there simulating snake trail'''
    was_apple_eaten = eat_apple(app)
    if not was_apple_eaten:
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                if app.board[row][col] >0:
                    app.board[row][col] -=1

def eat_apple(app):
    '''checks if snake can eat apple, if it can it spawns a new apple in another legal position. 
    Then it returns True or False depending on if it ate an apple'''
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
    '''move the snake in chosen direction'''
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

############################### RUN THE APP ########################################

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    from draw_menu import draw_menu, draw_settings
    run_app(width=500, height=400, title='Snake')
