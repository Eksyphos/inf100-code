def app_started(app):
    '''startup variables'''
    app.timer_delay =800
    app.state = 'menu'
    app.info_mode = False
    app.active_game = False
    app.hover = []
    ######## MULTI BOARD SETUP #######
    app.boardsize = (10,10)
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
    app.gamemode = False
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


    app.buttons = { # x1, y1, x2, y2, text, func
        'menu' : [
            [0,0,0,0,'Start Game',startgame,False],
            [0,0,0,0,'Settings',gotosettings,False],
            [0,0,0,0,'How To Play',gotoh2p,False],
            [0,0,0,0,'Leaderboard',gotoleaderboard,False]
            ],
        'menu2': [
            [0,0,0,0,'Resume',startgame,False],
            [0,0,0,0,'New Game',newgame,False],
            [0,0,0,0,'Settings',gotosettings,False],
            [0,0,0,0,'How To Play',gotoh2p,False],
            [0,0,0,0,'Leaderboard',gotoleaderboard,False]
            ],
        'Settings' : {
            'gamespeed': [
                [0,0,0,0,'Slow',gamespeedS,False],
                [0,0,0,0,'Normal',gamespeedN,False],
                [0,0,0,0,'Fast',gamespeedF,False],
                [0,0,0,0,'advanced',gamespeedC,False],
                ],
            'boardsize': [
                [0,0,0,0,'Small',boardsizeS,False],
                [0,0,0,0,'Medium',boardsizeM,False],
                [0,0,0,0,'Large',boardsizeL,False],
                [0,0,0,0,'Huge',boardsizeH,False]
                ],
            'gamemode': [
                [0,0,0,0,'slow',gm_1,False],
                [0,0,0,0,'medium',gm_1,False],
                [0,0,0,0,'fast',gm_1,False],
                [0,0,0,0,'advanced',gm_1,False]
                ],
            'keybinds': [[0,0,0,0,'Keybinds',keybinds,False]],
            'settingsreset': [[0,0,0,0,'Reset Settings', reset_settings,False]],
            'backtomenu' : [[0,0,0,0,'Back To Menu',gotomenu,False]],

            },
        'Tutorial' : [[0,0,0,0,'Menu',gotomenu,False]],
        'Leaderboard' : [[0,0,0,0,'Menu',gotomenu,False]],
        'Gameboard' : [[0,0,0,0,'Menu',gotomenu,False]],
        'ESCmenu' : [[0,0,0,0,'Menu',gotomenu,False]],
        'gameboard': [[0,0,0,0,'menu',gotomenu,False]]
     }
    # app.pagebuttons = {
    #     'menu' : ['Start Game', 'Settings', 'How To Play', 'Leaderboard',],
    #     'Settings' : ['Game speed', 'Board Size', 'Game Mode', 'Keybinds', 'Reset Settings'],
    #     'How To Play' : [],
    #     'Leaderboard' : ['winnerlist']
    #     }
    # app.buttonpos = {
    #     'menu' : [(87,113),(117,143),(147,173),(177,203)],
    #     'Settings' : [(87,113),(117,143),(147,173),(177,203),(207,233)],
    #     'How To Play' : [],
    #     'Leaderboard' : [],
    #     }
    app.illegalbuttonpress = {
        'north':'south',
        'south':'north',
        'east':'west',
        'west':'east',
    }
    buttonpos(app)

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

def mouse_pressed(app, event):
    click_button(app,event.x,event.y)

def mouse_moved(app,event):
    hover_button(app,event.x,event.y)
def size_changed(app):
    buttonpos(app)

############ DRAW THE GAME WINDOW ##############

def redraw_all(app, canvas):
    '''draws all visual elements shown in app depending on game state and other conditions'''
    if app.state == 'menu':
        draw_main_menu(canvas,app.width,app.height,app.buttons[app.state],app.state,app.info_mode)
    elif app.state == 'Settings':
        draw_settings(canvas,app.width,app.height,app.buttons[app.state],app.state,app.info_mode)
    elif app.state =='How To Play':
        draw_h2p(canvas,app.width,app.height,app.buttons[app.state],app.state,app.info_mode)
    elif app.state == 'gameover':
        canvas.create_text(app.width/2,app.height/2, text="GAME OVER", font='arial 50')
        canvas.create_text(app.width/2,app.height/1.5, text="Press <SPACEBAR> to return to menu", font='arial 20')
    
    elif app.state == 'Start Game':
        draw_board(canvas,app.width*0.05,app.height*0.05,app.width*0.8,app.height*0.95,app.board[0],app.info_mode,app.paused)
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

def create_buttons(app,):
    #needs to create x1,y1,x2,y2,label,function
    '''create the buttons and their position based on current windowsize'''


