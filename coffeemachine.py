# imports
import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# variables
money = 0
POWER = True


# functions


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear():
    os.system('clear')


def report():
    for key in resources:
        print(f'{key}: {resources[key]}')
    print(f'Cash: ${money}')
    remain = input('Continue with order? Y or N\n')
    if remain == 'n':
        turn_off()


def calculate():
    total = float(0)
    total += quarters * 0.25
    total += dimes * 0.1
    total += nickles * 0.05
    total += pennies * 0.01
    return total


def check_resource(drink):
    for ingre, amount in MENU[drink]['ingredients'].items():
        if resources[ingre] < amount:
            return False
        else:
            return True


def make_drink(drink):
    for ingre, amount in MENU[drink]['ingredients'].items():
        resources[ingre] -= amount


def turn_off():
    print('Turning off coffee machine. Goodbye.')
    exit()


# START
while POWER:
    clear_screen()
    order = input('''
Hi there! What coffee would you like to have today?
Espresso, Latte or Cappuccino?
''')
    if order == 'report':  # generates report from first input
        report()
    elif order == 'off':  # turns off machine from first input
        turn_off()
    else:
        check_resource(order)  # checks resources

        if not check_resource(order):
            print('Sorry, we do not have enough ingredients for this drink!')
            reply = input('Would you like to order something else? Y or N\n')
            if reply == 'y':
                continue

        elif check_resource(order):
            order_cost = MENU[order]['cost']
            print(f'You ordered a {order}. It costs ${order_cost}. Please insert coins.')
            quarters = float(input('How many quarters?'))
            dimes = float(input('How many dimes?'))
            nickles = float(input('How many nickles?'))
            pennies = float(input('How many pennies?'))

            if calculate() < order_cost:
                print(f'''
                Sorry, that is not enough money.
                A {order} costs ${order_cost}. You paid {calculate()}.
                Money refunded.
                ''')

            change = calculate() - order_cost
            print(f'\nHere is your {order}.')

            if change > 0:
                print(f'and here is ${change} in change.')

            print('Enjoy!')

            make_drink(order)
            money += MENU[order]['cost']

            next_order = input('Would you like another cup of coffee? Y or N?')

            if next_order == 'n':
                POWER = False
