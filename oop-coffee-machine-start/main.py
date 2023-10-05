from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
cashier = MoneyMachine()
is_on = True


while is_on:
    order = input(f'What would you like to order?\n{menu.get_items()}\n')
    if order == 'report':
        coffee_machine.report()
        cashier.report()
    elif order == 'n' or order == 'off':
        print('Powering down. Goodbye.')
        is_on = False
    else:
        order_menuitem = menu.find_drink(order)
        print(f'You ordered a {order_menuitem.name}')
        if coffee_machine.is_resource_sufficient(order_menuitem):
            if cashier.make_payment(order_menuitem.cost):
                coffee_machine.make_coffee(order_menuitem)



