

def draw_row(canvas,x1,y1,x2,y2,row):
    '''draws a single row of the qr'''
    collumns = len(row)
    length = abs(x1-x2)
    step = length/collumns
    for i in range(collumns):
        color = get_colors(row[i])
        canvas.create_rectangle(
            x1+step*i, y1,
            x1+step*(i+1), y2,
            fill=color,
            outline =''
        )      

def get_colors(val):
    '''selects the color of the square based on its value'''
    if val==0:
        clr='white'
    elif val>0:
        clr='black'
    return clr

def draw_qr(canvas,x_left,y_top,size,qr):
    '''draws the qr code'''
    height = size
    rows = len(qr)
    Hstep = height/rows
    for i in range(len(qr)):
        ys = y_top+(i*Hstep)
        ye = y_top+((i+1)*Hstep)
        draw_row(canvas,x_left,ys,x_left+size,ye,qr[i])
    

def display(matrix):
    from uib_inf100_graphics.simple import canvas, display as dsp
    canvas.create_rectangle(0, 0, 400, 400, fill='white', outline='')
    draw_qr(canvas, 25, 25, 350, matrix)
    dsp(canvas)

if __name__ == '__main__':
    sample_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    display(sample_grid)