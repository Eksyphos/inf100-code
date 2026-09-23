favorite_ducks = ["Donald","Dolly","Onkel Skrue"]
while len(favorite_ducks)<5:
    print("Hva er din favoritt and? ", end="")
    ny_and = str(input())
    if ny_and in favorite_ducks:
        print(ny_and,"er allerede i listen godt valg!")
    else:
        favorite_ducks.append(ny_and)
        print("Denne har jeg ikke hørt om før, legger den til i listen!")

print("\nFor en flott liste med ender!\n", favorite_ducks, "\nFint at folk har så mange favoritter!\n")

