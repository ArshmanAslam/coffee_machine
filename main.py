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


def coffee_info(user_selected, data_of_coffee):
    coff_inf = data_of_coffee[user_selected]['ingredients']
    return coff_inf


def check_for_resources(coffee_ingredients, machine):
    avl_water = machine['water']
    avl_milk = machine['milk']
    avl_coffee = machine['coffee']

    water = coffee_ingredients['water']
    coffee_user = coffee_ingredients['coffee']

    if 'milk' in coffee_ingredients:
        milk = coffee_ingredients['milk']
        if avl_milk > milk:
            remaining_milk = avl_milk - milk
            machine['milk'] = remaining_milk

    if avl_water > water and avl_coffee > coffee_user:
        remaining_water = avl_water - water
        machine['water'] = remaining_water
        remaining_coffee = avl_coffee - coffee_user
        machine['coffee'] = remaining_coffee
        return True

    else:
        print("Out Of Resources :(")
        return False


def total_price_maker(coffee_name, coffee_data, profit):
    quarters = int(input("How many quarters ?"))
    dimes = int(input('How many dimes ?'))
    nickles = int(input("How many nickles?"))
    pennies = int(input("how many pennies?"))

    coffee_price = coffee_data[coffee_name]['cost']
    user_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

    if user_money >= coffee_price:
        remaining = user_money - coffee_price
        profit['money'] = coffee_price
        print(f"Here Is ${round(remaining, 2)} Dollars in Change")
        print(f"Here Is Your {user}☕ Enjoy!😊")
        return True
    elif user_money < coffee_price:
        print(f"Sorry that's not enough money. Money refunded.${user_money}")
        return False


def report(r):
    rep = []
    for x in r:
        rep.append(x)
    print(f'{rep[0]} : {r["water"]}ml')
    print(f"{rep[1]} : {r['milk']}ml")
    print(f"{rep[2]} : {r['coffee']}g")
    print(f"{rep[3]} : ${r['money']}")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}

machine_on = True

while machine_on:
    user = input("What would you like? (espresso/latte/cappuccino):")
    if user in ['espresso', 'latte', 'cappuccino']:
        print("Insert Coins")
        coffee = coffee_info(user, MENU)
        if check_for_resources(coffee, resources):
            total_price_maker(user, MENU, resources)

    elif user == 'off':
        machine_on = False
    elif user == 'report':
        report(resources)


