print ("Grunnfarge:")
ColA= input()
print ("Målfarge:")
ColB = input()
print("Andel målfarge:")
rationB = float(input())


RedA= int(ColA[:3])
GreenA= int(ColA[3:6])
BlueA= int(ColA[6:9])
RedB= int(ColB[:3])
GreenB= int(ColB[3:6])
BlueB= int(ColB[6:9])

RedF = round(RedA-((RedA-RedB)*rationB))
GreenF = round(GreenA-((GreenA-GreenB)*rationB))
BlueF = round(BlueA-((BlueA-BlueB)*rationB))

redx=str(f"{RedF:03d}")
greenx=str(f"{GreenF:03d}")
bluex=str(f"{BlueF:03d}")

#resultat = str(str(RedF)+str(GreenF)+str(BlueF))
#print(resultat)

print(f"{redx}{greenx}{bluex}")