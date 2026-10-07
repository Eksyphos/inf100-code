def app_started(app):
    '''startup variables'''
    app.timer_delay =800
    app.state = 'menu'
    app.info_mode = False
    ######## MULTI BOARD SETUP #######
    app.board = [
        [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    ]
    app.compass['north','east','south','west']
    app.direction = ['east','east']
    app.snake_size = [3]
    app.head_pos = [(4, 3)] 
    app.last_move = ['east']

    ##### GAME SETTINGS #######
    app.paused = False
    app.settings = {
        'Game speed':1,
        'Board Size':1,
        'Game Mode':1,
    }
    app.keybinds = {
        'movedirection':[
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
                ]
    }
    ######### BUTTON DATA ##########
    app.pagebuttons = {
        'menu' : ['Start Game', 'Settings', 'How To Play', 'Leaderboard',],
        'Settings' : ['Game speed', 'Board Size', 'Game Mode', 'Keybinds', 'Reset Settings'],
        'How To Play' : [],
        'Leaderboard' : ['winnerlist']
        }
    app.buttonpos = {
        'menu' : [(87,113),(117,143),(147,173),(177,203)],
        'Settings' : [(87,113),(117,143),(147,173),(177,203),(207,233)],
        'How To Play' : [],
        'Leaderboard' : [],
        }

###################### INPUT ###################

def key_pressed(app, event):
    '''updates key presses'''

    if event.key == 'Escape':
        app.state = 'menu'
    if event.key == 'i':
        app.info_mode = not app.info_mode
    if app.state == 'gameover':
        if event.key == 'Space':
            reset_game(app)
    if event.key == 'p':
        app.paused = not app.paused
    if app.state == 'Start Game': #direction control Board 1
        for i in range(len(app.board)):
            if event.key in app.keybinds['movedirection'][i]:
                app.direction[i] = app.keybinds['movedirection'][i][event.key]

        # if event.key == 'Up' and app.last_move[0] != 'south':
        #     app.direction[0] = 'north'
        # elif event.key == 'Down' and app.last_move[0] != 'north':
        #     app.direction[0] = 'south'
        # elif event.key == 'Right' and app.last_move[0] != 'west':
        #     app.direction[0] = 'east'
        # elif event.key == 'Left' and app.last_move[0] != 'east':
        #     app.direction[0] = 'west'

def mouse_pressed(app, event):
    mouse_x = event.x
    mouse_y = event.y
    #if app.state == 'menu':
    x_low = app.width/2-app.height/16*2
    x_high = app.width/2+app.height/16*2
    if mouse_x>x_low and mouse_x<x_high:
        click_button(app,mouse_y,app.state)
    #elif app.state == 'Settings':

def click_button(app,pos,page):
    if page == 'menu':
        for i in range(len(app.buttonpos[page])):
            start,end = app.buttonpos[page][i]
            if pos in range(start,end):
                app.state = app.pages[page][i]
    if page == 'Settings':
        for i in range(len(app.buttonpos[page])):
            start,end = app.buttonpos[page][i]
            if pos in range(start,end):
                app.settings[app.pages['Settings'][i]] = (app.settings[app.pages['Settings'][i]]+1)%3


############ DRAW THE GAME WINDOW ##############

def redraw_all(app, canvas):
    '''draws all visual elements shown in app depending on game state and other conditions'''
    if app.state != 'Start Game':
        page = app.state
        if page == 'Settings':
            settinglist = app.settings
        else:
            settinglist = ''
        draw_menu(canvas,app.pages[page],app.width,app.height,settinglist)
    
    elif app.state == 'gameover':
        canvas.create_text(app.width/2,app.height/2, text="GAME OVER", font='arial 50')
        canvas.create_text(app.width/2,app.height/1.5, text="Press <SPACEBAR> to return to menu", font='arial 20')
    
    elif app.state == 'Start Game':
        draw_board(canvas,25,25,app.width-125,app.height-25,app.board[0],app.info_mode)
        if app.info_mode:
            canvas.create_text(
                app.width/2, 15, 
                text=f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction = \'{app.direction}\'', 
                font="arial 10")
    


############ GAME FUNCTIONS ###################

def timer_fired(app):
    '''automatic updates'''
    if app.state == 'Start Game' and not app.paused:
        move_snake(app)

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

#################### RESET FUNCTIONS ######################

def reset_game(app):
    '''startup variables'''
    app.timer_delay =1000
    app.direction = 'east'
    app.info_mode = False
    app.board = [
        [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    ]
    app.snake_size = 3
    app.head_pos = (4, 3)
    app.state = 'menu'
    app.pressed_keys = []
    app.last_move = 'east'

def reset_settings(app):
    app.settings = {
        'Game speed':1,
        'Board Size':1,
        'Game Mode':0,
    }


##################### START THE GAME #################

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    from draw_menu import draw_menu
    run_app(width=500, height=400, title='Snake')
