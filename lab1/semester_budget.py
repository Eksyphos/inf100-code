print ("Hva er budsjettet ditt? ",end="")
budsjett = int(input())
print ("Hvor mye bruker du på bolig? ",end="")
bolig= int(input())
print ("Hvor mye bruker du på mat? ",end="")
mat= int(input())

kaffepris = 45
rest = budsjett-bolig-mat
kaffekopper = rest//kaffepris

print(f"Det er {rest} NOK igjen, det er nok til {kaffekopper} kopper kaffe!")