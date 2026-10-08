def app_started(app):
    '''startup variables'''
    app.timer_delay =800
    app.state = 'menu'
    app.info_mode = False
    ######## MULTI BOARD SETUP #######
    app.board = [
        [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    ]
    app.direction = ['east','east']
    app.snake_size = [3,3]
    app.head_pos = [(4, 3),(4,3)] 
    app.last_move = ['east','east']

    ##### GAME SETTINGS #######
    app.paused = False
    app.settings = {
        'Game speed':1,
        'Board Size':1,
        'Game Mode':1,
        'Keybinds':1,
        'Reset Settings':1,
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
    app.illegalbuttonpress = {
        'north':'south',
        'south':'north',
        'east':'west',
        'west':'east',
    }

###################### INPUT ###################

def key_pressed(app, event):
    '''updates key presses'''

    if event.key == 'Escape':
        app.state = 'menu'
        app.paused = True
    if event.key == 'i':
        app.info_mode = not app.info_mode
    if app.state == 'gameover':
        if event.key == 'Space':
            reset_game(app)
    if event.key == 'p':
        app.paused = not app.paused
    if app.state == 'Start Game': #direction control Board 1
        for i in range(len(app.board)):
            if event.key in app.keybinds['movedirection'][i] and app.illegalbuttonpress[app.keybinds['movedirection'][i][event.key]]!=app.last_move[i]:
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
    if app.state == 'How To Play':
        if point_in_rectangle(app.width*0.05,app.height*0.05,app.width*0.25,app.height*0.25,event.x,event.y):
            app.state= 'menu'
    if mouse_x>x_low and mouse_x<x_high:
        click_button(app,mouse_y,app.state)
    #elif app.state == 'Settings':

def click_button(app,pos,page):
    if page == 'menu':
        for i in range(len(app.buttonpos[page])):
            start,end = app.buttonpos[page][i]
            if pos in range(start,end):
                app.state = app.pagebuttons[page][i]
    if page == 'Settings':
        for i in range(len(app.buttonpos[page])):
            start,end = app.buttonpos[page][i]
            if pos in range(start,end):
                app.settings[app.pagebuttons['Settings'][i]] = (app.settings[app.pagebuttons['Settings'][i]]+1)%3
    


############ DRAW THE GAME WINDOW ##############

def redraw_all(app, canvas):
    '''draws all visual elements shown in app depending on game state and other conditions'''
    if app.state == 'menu':
        draw_main_menu(canvas,app.width,app.height,app.pagebuttons[app.state],app.info_mode)
    elif app.state == 'Settings':
        draw_settings_page(canvas,app.width,app.height,app.pagebuttons[app.state],app.settings,app.info_mode)
    elif app.state =='How To Play':
        draw_h2p(canvas,app.width,app.height,app.pagebuttons[app.state],app.settings,app.info_mode)
    elif app.state == 'gameover':
        canvas.create_text(app.width/2,app.height/2, text="GAME OVER", font='arial 50')
        canvas.create_text(app.width/2,app.height/1.5, text="Press <SPACEBAR> to return to menu", font='arial 20')
    
    elif app.state == 'Start Game':
        draw_board(canvas,25,25,app.width-125,app.height-25,app.board[0],app.info_mode)
        if app.info_mode:
            canvas.create_text(
                app.width/2, 15, 
                text=f'app.head_pos={app.head_pos[0]} app.snake_size={app.snake_size} app.direction = \'{app.direction}\'', 
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
    if not is_legal_move(app.head_pos[0],app.board[0]):
        app.state = 'gameover'
        return
    board_update(app)
    x,y = app.head_pos[0]
    app.board[0][y][x] = app.snake_size[0]
    app.last_move[0] = app.direction[0]

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
    x,y = app.head_pos[0]
    if app.direction[0] == 'north':
        y-=1
    elif app.direction[0] == 'south':
        y+=1
    elif app.direction[0] == 'east':
        x +=1
    elif app.direction[0] == 'west':
        x-=1
    #app.head_pos[0] = x%len(app.board[0]),y%len(app.board)
    app.head_pos[0] = x,y

def board_update(app):
    '''updates the board state 1 step forward in time by reducing all positive values(where the snake has been) by 1, 
    thus keeping track of how long ago the snake was there simulating snake trail'''
    was_apple_eaten = eat_apple(app)
    if not was_apple_eaten:
        for row in range(len(app.board[0])):
            for col in range(len(app.board[0][0])):
                if app.board[0][row][col] >0:
                    app.board[0][row][col] -=1

def eat_apple(app,whichsnake=0):
    '''checks if snake can eat apple, if it can it spawns a new apple in another legal position. 
    Then it returns True or False depending on if it ate an apple'''
    from random import randrange
    x,y = app.head_pos[0]
    if app.board[0][y][x] <0:
        app.snake_size[0] +=1
        while True and app.snake_size[0]<(len(app.board[0][0])+len(app.board[0])):
            x = randrange(len(app.board[0][0]))
            y = randrange(len(app.board[0]))
            if app.board[0][y][x] ==0:
                app.board[0][y][x] = -1
                break
            else:
                continue
        return True
    return False

#################### RESET FUNCTIONS ######################

def reset_game(app):
    '''startup variables'''
    app.timer_delay =800
    app.state = 'menu'

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
    app.direction = ['east','east']
    app.snake_size = [3,3]
    app.head_pos = [(4, 3),(4,3)] 
    app.last_move = ['east','east']

def reset_settings(app):
    app.settings = {
        'Game speed':1,
        'Board Size':1,
        'Game Mode':0,
    }

#################### HELP FUNCTIONS #####################

def point_in_rectangle(x1,y1,x2,y2,xp,yp):
    if (x1<=xp<=x2 or x2<=xp<=x1) and (y1<=yp<=y2 or y2<=yp<=y1):
        return True
    else:
        return False

##################### START THE GAME #################

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    from draw_pages import draw_main_menu, draw_settings_page,draw_h2p
    run_app(width=500, height=400, title='Snake')
