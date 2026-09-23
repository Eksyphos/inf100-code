from uib_inf100_graphics.simple import canvas, display

#def eyes(posX,posY,spacing,size,color):
    #canvas.create_oval(posX-spacing-size,)
#head
canvas.create_oval(100, 50, 300, 300, fill="green")

#eyes
canvas.create_oval(150,120,180,150, fill="white")
canvas.create_oval(160,130,170,140, fill="black")

canvas.create_oval(250,120,220,150, fill="white")
canvas.create_oval(240,130,230,140, fill="black")

#mouth
canvas.create_oval(150,200,250,250,fill="yellow")
canvas.create_oval(175,240,210,250,fill="red")

display(canvas)
