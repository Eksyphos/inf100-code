liste1 = [1,2,3,4]
a = liste1.copy()

def destruktiv(liste):
    for i in range(len(liste)):
            liste[i]= i+2

def ikkedestruktiv(liste):
    newlist = []
    for i in range(len(liste)):
            newlist.append(liste[i]+1)
    return newlist


var2 = ikkedestruktiv(liste1)
print(var2)
destruktiv(liste1)
print(liste1)