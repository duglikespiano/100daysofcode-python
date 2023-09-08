MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 3000,
    "milk": 2000,
    "coffee": 100,
}

keep_going = True


def calculate_user_input(user_choice_coffee):
    print(f"You have chosen {user_choice_coffee}, Please insert coins.")
    quarters_total = input("how many quarters?: ")
    if len(quarters_total) == 0:
        quarters_total = 0
    else:
        quarters_total = int(quarters_total) * 0.25

    dimes_total = input("how many dimes?: ")
    if len(dimes_total) == 0:
        dimes_total = 0
    else:
        dimes_total = int(dimes_total) * 0.1

    nickles_total = input("how many nickles?: ")
    if len(nickles_total) == 0:
        nickles_total = 0
    else:
        nickles_total = int(nickles_total) * 0.05

    pennies_total = input("how many pennies?: ")
    if len(pennies_total) == 0:
        pennies_total = 0
    else:
        pennies_total = int(pennies_total) * 0.01

    all_total = quarters_total + dimes_total + nickles_total + pennies_total
    return all_total


def consume_indegrient(user_choice_coffee):
    if (user_choice_coffee == "espresso"):
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif (user_choice_coffee == "latte"):
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif (user_choice_coffee == "cappuccino"):
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]


def check_menu_before_making(user_choice_coffee):
    global profit
    if user_choice_coffee == "espresso":
        if (user_input_total > MENU[user_choice_coffee]["cost"]) and (resources["water"] - MENU[user_choice_coffee]["ingredients"]["water"]) >= 0 and (resources["coffee"] - MENU[user_choice_coffee]["ingredients"]["coffee"] >= 0):
            change = round(user_input_total -
                           MENU[user_choice_coffee]["cost"], 2)
            consume_indegrient(user_choice_coffee)
            profit += user_input_total
            print(
                f"Here's your change {change} and your {user_choice_coffee}. ☕️")
        elif (user_input_total < MENU[user_choice_coffee]["cost"]):
            print("​Sorry that's not enough money. Money refunded.​")
        else:
            print("Ingridents are not enough. Please make a different order.")
    else:
        if (user_input_total > MENU[user_choice_coffee]["cost"]) and (resources["water"] - MENU[user_choice_coffee]["ingredients"]["water"]) >= 0 and (resources["milk"] - MENU[user_choice_coffee]["ingredients"]["milk"]) >= 0 and (resources["coffee"] - MENU[user_choice_coffee]["ingredients"]["coffee"] >= 0):
            consume_indegrient(user_choice_coffee)
            profit += user_input_total
            print(f"Here's your {user_choice_coffee}. ☕️")
        elif (user_input_total < MENU[user_choice_coffee]["cost"]):
            print("​Sorry that's not enough money. Money refunded.​")
        else:
            print("Ingridents are not enough. Please make a different order.")


print("Welcome to Dug's cafe☕️")

while (keep_going):
    user_choice_coffee = input(
        "What would you like? (espresso/latte/cappuccino): ")
    if user_choice_coffee == 'report':
        print(f""" 
        Water : {resources['water']},
        Milk : {resources['milk']}
        Coffee : {resources['coffee']}
        Money : {profit}
    """)
    elif user_choice_coffee == 'exit':
        print('Coffee machine is turning off')
        keep_going = False
    elif user_choice_coffee == "espresso" or user_choice_coffee == "latte" or user_choice_coffee == "cappuccino":
        print(f"You've chosen {user_choice_coffee}")
        user_input_total = calculate_user_input(user_choice_coffee)
        check_menu_before_making(user_choice_coffee)
    else:
        print("You've made a wrong order. ")
