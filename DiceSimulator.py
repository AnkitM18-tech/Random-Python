import random
x=input("Input Initial Value To Start(\"y\"):")

while x=="y":
    number=random.randint(1,6)
    if number==1:
        print("-----------------")
        print("|               |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("|               |")
        print("-----------------")
    elif number==2:
        print("-----------------")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("-----------------")
    elif number==3:
        print("-----------------")
        print("|               |")
        print("|               |")
        print("|  O   O   O    |")
        print("|               |")
        print("|               |")
        print("-----------------")
    elif number==4:
        print("-----------------")
        print("|               |")
        print("|  O         O  |")
        print("|               |")
        print("|  O         O  |")
        print("|               |")
        print("-----------------")
    elif number==5:
        print("-----------------")
        print("|               |")
        print("|  O         O  |")
        print("|       O       |")
        print("|  O         O  |")
        print("|               |")
        print("-----------------")
    elif number==6:
        print("-----------------")
        print("|               |")
        print("|    O     O    |")
        print("|    O     O    |")
        print("|    O     O    |")
        print("|               |")
        print("-----------------")
    x=input("Enter \"y\" to Roll The Dice:")