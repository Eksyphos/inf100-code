#lese inn tre ord
print("Skriv et ord:")
ord1 = input()
print("Skriv et annet ord:")
ord2 = input()
print("Skriv et siste ord:")
ord3 = input()
minord = (min(len(ord1),
              len(ord2),
              len(ord3)))
print("")
if len(ord1)<=minord:
    print(ord1)

if len(ord2)<=minord:
    print(ord2)

if len(ord3)<=minord:
    print(ord3)
