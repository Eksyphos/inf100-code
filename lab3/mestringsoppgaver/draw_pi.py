from uib_inf100_graphics.simple import canvas, display
import random
#draw and highlight dots
def draw_dot(canvas, x, y,totaldots):
    if circles_overlap(x,y):
        canvas.create_oval(x-3, y-3, x+3, y+3, fill='orange')
        return True
    else:
        canvas.create_oval(x-3, y-3, x+3, y+3, fill='grey')
        return False

def circles_overlap(x1,y1):
    rekkevidde = 200
    avstand = (((200-x1)**2)+((200-y1)**2))**0.5
    if avstand<=rekkevidde:
        return True
    else:
        return False

# Draw a circle in the window
canvas.create_oval(0, 0, 400, 400)

dotter = 1_000_000
count = 0
incount = 0
while count < dotter:
    count +=1
    x = random.random() * 400
    y = random.random() * 400
    if draw_dot(canvas, x, y):
        incount+=1
print(incount)

picalc = incount/dotter*4

#draw result message
canvas.create_rectangle(100,175,300,225, fill="white")
canvas.create_text(200,200, text=f"{incount}/{dotter} prikker traff sirkelen", anchor="center")
display(canvas)
print(picalc)