def draw_multicolored_flag(canvas,x1,y1,x2,y2,colors):
    collumns = len(colors)
    length = abs(x1-x2)
    step = length/collumns
    for i in range(collumns):
        canvas.create_rectangle(
            x1+step*i, y1,
            x1+step*(i+1), y2,
            fill=str(colors[i]),
            outline = ""
        )