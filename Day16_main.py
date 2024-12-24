from Day16_menu import Menu, MenuItem
from Day16_coffeemaker import CoffeeMaker
from Day16_moneymachine import MoneyMachine

coffeemachine = CoffeeMaker()
coinmachine = MoneyMachine()
machinemenu = Menu()
coffeemachine_is_on = True
while coffeemachine_is_on:
    choice = input(f"What would you like? ({machinemenu.get_items()}): ").lower()
    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        coffeemachine_is_on = False
        break
    
    elif choice == "report":
        coffeemachine.report()
        coinmachine.report()
        continue
    
    else: 
        #first we have to ask user for input and set chosen coffee as drink to get access to its sttributes like ingredients and cost
        drink = machinemenu.find_drink(choice) 
        try:
            if coffeemachine.is_resource_sufficient(drink):  
                try: 
                    #even though function is written with if, it gets executed and we get all of its functionality rather than only return value
                    if coinmachine.make_payment(drink.cost):  
                        coffeemachine.make_coffee(drink)  
                    else:
                        continue
                except ValueError:
                    print("Please enter valid denominations.")
                    continue
        except AttributeError:  #if choice entered not a valid drink
            print("Please enter a valid drink.")
            continue
