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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You are starting at a cross road. Which way do you want to go?")
way = input("Type 'left' or 'right': ")
way = way.lower()
if way == "left":
    print("You've come to a lake. There's an island in the middle of the lake.")
    action = input("Type 'wait' to wait for a boat, or type 'swim' to swim across: ")
    action = action.lower()
    if action == "wait" or action == "wait for boat" or action == "boat":
        print("The boat takes you to the island safely. On the island, there is a house with three doors.")
        print("One red, one yellow and one blue.")
        door = input("Which colour do you choose? ")
        door = door.lower()
        if door == "yellow":
            print("Congratulations! You found the treasure! YOU WIN!!")
        elif door == "red":
            print("The room is on fire and it burns you down! GAME OVER.")
        elif door == "blue":
            print("The room is full of lions and you fall prey to them! GAME OVER.")
        else:
            print("You chose a door that doesn't exist! GAME OVER.")
    else:
        print("Oh no! The lake is full of crocodiles, and they've attacked you! GAME OVER.")
else:
    print("Oops! You've fallen into a hole! GAME OVER.")
