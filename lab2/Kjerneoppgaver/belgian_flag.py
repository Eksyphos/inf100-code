# belgian_flag.py

def draw_belgian_flag(canvas, x1, y1, x2, y2):
    width = x2-x1
    height = y2-y1
    canvas.create_rectangle(
            x1, y1,
            x1+width/3, y2,
            fill="black", outline=''
        )
    canvas.create_rectangle(
            x1+width/3, y1,
            x1+width/3*2, y2,
            fill="yellow", outline=''
        )
    canvas.create_rectangle(
            x1+width/3*2, y1,
            x1+width, y2,
            fill="red", outline=''
        )