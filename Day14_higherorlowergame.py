logo = ('''
 /$$   /$$ /$$           /$$                                                           /$$                                                   /$$$$ 
| $$  | $$|__/          | $$                                                          | $$                                                  /$$  $$
| $$  | $$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$         /$$$$$$   /$$$$$$       | $$        /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$|__/\ $$
| $$$$$$$$| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$       /$$__  $$ /$$__  $$      | $$       /$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$   /$$/
| $$__  $$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$  \ $$| $$  \__/      | $$      | $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/  /$$/ 
| $$  | $$| $$| $$  | $$| $$  | $$| $$_____/| $$            | $$  | $$| $$            | $$      | $$  | $$| $$ | $$ | $$| $$_____/| $$       |__/  
| $$  | $$| $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$            |  $$$$$$/| $$            | $$$$$$$$|  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$        /$$  
|__/  |__/|__/ \____  $$|__/  |__/ \_______/|__/             \______/ |__/            |________/ \______/  \_____/\___/  \_______/|__/       |__/  
               /$$  \ $$                                                                                                                           
              |  $$$$$$/                                                                                                                           
               \______/   
        ''')

versus = ('''
 /$$    /$$            
| $$   | $$            
| $$   | $$ /$$$$$$$   
|  $$ / $$//$$_____/   
 \  $$ $$/|  $$$$$$    
  \  $$$/  \____  $$   
   \  $/   /$$$$$$$//$$
    \_/   |_______/|__/
          ''')

import random
from Day14_gamedata import data  #accessing the list from game data

score = 0
def insta_account():
    chosen_account = random.choice(data) 
    name = chosen_account["name"]
    follower_count = chosen_account["follower_count"]
    description = chosen_account["description"]
    country = chosen_account["country"]
    return {"name": name, "follower_count": follower_count, "description": description, "country": country}
    #will return chosen account dictionary from data list

def if_guess_is_A():
    global score, accountA, accountB
    if accountA["follower_count"] > accountB["follower_count"]:
        score+=1
        print("\n"*20)
        print(logo)
        print(f"You're right! Your current score is {score}.")
        accountA = accountB  #swap accounts
        accountB = insta_account()
        while accountA["name"] == accountB["name"]:
            accountB = insta_account()
        play_game()
    else:
        print(f"Sorry, that's wrong. Your final score is {score}.")
        return

def if_guess_is_B():
    global score, accountA, accountB
    if accountB["follower_count"] > accountA["follower_count"]:
        score+=1
        print("\n"*20)
        print(logo)
        print(f"You're right! Your current score is {score}.")
        accountA = accountB  #swap accounts
        accountB = insta_account()
        while accountA["name"] == accountB["name"]:
            accountB = insta_account()
        play_game()
    else:
        print(f"Sorry, that's wrong. Your final score is {score}.")
        return

def play_game():
    global accountA, accountB, score
    if score == 0:  #for first round choose two random accounts
        accountA = insta_account()
        accountB = insta_account()
        while accountA["name"] == accountB["name"]:  #if two accounts chosen are same
            accountB = insta_account()
    print(f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}.")
    print(versus)
    print(f"Against B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}.")
    guess = input("Who has more followers, A or B?: ").upper()
    
    while guess not in ["A", "B"]:
        print("Please type either 'A' or 'B'. ")
        guess = input("Who has more followers, A or B?: ").upper()
    if guess == "A":
        if_guess_is_A()
    elif guess == "B":
        if_guess_is_B()

print(logo)
play_game()

playchoice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
while playchoice not in ["y", "n"]:
    print("Please enter either 'y' or 'n'.")
    playchoice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()

while playchoice == "y":
    print("\n"*100)
    score = 0 #so that in new game, u get new score
    print(logo)
    play_game()
    playchoice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    while playchoice not in ["y", "n"]:
        print("Please enter either 'y' or 'n'.")
        playchoice = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
if playchoice == "n":
    print("Thanks for playing!")
