def sequence_for(n): #definerer funksjonen "sequence for" med parameter n
    string = "" #lager en tom streng
    for i in range(n+1): #for loop for å gå gjennom alle tallene i en satt range
        string = f"{string}{i} " #legger tallet til strengen
    return string #returnerer strengen

def sequence_while(n): #definerer funksjonen "sequence while" med parameter n
    string = ""#lager en tom streng
    i = 0 #lager en int variabel
    while i in range(n+1): #while loop for å gjøre operasjonen så lenge i finnes i den satte rangen
        string = f"{string}{i} " #legger taller til i strengen
        i += 1 #bruker i for å telle at vi har sjekket dette heltallet og går til neste
    return string #returnerer strengen

streng = sequence_for(5) #kaller på funksjonen "sequence for" med argumentet 5
string = sequence_while(5) #kaller på funksjonen "sequence while" med argumentet 5

print(streng)
print(string)