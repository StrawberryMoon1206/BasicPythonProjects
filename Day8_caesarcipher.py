print('''
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
                                                         
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             

''')
print("Welcome to the digital Caesar Cipher!")
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while True:
    direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt: \n").lower()
    if direction != "encode" and direction != "decode":
        print("Please choose either 'encode' or 'decode' to use the caesar cipher.")
        continue
    text = input("Type your message: \n").lower()
    shift = int(input("Enter shift number: \n"))

    def caesar(task, original_text, shift_amount):
        finaltext = ""
        for letter in original_text:
            if not letter in alphabets:  #includes spaces
                finaltext += letter
            else: 
                letterindex = alphabets.index(letter)
                if task == "encode":
                    shiftedletter = shift_amount + letterindex
                if task == "decode":
                    shiftedletter = letterindex - shift_amount
                try: 
                    finaltext += alphabets[shiftedletter]
                except:
                        finaltext += alphabets[shiftedletter%len(alphabets)] #for range to be within 26
        return finaltext

    print(f"The {direction}d message is:", caesar(direction,text,shift))
    choice = input("Type 'Yes' if you want to go again, otherwise type 'No': \n").lower()
    if choice != "yes":
        print("Thank you for using the Caesar Cipher! Goodbye!")
        break
