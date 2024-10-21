letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the Python Password Generator!")
passletters = int(input("How many letters would you like in your password?\n"))
passnumbers = int(input("How many numbers would you like in your password?\n"))
passsymbols = int(input("How many symbols would you like in your password?\n"))

listpassword = []
lcount = 0
while lcount<passletters:
    letter = random.choice(letters)
    listpassword.append(letter)
    lcount +=1

ncount = 0
while ncount<passnumbers:
    number = random.choice(numbers)
    listpassword.append(number)
    ncount +=1

scount = 0
while scount<passsymbols:
    symbol = random.choice(symbols)
    listpassword.append(symbol)
    scount +=1

random.shuffle(listpassword)
print("The characters you could use are:", listpassword)
password = "".join(listpassword)
print("Your new password could be:", password)
print("Stay safe from hackers!")

#Alternate code
# listpassword = []

# for char in range(0, passletters):
#     listpassword.append(random.choice(letters))

# for char in range(0, passnumbers):
#     listpassword.append(random.choice(numbers))

# for char in range(0, passsymbols):
#     listpassword.append(random.choice(symbols))

# print(listpassword)  #Easy level, predictable password as it has first letters, then numbers and then symbols
# random.shuffle(listpassword)
# print(listpassword)
# password = ""
# for char in listpassword:
#     password += char  #concatenate using for loop instead of .join() method

# print("Your password is:", password)
