print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)? ").lower()

if answer=="left":
    answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around or 'swim' to swim across: ").lower()
    if answer=="swim":
        print("You swam across and were eaten by a Caiman. You Lose!")
    elif answer=="walk":
        print("You ran for many miles, ran out of water and you lost the game.")
    else:
        print("Invalid Choice. You Lose!")
elif answer=="right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer=="back":
        print("You go back and you lose!")
    elif answer=="cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer=="yes":
            print("You talk to the stranger and they give you gold. You Win!!")
        elif answer=="no":
            print("You ignored stranger and they stab you in the bacl. You Lose!")
        else: 
            print("Invalid Choice. You Lose!")
    else:
        print("Invalid Choice. You Lose!")
else:
    print("Invalid Choice. You Lose!")

print("Thanks for playig the game,", name + "!")