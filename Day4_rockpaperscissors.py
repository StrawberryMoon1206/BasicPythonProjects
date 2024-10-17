print("Welcome to the classic game of Rock Paper Scissors!")
print("What do you choose?")
userchoice = int(input("Type 0 for ROCK, 1 for PAPER, and 2 for SCISSORS: "))
if userchoice>2 or userchoice<0:   #Handling invalid input
    print("You typed an invalid number! You lose!")
    quit()  #If program implemetation not stopped here, it raises error as the index in the list 'images' goes out of the list's range
import random
computerchoice = random.randint(0,2)
rockascii = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
      
''')
paperascii = ('''
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
      
''')
scissorascii = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
      
''')
images = [rockascii, paperascii, scissorascii]
print("You chose:")
print(images[userchoice])
print("Computer chose:")
print(images[computerchoice])
#WIN 0-2, 1-0, 2-1
if (userchoice == 0 and computerchoice == 2) or (userchoice == 1 and computerchoice == 0) or (userchoice == 2 and computerchoice == 1):
    print("Congrats! You WON!")
#LOSE 0-1, 1-2, 2-0
elif (userchoice == 0 and computerchoice == 1) or (userchoice == 1 and computerchoice == 2) or (userchoice == 2 and computerchoice == 0):
    print("Oh no! You lose!")
#DRAW 0-0, 1-1, 2-2
elif userchoice == computerchoice:
    print("It's a draw!")

#Alternate code
# if userchoice>3 or userchoice<0:
#     print("You typed an invalid number! You lose!")
# elif userchoice == 0 and computerchoice == 2:
#     print("You win!")
# elif computerchoice == 2 and userchoice == 0:
#     print("You lose!")
# elif computerchoice>userchoice:
#     print("You lose!")
# elif userchoice>computerchoice:
#     print("You win!")
# elif computerchoice == userchoice:
#     print("It's a draw!")












