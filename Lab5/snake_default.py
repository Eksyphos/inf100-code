def reset_game(app):
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
   
######### SETTINGS ##########

def reset_settings(app):
    app.settings = {
        'Game speed':1,
        'Board Size':1,
        'Game Mode':0,
    }
