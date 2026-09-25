def draw_multicolored_flag(canvas,x1,y1,x2,y2,colors):
    collumns = len(colors)
    length = abs(x1-x2)
    step = length/collumns
    for i in range(collumns):
        canvas.create_rectangle(
            x1+step*i, y1,
            x1+step*(i+1), y2,
            fill=str(colors[i]),
            #outline = ""
        )

def draw_grid(canvas,x1,y1,x2,y2,color_grid):
    length = abs(x1-x2)
    height = abs(y1-y2)
    rows = len(color_grid)
    collumns = len(color_grid[0])
    Lstep = length/collumns
    Hstep = height/rows
    for i in range(len(color_grid)):
        ys = y1+(i*Hstep)
        ye = y1+((i+1)*Hstep)
        draw_multicolored_flag(canvas,x1,ys,x2,ye,color_grid[i])