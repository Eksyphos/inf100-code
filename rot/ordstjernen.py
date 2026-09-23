from pathlib import Path

file_data = Path("nsf2025.txt").read_text(encoding='utf-8')
ordliste = file_data.split("\n")
filterliste = []
gyldige_ord = []

senterbokstav = "f"
bokstavliste = "bgufetå"

for ord in ordliste:
    if len(ord)>3:
        filterliste.append(ord)

#gyldigsjekk
def word_is_legal(word):
    for letter in word:
        if senterbokstav not in word:
            return False
        
        if letter not in bokstavliste:
            return False
    return True

for word in filterliste:
    if word_is_legal(word)==True:
        gyldige_ord.append(word)

print(gyldige_ord)
print(len(gyldige_ord))