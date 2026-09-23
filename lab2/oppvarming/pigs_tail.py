from uib_inf100_graphics.simple import canvas, display

# Legs
canvas.create_rectangle(110, 230, 150, 300, fill="pink")
canvas.create_rectangle(300, 230, 340, 300, fill="pink")
canvas.create_rectangle(80, 260, 120, 330, fill="pink")
canvas.create_rectangle(280, 260, 320, 330, fill="pink")

# Ears
canvas.create_polygon(260, 70, 260, 30, 290, 60, fill="pink", outline="black")
canvas.create_polygon(310, 55, 330, 30, 340, 70, fill="pink", outline="black")

# Body
canvas.create_oval(50, 100, 350, 300, fill="pink")

# Head
canvas.create_oval(250, 50, 350, 150, fill="pink")

# Eyes
canvas.create_oval(280, 70, 295, 85, fill="black")
canvas.create_oval(320, 70, 335, 85, fill="black")

# Nose
canvas.create_oval(290, 100, 330, 130, fill="lightpink")
canvas.create_oval(295, 110, 305, 120, fill="black")
canvas.create_oval(315, 110, 325, 120, fill="black")

# Tail
canvas.create_line(50,200,
                   40,100, 50,100, 45,100, 45,50, 40,50, 55,50,
                   55,100, 55,50, 65,100, 65,50,
                   90,50, 70,50, 70,100, 70,60, 80,60, 70,60, 70,50,
                   90,50, 85,55, 90,50, 90,100, 85,100, 100,100,
                   95,95, 95,55, 100,50, 105,55, 105,95, 100,100,
                   115,100, 110,95, 110,55, 115,50, 120,55, 120,95, 115,100
                   )

display(canvas)
