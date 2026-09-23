#konverteringsfunksjon
def nmtilTHz(nm):
    #c = 299_792_458 #i meter
    c = 3*10**8
    Thz= c*10**-3/int(nm)
    return Thz

#input
enhet = str.lower(input("Angi enhet (nm eller THz):"))
if enhet == "nm":
    nmverdi = input("Angi verdi i nm:")
    thzverdi = nmtilTHz(nmverdi)
elif enhet == "thz":
    thzverdi = int(input("Angi verdi i THz:"))
else:
    print(f"Enheten må være i nm eller THz, det kan ikke være {enhet}.")
#bare kjør hvis reelt svar
if enhet =="nm" or enhet=="thz":
    #Bestem fargen
    if 400<=thzverdi<480:
        farge = "red"
    elif thzverdi<510:
        farge = "Orange"
    elif thzverdi<530:
        farge = "Yellow"
    elif thzverdi<600:
        farge = "Green"
    elif thzverdi<620:
        farge = "Cyan"
    elif thzverdi<670:
        farge = "Blue"
    elif thzverdi<=790:
        farge = "Violet"
    else:
        farge="utenfor"
    #returnerer farge om den er innenfor det synlige spektrumet
    if farge=="utenfor":
        if enhet=="nm":
            print(f"{nmverdi} nm er utenfor det synlige spekteret.")
        else:
            print(f"{thzverdi} THz er utenfor det synlige spekteret.")
    else:
        print(farge)



