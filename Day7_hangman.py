import random
list_of_words = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "rat", "raven", "rhino", "shark", "sheep", "spider", "toad", "turkey", "turtle", "wolf", "wombat", "zebra"]
word_to_guess = random.choice(list_of_words)
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Welcome to Hangman! Try to guess the word one letter at a time.")
print("You have 6 lives to figure it out. Good luck!")
print("Hint: The word is related to the animal kingdom!")
placeholder = ""
for x in range(len(word_to_guess)):
    placeholder += "_"
print("The word to guess is:", placeholder)

correct_letters = []
lives = 0

while True:
    user_guess = str(input("Enter a letter: ")).lower()
    if not user_guess.isalpha() or len(user_guess) != 1:
        print("Please enter a single letter.")
        continue
    if user_guess in correct_letters:
        print(f"You've already entered the letter {user_guess}! Please enter another letter.")
    display = "" 
    for letter in word_to_guess:
        if letter == user_guess:
            display += user_guess
            correct_letters.append(user_guess)
        elif letter in correct_letters:  #retains already guessed letters
            display += letter
        else:
            display += "_"
    print("The word to guess is: ", display)
    if user_guess in word_to_guess:
        print(stages[lives])
    else:
        print(f"Oh no! {user_guess} is not in the word. You lose a life!")
        lives += 1
        if lives <7:
            print(stages[lives])
    print(f"Number of lives left: {6-lives}")
    if lives == 6:
        print("**********YOU LOSE!**********")
        print(f"The word was '{word_to_guess}'! Better luck next time!")
        break
    elif "_" not in display:
        print("Congratulations! You guessed the word correctly!")
        print("**********YOU WIN!**********")
        break