################## GO TO FUNCTIONS #########################

def gotomenu(app):
    app.state = 'menu'
def gotosettings(app):
    app.state = 'Settings'
def gotoh2p(app):
    app.state = 'How To Play'
def gotoleaderboard(app):
    app.state = 'Leaderboard'

def startgame(app):
    app.state = 'Start Game'
def newgame(app):
    reset_game(app)
    app.state = 'Start Game'


################ SETTING FUNCTIONS ###########################
def gamespeedS(app):
    app.timer_delay = 800
def gamespeedN(app):
    app.timer_delay = 400
def gamespeedF(app):
    app.timer_delay = 200
def gamespeedC(app):
    app.timer_delay = 800

def boardsizeS(app):
    app.boardsize = (8,8)
def boardsizeM(app):
    app.boardsize = (16,16)
def boardsizeL(app):
    app.boardsize = (32,32)
def boardsizeH(app):
    app.boardsize = (64,64)

def gm_1(app):
    app.gamemode = not app.gamemode

def keybinds(app):
    app.state = 'keys'

################## BUTTON FUNCTIONS ##################
def buttonpos(app):
    buttonheight = app.height/16
    buttonwidth = app.width/4
    for key in app.buttons:
        if type(app.buttons[key])==list:
            for i in range(len(app.buttons[key])):
                x1 = app.width/2-buttonwidth
                y1 = app.height*0.4+buttonheight*(i)+1
                x2 = app.width/2+buttonwidth
                y2 = app.height*0.4+buttonheight*(i+1)
                app.buttons[key][i][0]=x1
                app.buttons[key][i][1]=y1
                app.buttons[key][i][2]=x2
                app.buttons[key][i][3]=y2
        elif type(app.buttons[key])==dict:
            counter = 0
            for key2 in app.buttons[key]:
                    counter+=1
                # if type(app.buttons[key][key2][0])==list:
                    for i in range(len(app.buttons[key][key2])):
                        x1 = app.width/2+buttonwidth*(i-len(app.buttons[key][key2])/2)+1
                        y1 = app.height*0.4+buttonheight*counter+1
                        x2 = app.width/2+buttonwidth*(i+1-len(app.buttons[key][key2])/2)
                        y2 = app.height*0.4+buttonheight*(counter+1)
                        app.buttons[key][key2][i][0]=x1
                        app.buttons[key][key2][i][1]=y1
                        app.buttons[key][key2][i][2]=x2
                        app.buttons[key][key2][i][3]=y2
                # else:
                #     x1 = app.width/2+buttonwidth*(i-len(app.buttons[key][key2])/2)
                #     y1 = app.height*0.4-buttonheight
                #     x2 = app.width/2+buttonwidth*(i+1-len(app.buttons[key][key2])/2)
                #     y2 = app.height*0.4+buttonheight
                #     app.buttons[key][key2][0]=x1
                #     app.buttons[key][key2][1]=y1
                #     app.buttons[key][key2][2]=x2
                #     app.buttons[key][key2][3]=y2

def click_button(app,mouse_x,mouse_y):
    if app.state == 'Settings':
        for key in app.buttons[app.state]:
            for button in app.buttons[app.state][key]:
                x1,y1,x2,y2,text,func,hover = button
                if point_in_rectangle(x1,y1,x2,y2,mouse_x,mouse_y):
                    func(app)
    else:
        for button in app.buttons[app.state]:
            x1,y1,x2,y2,text,func,hover = button
            if point_in_rectangle(x1,y1,x2,y2,mouse_x,mouse_y):
                func(app)

def hover_button(app,mouse_x,mouse_y):
    count = 0
    if app.state == 'Settings':
        for key in app.buttons[app.state]:
            counter = 0
            for button in app.buttons[app.state][key]:
                x1,y1,x2,y2,text,func,hover = button
                if point_in_rectangle(x1,y1,x2,y2,mouse_x,mouse_y):
                    app.buttons[app.state][key][counter][6] = True
                else:
                    app.buttons[app.state][key][counter][6] = False
                counter +=1
    else:
        counter = 0
        for button in app.buttons[app.state]:
            
            x1,y1,x2,y2,text,func,hover = button
            if point_in_rectangle(x1,y1,x2,y2,mouse_x,mouse_y):
                app.buttons[app.state][counter][6] = True
            else:
                app.buttons[app.state][counter][6] = False
            counter +=1


##################### START THE GAME #################

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
   # from draw_pages import draw_main_menu, draw_settings_page,draw_h2p
    from make_menus import draw_main_menu, draw_settings,draw_h2p
    run_app(width=500, height=400, title='Snake')
