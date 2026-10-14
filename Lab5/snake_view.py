

def draw_board_row(canvas,x1,y1,x2,y2,row,rownum,info_mode):
    '''draws a single row of the board'''
    collumns = len(row)
    length = abs(x1-x2)
    step = length/collumns
    for i in range(collumns):
        color = get_colors(row[i])
        canvas.create_rectangle(
            x1+step*i, y1,
            x1+step*(i+1), y2,
            fill=color,
        )
        if info_mode:
            canvas.create_text(x1+step*(i+0.5),(y1+y2)/2, text=f'{i},{rownum}\n {row[i]}', font="arial 10")
            

def get_colors(val):
    '''selects the color of the square based on its value'''
    if val==0:
        clr='lightgray'
    elif val>0:
        clr='orange'
    else:
        clr ='cyan'
    return clr

def draw_board(canvas,x1,y1,x2,y2,board,info_mode,paused,snaketracker):
    '''draws the game board and fills in the correct colors'''
    fontsize=int(round(min(x2,y2)*0.1))
    height = abs(y1-y2)
    rows = len(board)
    Hstep = height/rows
    for i in range(len(board)):
        ys = y1+(i*Hstep)
        ye = y1+((i+1)*Hstep)
        draw_board_row(canvas,x1,ys,x2,ye,board[i],i,info_mode)
    if paused:
        canvas.create_rectangle(x2/2-x2*0.3,y2/2-y2*0.075,x2/2+x2*0.3,y2/2+y2*0.075,fill='orange',width=3,outline='black')
        canvas.create_text(x2/2,y2/2,text='PAUSED',font=f'arial {fontsize}',fill='white')
    if info_mode:
        canvas.create_text(x2/2,y2*1.02,text=f'{snaketracker}')
    

def draw_multiple_boards(canvas,):
    #make a function that creates atleast 2 boards to play in at the same time
    a = 0
