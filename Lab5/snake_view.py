

def draw_board_row(canvas,x1,y1,x2,y2,row,rownum,info_mode):
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
    if val==0:
        clr='lightgray'
    elif val>0:
        clr='orange'
    else:
        clr ='cyan'
    return clr

def draw_board(canvas,x1,y1,x2,y2,board,info_mode):
    height = abs(y1-y2)
    rows = len(board)
    Hstep = height/rows
    for i in range(len(board)):
        ys = y1+(i*Hstep)
        ye = y1+((i+1)*Hstep)
        draw_board_row(canvas,x1,ys,x2,ye,board[i],i,info_mode)


if __name__ == '__main__':
    from uib_inf100_graphics.simple import canvas, display

    test_board = [
        [1, 2, 3, 0, 5, 4,-1,-1, 1, 2, 3],
        [0, 4, 0, 7, 0, 3,-1, 0, 0, 4, 0],
        [0, 5, 0, 8, 1, 2,-1,-1, 0, 5, 0],
        [0, 6, 0, 9, 0, 0, 0,-1, 0, 6, 0],
        [0, 7, 0,10,11,12,-1,-1, 0, 7, 0],
    ]

    draw_board(canvas, 25, 80, 375, 320, test_board, True)
    display(canvas)
