import math
print("x1 = ")
x1 = int(input())
print("y1 = ")
y1 = int(input())
print("x2 = ")
x2 = int(input())
print("y2 = ")
y2 = int(input())
#endringstest
distx =(x1-x2)
disty =(y1-y2)

distance = math.sqrt((distx**2)+(disty**2))
print (f"Avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er ", distance)