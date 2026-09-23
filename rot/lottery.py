from random import randrange

dice_roll = randrange(6)+randrange(6)+2
print(dice_roll)

if dice_roll==7:
    print("You won")
else:
    print("You lost!")

