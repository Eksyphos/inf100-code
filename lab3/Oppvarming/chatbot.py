answer = "yes"
while answer != "no":
    answer = str.lower(input("Hi! Do you want to talk to me?"))
    if answer == "no":
        print("All right, bye!")
    else:
        print("That's cool!")
