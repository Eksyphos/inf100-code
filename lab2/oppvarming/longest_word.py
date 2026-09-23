#lese inn tre ord
print("Skriv et ord:")
ord1 = input()
print("Skriv et annet ord:")
ord2 = input()
print("Skriv et siste ord:")
ord3 = input()
maxord = (max(len(ord1),
              len(ord2),
              len(ord3)))
print("")
if len(ord1)>=maxord:
    print(ord1)
elif len(ord2)>=maxord:
    print(ord2)
elif len(ord3)>=maxord:
    print(ord3)
