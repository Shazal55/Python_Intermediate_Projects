from Coffee_menu import menu
from Coffee_menu import available_items
from Coffee_menu import logo
def insert_coin():
    global total_amount
    print("Please insert coin")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_amount = (0.25 * quarters)+(0.10 * dimes)+(0.05 * nickles) + (0.01 * pennies)
def choice(drink):
    global change
    if available_items["water in ml"]< menu[drink]["ingredients"]["water in ml"]:
        print("sorry! we are out of water")
        return
    elif available_items["coffee in g"] < menu[drink]["ingredients"]["coffee in g"]:
        print("sorry! we are out of coffee")
        return
    elif available_items["milk in ml"] < menu[drink]["ingredients"]["milk in ml"]:
        print("Sorry! We are out of milk.")
        return

    insert_coin()
    cost = menu[drink]["price"]
    if total_amount >= cost:
        change = round((total_amount - cost),2)
        available_items["money"] +=cost
        print(f"Your change is : {change}$")
        print(f"Here's your {drink}🍵. Enjoy!")
        available_items["water in ml"] -= menu[drink]["ingredients"]["water in ml"]
        available_items["coffee in g"] -= menu[drink]["ingredients"]["coffee in g"]
        available_items["milk in ml"] -= menu[drink]["ingredients"]["milk in ml"]
    else:
        print(f"Not enough money!, The {drink} costs {cost}$. Money refunded!")
def keep_running():
    running = input("Do you want to continue using machine? Y/N: ")
    if running.lower() == "n":
        return False
    else:
        return True
total_amount = 0
change = 0
machine_running = True
print(logo)
while machine_running:

    user_choice = input("What would you like? (espresso, latte or cappuccino): ").lower()
    if user_choice == "report":
        print(f"water in ml : {available_items['water in ml']} ml")
        print(f"milk in ml : {available_items['milk in ml']} ml")
        print(f"coffee in g: {available_items['coffee in g']} g")
        print(f"money : {available_items['money']} $")
        machine_running = keep_running()
    elif user_choice in menu:
        choice(user_choice)
        machine_running = keep_running()
    else:
        print("Sorry, Invalid Input")
        machine_running = keep_running()