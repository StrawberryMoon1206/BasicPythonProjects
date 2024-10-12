print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
tipaspercent = tip/100
people = int(input("How many people to split the bill? "))
payperperson = float(round((bill + bill*tipaspercent)/people,2))
print(f"Each person should pay: ${payperperson}")
