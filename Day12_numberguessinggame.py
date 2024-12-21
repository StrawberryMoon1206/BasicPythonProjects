logo = ('''
8""""8                                               8"""8                                  8  
8    " e   e eeee eeeee eeeee    eeeee e   e eeee    8   8 e   e eeeeeee eeeee  eeee eeeee  88 
8e     8   8 8    8   " 8   "      8   8   8 8       8e  8 8   8 8  8  8 8   8  8    8   8  88 
88  ee 8e  8 8eee 8eeee 8eeee      8e  8eee8 8eee    88  8 8e  8 8e 8  8 8eee8e 8eee 8eee8e 88 
88   8 88  8 88      88    88      88  88  8 88      88  8 88  8 88 8  8 88   8 88   88   8    
88eee8 88ee8 88ee 8ee88 8ee88      88  88  8 88ee    88  8 88ee8 88 8  8 88eee8 88ee 88   8 88 
''')
import random
numbers = []
for x in range(1, 101):
    numbers.append(x)

def decide_number():
    number_to_guess = random.choice(numbers)
    return number_to_guess


def easy():
    number_to_guess = decide_number()
    for y in range(10, 0, -1):
        print(f"You have {y} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Please enter a valid number!")
            continue
        if guess == number_to_guess:
            return f"You got it! The number was {number_to_guess}."
        elif guess>number_to_guess:
            print("Entered guess is too high!")
            if y != 1:
                print("Try again!")
        else:
            print("Entered guess is too low!")
            if y != 1:
                print("Try again!")
    return f"You've run out of guesses! The number was {number_to_guess}!"
    

def hard():
    number_to_guess = decide_number()
    for y in range(5, 0, -1):
        print(f"You have {y} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Please enter a valid number!")
            continue
        if guess == number_to_guess:
            return f"You got it! The number was {number_to_guess}."
        elif guess>number_to_guess:
            print("Entered guess is too high!")
            if y != 1:
                print("Try again!")
        else:
            print("Entered guess is too low!")
            if y != 1:
                print("Try again!")
    return f"You've run out of guesses! The number was {number_to_guess}!"

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        print("Please enter either 'easy' or 'hard' as the difficulty.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        print(easy())
    elif difficulty == "hard":
        print(hard())


play_game()
game_choice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
while game_choice not in ["y", "n"]:  #checks first round
    print("Please choose either 'y' or 'n'.")
    game_choice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
while game_choice == "y":
    print("\n"*100)
    play_game()
    game_choice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    while game_choice not in ["y", "n"]: #again here for checking for subsequent rounds
        print("Please choose either 'y' or 'n'.")
        game_choice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
if game_choice == "n":
    print("Thanks for playing!")
