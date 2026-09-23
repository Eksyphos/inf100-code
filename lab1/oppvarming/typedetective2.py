type: 
a = 5#int()
b = 5.0#float()
c = 5/1#float()
d = 5//1#int()
e = "5"#str
f = 5==5.0#bool
g = True + True#int()
h = int("42")#int()
i = int("42.0")#error
list = [a,b,c,d,e,f,g,h,i]
x=0
while x<len(list):
    print(type(list[x]))
    x=x+1
