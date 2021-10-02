import random

print("This is my Dice simulator")
a = "y"
while a == "y" or a == "Y":
    r = random.randint(1, 6)
    if r == 1:
        print("----------------")
        print("|              |")
        print("|      O       |")
        print("|              |")
        print("----------------")
    elif r == 2:
        print("----------------")
        print("|              |")
        print("|   O      O   |")
        print("|              |")
        print("----------------")

    elif r == 3:
        print("----------------")
        print("|      O       |")
        print("|      O       |")
        print("|      O       |")
        print("----------------")
    elif r == 4:
        print("----------------")
        print("|   O      O   |")
        print("|              |")
        print("|   O      O   |")
        print("----------------")

    elif r == 5:
        print("----------------")
        print("|   O      O   |")
        print("|      O       |")
        print("|   O      O   |")
        print("----------------")
    elif r == 6:
        print("----------------")
        print("|   O      O   |")
        print("|   O      O   |")
        print("|   O      O   |")
        print("----------------")
    a = input("If you want to roll Dice again then Press 'y' otherwise press any other key to exit")
print("Thanks!! , See You Later")

