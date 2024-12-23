menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

value_of_quarter = 0.25
value_of_dime = 0.10
value_of_nickel = 0.05
value_of_penny = 0.01

logo = ('''
   ______      ________             __  ___           __    _          
  / ____/___  / __/ __/__  ___     /  |/  /___ ______/ /_  (_)___  ___ 
 / /   / __ \/ /_/ /_/ _ \/ _ \   / /|_/ / __ `/ ___/ __ \/ / __ \/ _ |
/ /___/ /_/ / __/ __/  __/  __/  / /  / / /_/ / /__/ / / / / / / /  __/
\____/\____/_/ /_/  \___/\___/  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/ 
                                                                              
''')

def are_resources_sufficient(userchoice, definedmenu, machine_resources):
    requirements = definedmenu[userchoice]["ingredients"]
    if machine_resources["water"]>= requirements["water"]:
        if machine_resources["milk"]>= requirements["milk"]:
            if machine_resources["coffee"]>= requirements["coffee"]:
                return True
            else:
                return "Sorry, there is not enough coffee."
                
        else: 
            return "Sorry, there is not enough milk."
            
    else: 
        return "Sorry, there is not enough water."
    
def deduct_ingredients(userchoice, definedmenu, machine_resources):
    requirements = definedmenu[userchoice]["ingredients"]
    machine_resources["water"] -= requirements["water"]
    machine_resources["milk"] -= requirements["milk"]
    machine_resources["coffee"] -= requirements["coffee"]
    return machine_resources

coffeemachine_is_on = True

while coffeemachine_is_on:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Please enter a valid choice.")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        coffeemachine_is_on = False
        break

    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")

    else:
        if are_resources_sufficient(choice, menu, resources) == True:
            print("Please insert coins.")
            while True:
                try:
                    no_of_quarters = float(input("How many quarters?: "))
                    no_of_dimes = float(input("How many dimes?: "))
                    no_of_nickels = float(input("How many nickels?: "))
                    no_of_pennies = float(input("How many pennies?: "))
                    if no_of_quarters < 0 or no_of_dimes < 0 or no_of_nickels < 0 or no_of_pennies < 0:
                        print("Please enter only non-negative numbers for coins.")
                        continue
                    break
                except:
                    print("Please enter a valid number.")
            user_money = value_of_quarter*no_of_quarters + value_of_dime*no_of_dimes + value_of_nickel*no_of_nickels + value_of_penny*no_of_pennies
            cost_of_coffee = menu[choice]["cost"]
            if user_money<cost_of_coffee:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                profit += cost_of_coffee
                if user_money>cost_of_coffee:
                    change = user_money - cost_of_coffee
                    change = round(change, 2)
                    print(f"Here is ${change} in change.")
                deduct_ingredients(choice, menu, resources)
                print(f"Here's your {choice} 🫖🧋, Enjoy!")

        else:
            print(are_resources_sufficient(choice, menu, resources))
