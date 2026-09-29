from uib_inf100_graphics.simple import canvas
def draw_eyes():
    size = 0
def draw_face_fixed(canvas):
    canvas.create_oval(0,0,400,400,fill="pink")
    canvas.create_oval(100,100,125,150,fill="red")
    canvas.create_oval(300,100,325,150,fill="red")
    canvas.create_line(100,300,200,350,300,300,smooth="bezier", width = 3, fill="red")

def draw_face_scaled(canvas, x_lft, y_lft, width, height):
    Xscale = width/400
    Yscale = height/400
    #head
    canvas.create_oval(0*Xscale + x_lft,0*Yscale +y_lft,400*Xscale + x_lft,400*Yscale +y_lft,fill="pink")
    #eyes
    canvas.create_oval(
        100*Xscale + x_lft,100*Yscale +y_lft,
        125*Xscale + x_lft,150*Yscale +y_lft,
        fill="red"
        )
    canvas.create_oval(
        300*Xscale + x_lft,100*Yscale +y_lft,
        325*Xscale + x_lft,150*Yscale +y_lft,
        fill="red"
        )
    canvas.create_line(
        100*Xscale + x_lft,300*Yscale +y_lft,
        200*Xscale + x_lft,350*Yscale +y_lft,
        300*Xscale + x_lft,300*Yscale +y_lft,
        smooth=True,
        width = round(8*Yscale),
        fill="red"
        )

def draw_face_at(canvas,x_center,y_center,radius):

    draw_face_scaled(canvas,x_center-radius ,y_center-radius , radius*2,radius*2)