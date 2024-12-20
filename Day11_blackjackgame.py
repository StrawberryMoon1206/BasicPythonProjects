import random
logo2 = ('''
  _     _            _    _            _    
 | |   | |          | |  (_)          | |   
 | |__ | | __ _  ___| | ___  __ _  ___| | __
 | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                        _/ |                
                       |__/        
              ''')
logo = ('''
                   .------.
.------.           |A .   |
|A_  _ |    .------; / \  |
|( \/ )|-----. _   |(_,_) |
| \  / | /\  |( )  |  I  A|
|  \/ A|/  \ |_x_) |------'
`-----+'\  / | Y  A|
      |  \/ A|-----'    
      `------'
            ''')
def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def calculate_sum(cardlist):
    if sum(cardlist) == 21 and len(cardlist) == 2:
        return 0 # when user has ace and 10 only
    if sum(cardlist)>21 and 11 in cardlist:
        cardlist.remove(11)
        cardlist.append(1) #swap before calculating sum
    return sum(cardlist)

def verdict(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over 21! YOU LOSE! 😭"
    if player_score == computer_score:
        return "You both get the same score! It's a DRAW! 🤝"
    elif computer_score == 0:
        return "Computer got a blackjack! YOU LOSE! 😭"
    elif player_score == 0:
        return "You got a blackjack! YOU WIN! 🥳"
    elif player_score>21:
        return "You went over 21! YOU LOSE! 😭 "
    elif computer_score>21:
        return "Computer went over 21! YOU WIN! 🥳"
    elif player_score>computer_score:
        return "You have a higher score! YOU WIN! 🥳"
    else:
        return "Computer has a higher score! YOU LOSE! 😭"

def play_blackjack():
    print(logo2+logo)
    user_cards = []
    dealer_cards = []

    for x in range(2):
        user_cards.append(get_card())
        dealer_cards.append(get_card())
    
    game_over = False   #using flag variable instead of normal while True

    while not game_over:  #loop for dealing cards to the user
        user_score = calculate_sum(user_cards)
        dealer_score = calculate_sum(dealer_cards)
        print(f"Your cards are: {user_cards},  Your current score is: {user_score}")
        print(f"Computer's first card is: {dealer_cards[0]}")
        if user_score == 0 or dealer_score == 0 or user_score>21:
            game_over = True
        else:
            gamechoice = input("Type 'hit' to get another card, or type 'stand' to pass: ").lower()
            if gamechoice == "hit":
                user_cards.append(get_card())
            else:
                game_over = True
    
    while dealer_score != 0 and dealer_score<17:  #loop for dealing cards to the computer
        dealer_cards.append(get_card())
        dealer_score = calculate_sum(dealer_cards)

    print(f"Your final hand is: {user_cards},  Your final score is: {user_score}")
    print(f"Computer's final hand is: {dealer_cards},  Computer's final score is: {dealer_score}")
    print(verdict(user_score, dealer_score))
    
playchoice = input("Do you want to play a game of blackjack? Type 'y' for yes, or 'n' for no: ")

while playchoice == "y":
    print("\n"*100)
    play_blackjack()
    playchoice = input("Do you want to play again? Type 'y' for yes, or 'n' for no: ")
else:
    print("Thanks for playing!")
