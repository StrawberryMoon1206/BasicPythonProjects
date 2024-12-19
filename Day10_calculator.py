def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
calc_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
#not using () after the fn name because we are only storing it not using/triggering it
logo = ('''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |    
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')
logo2 = ('''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

''')

print("Welcome to The Calculator!")
while True: 
    print(logo2 + logo)
    try:
        first_num = float(input("Enter the first number: "))
    except:
        print("Please enter a valid number.")
        continue
    while True: 
        print("Pick any one operation:")
        for symbol in calc_dict:
            print(symbol)
        operation = input()
        if operation not in calc_dict:
            print("Please enter a valid operation.")
            continue
        try:
            second_num = float(input("Enter the next number: "))
        except:
            print("Please enter a valid number.")
            continue
        try:
            solution = calc_dict[operation](first_num, second_num)
            solution = round(solution, 3)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            continue
        print(f"{first_num} {operation} {second_num} = {solution}")
        choice = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            first_num = solution
            continue
        elif choice == "n":
            print("\n"*100)
            break
        elif choice not in ["y", "n"]:
            print("Invalid Input.")
            quit()
